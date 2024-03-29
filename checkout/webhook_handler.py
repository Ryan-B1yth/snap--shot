import json
import time

from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from checkout.models import Order, OrderLineItem
from products.models import Product
from profiles.models import Profile


class StripeWebhookHandler:
    """ Stripe webhook handler """
    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/email_subject.txt',
            {'order': order}
        )
        body = render_to_string(
            'checkout/confirmation_emails/email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL}
        )

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [email]
            )

    def handle_event(self, event):
        """ Handle event """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """ Handle payment intent succeeded """
        intent = event.data.object
        pid = intent.id
        basket = intent.metadata.basket
        save_location = intent.metadata.save_location

        billing_details = intent.charges.data[0].billing_details
        shipping = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        for field, value in shipping.address.items():
            if value == "":
                shipping.address[field] = None

        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = Profile.objects.get(user__username=username)
            if save_location:
                profile.default_phone_number = shipping.phone
                profile.default_country = shipping.address.country
                profile.default_postcode = shipping.address.postal_code
                profile.default_city = shipping.address.city
                profile.default_address_1 = shipping.address.line1
                profile.default_address_2 = shipping.address.line2
                profile.default_county = shipping.address.state
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    name__iexact=shipping.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping.phone,
                    country__iexact=shipping.address.country,
                    postcode__iexact=shipping.address.postal_code,
                    city__iexact=shipping.address.city,
                    address_1__iexact=shipping.address.line1,
                    address_2__iexact=shipping.address.line2,
                    county__iexact=shipping.address.state,
                    grand_total=grand_total,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'WH received: {event["type"]} | SUCCESS: Order in DB',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    name=shipping.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=shipping.phone,
                    country=shipping.address.country,
                    postcode=shipping.address.postal_code,
                    city=shipping.address.city,
                    address_1=shipping.address.line1,
                    address_2=shipping.address.line2,
                    county=shipping.address.state,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(basket).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in (
                                item_data['items_by_size'].items()):
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'WH: {event["type"]} | SUCCESS: Created order',
            status=200)

    def handle_payment_intent_failed(self, event):
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
