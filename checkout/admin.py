from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
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

    list_display = (
        'order_no',
        'date',
        'name'
    )

    ordering = (
        '-date',
    )


admin.site.register(Order, OrderAdmin)
