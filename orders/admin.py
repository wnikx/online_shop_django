from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id',  'first_name', 'last_name',
                    'address', 'city', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated', 'order_detail']
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderDetail(admin.ModelAdmin):
    list_display = ['order', 'product', 'price', 'quantity']
