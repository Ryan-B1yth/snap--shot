""" Imports """
from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """ Order line item admin """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """ Order admin """
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = (
        'order_no',
        'delivery_amount',
        'order_amount',
        'grand_total',
        'date',
        'original_basket',
        'stripe_pid'
    )

    fields = (
        'order_no',
        'user_profile',
        'date',
        'name',
        'email',
        'phone_number',
        'country',
        'postcode',
        'city',
        'address_1',
        'address_2',
        'county',
        'delivery',
        'order_total',
        'grand_total',
        'original_basket',
        'stripe_pid'
        )

    list_display = (
        'order_no',
        'date',
        'name'
    )

    ordering = (
        '-date',
    )


admin.site.register(Order, OrderAdmin)
