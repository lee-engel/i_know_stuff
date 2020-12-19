from django.db import models
from django.contrib.auth.models import User

DELIVERY_OPTIONS = [('Deliver', 'Deliver'), ('Collect', 'Collect')]
PAYMENT_OPTIONS = [('Cash', 'Cash'), ('Card', 'Card')]
ORDER_STATES = [('New', 'New'), ('Making', 'Making'), ('Out', 'Out'),
                ('Cancelled', 'Cancelled'), ('Delivered', 'Delivered')]


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cell_number = models.CharField(max_length=16)
    last_address = models.CharField(max_length=250)

    def __str__(self):
        return self.user.username


class MenuCategory(models.Model):
    name = models.CharField(max_length=16, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    item_name = models.CharField(max_length=64, unique=True)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    is_available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    special_price = models.DecimalField(max_digits=11, decimal_places=2, blank=True, default=0)
    item_image_1 = models.ImageField("Image #1", upload_to='frontend/static/menu', blank=True)
    item_image_2 = models.ImageField("Image #2", upload_to='frontend/static/menu', blank=True)
    item_image_3 = models.ImageField("Image #3", upload_to='frontend/static/menu', blank=True)

    def __str__(self):
        return self.item_name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    notes = models.CharField(max_length=150)
    cdate = models.DateTimeField(auto_now_add=True)
    mdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_option = models.CharField(max_length=16, choices=DELIVERY_OPTIONS)
    delivery_address = models.CharField(max_length=250)
    order_total = models.DecimalField(max_digits=11, decimal_places=2, default=0.00)
    tip_total = models.DecimalField(max_digits=11, decimal_places=2, default=0.00)
    notes = models.CharField(max_length=150, blank=True)
    payment_method = models.CharField(max_length=32, choices=PAYMENT_OPTIONS)
    order_state = models.CharField(max_length=32, choices=ORDER_STATES)
    cdate = models.DateTimeField(auto_now_add=True)
    mdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    final_price = models.DecimalField(max_digits=11, decimal_places=2)
    notes = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return "{} {}".format(self.order.user.username, self.item.item_name)


class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_amount = models.DecimalField(max_digits=11, decimal_places=2, default=0.00)
    payment_method = models.CharField(max_length=32, choices=PAYMENT_OPTIONS)
    notes = models.CharField(max_length=150, blank=True)
    cdate = models.DateTimeField(auto_now_add=True)
    mdate = models.DateTimeField(auto_now=True)
