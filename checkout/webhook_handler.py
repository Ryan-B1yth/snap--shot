from django.http import HttpResponse
from checkout.models import Order, OrderLineItem
from products.models import Product

import json
import time


class StripeWebhookHandler:
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
    
    def handle_payment_intent_succeeded(self, event):
        intent = event.data.object
        pid = intent.id
        basket = intent.metadata.basket
        # save_location = intent.metadata.save_location

        billing_details = intent.charges.data[0].billing_details
        shipping = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        for field, value in shipping.address.items():
            if value == "":
                shipping.address[field] = None
        
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
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    name=shipping.name,
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
                        for size, quantity in item_data['items_by_size'].items():
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
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)
    
    def handle_payment_intent_failed(self, event):
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
