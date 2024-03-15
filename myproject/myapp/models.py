# myapp/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class UserProfile(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    
    def __str__(self):
        return self.name
    
UserProfile._meta.get_field('groups').remote_field.related_name = 'user_profiles_groups'
UserProfile._meta.get_field('user_permissions').remote_field.related_name = 'user_profiles_permissions'

class Order(models.Model):
    amount = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100)
    paid = models.BooleanField(default = False)