from django.db import models
from django.contrib.auth.models import User

DELIVERY_OPTIONS = [('Deliver', 'Collect')]
PAYMENT_OPTIONS = [('Cash', 'Cash'), ('Card', 'Card')]
ORDER_STATES = [('New', 'New'), ('Making', 'Making'), ('Out', 'Out'),
                ('Cancelled', 'Cancelled'), ('Delivered', 'Delivered')]


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cell_number = models.CharField(max_length=16)
    last_address = models.CharField(max_length=250)


class MenuCategory(models.Model):
    name = models.CharField(max_length=16, unique=True)
    description = models.CharField(max_length=200)


class MenuItem(models.Model):
    item_name = models.CharField(max_length=64, unique=True)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    is_available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    special_price = models.DecimalField(max_digits=4, decimal_places=2)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    notes = models.CharField(max_length=150)
    cdate = models.DateTimeField(auto_now_add=True)
    mdate = models.DateTimeField(auto_now=True)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_option = models.CharField(max_length=16, choices=DELIVERY_OPTIONS)
    delivery_address = models.CharField(max_length=250)
    order_total = models.DecimalField(max_digits=4, decimal_places=2)
    tip_total = models.DecimalField(max_digits=4, decimal_places=2)
    notes = models.CharField(max_length=150)
    payment_method = models.CharField(max_length=32, choices=PAYMENT_OPTIONS)
    order_state = models.CharField(max_length=32, choices=ORDER_STATES)
    cdate = models.DateTimeField(auto_now_add=True)
    mdate = models.DateTimeField(auto_now=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    final_price = models.DecimalField(max_digits=4, decimal_places=2)
    notes = models.CharField(max_length=150)
