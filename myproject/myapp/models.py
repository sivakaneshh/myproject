# myapp/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class Item(models.Model):

    name = models.CharField(max_length=100, unique=True)
    price = models.IntegerField(default = 0)
    quantity = models.IntegerField(default = 0)
    description = models.TextField()

class UserProfile(AbstractUser):

    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    ph_no = models.IntegerField(default = 0)
    password = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
    
    def __str__(self):
        return self.name
    
UserProfile._meta.get_field('groups').remote_field.related_name = 'user_profiles_groups'
UserProfile._meta.get_field('user_permissions').remote_field.related_name = 'user_profiles_permissions'

class Order(models.Model):

    status = models.CharField(max_length=50)
    transaction = models.CharField(max_length=50)
    user = models.OneToOneField(UserProfile, on_delete = models.CASCADE)

    def get_total(self):
        total = 0
        for order in self.order_unit_set.all():
            total += order.get_price()
        return total

class OrderUnits(models.Model):

    quantity = models.IntegerField()
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    orders = models.ForeignKey(Order, on_delete = models.CASCADE)
    
    def get_price(self):
        return self.price * self.quantity
    
class RazorpayOrder(models.Model):
    pass