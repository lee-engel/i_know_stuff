from django.contrib import admin
from .models import MenuItem, MenuCategory, Order, OrderItem, UserProfile, Cart


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'description')
    list_display = ('name', 'description')


admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(UserProfile)
admin.site.register(Cart)
