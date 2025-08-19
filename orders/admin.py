# Register your models here.
from django.contrib import admin
from .models import Menu, Order, OrderItem

# Inline to show items inside an order
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "available")
    search_fields = ("name",)
    list_filter = ("available",)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "status", "total_amount", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("customer__username", "id")
    inlines = [OrderItemInline]