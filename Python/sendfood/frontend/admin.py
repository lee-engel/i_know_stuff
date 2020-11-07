from django.contrib import admin
from .models import MenuItem, MenuCategory, Order, OrderItem, UserProfile, Cart


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'description')
    list_display = ('name', 'description')


@admin.register(MenuItem)
class MenuCategoryAdmin(admin.ModelAdmin):
    fields = ('item_name', 'description', 'is_available', 'price', 'special_price')
    list_display = ('item_name', 'description', 'is_available', 'price', 'special_price')


admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(UserProfile)
admin.site.register(Cart)
