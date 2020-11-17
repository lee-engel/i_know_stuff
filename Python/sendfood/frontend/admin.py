from django.contrib import admin
from .models import MenuItem, MenuCategory, Order, OrderItem, UserProfile, Cart


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'description')
    list_display = ('name', 'description')


@admin.register(MenuItem)
class MenuCategoryAdmin(admin.ModelAdmin):
    fields = ('item_name', 'category', 'description', 'is_available', 'price', 'special_price',
              'item_image_1', 'item_image_2', 'item_image_3')
    list_display = ('item_name', 'category', 'description', 'is_available', 'price', 'special_price')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'cdate', 'order_total', 'tip_total', 'payment_method', 'order_state')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'item', 'final_price')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'cell_number', 'last_address')


admin.site.register(Cart)
