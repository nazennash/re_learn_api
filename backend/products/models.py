from django.db import models
from decimal import Decimal
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db.models import Q

# User = settings.AUTH_USER_MODEL
User = get_user_model()

# Create your models here.

class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)
    
    def search(self, query, user=None):
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        qs = self.is_public().filter(lookup)
        if user is not None:
            qs2 = self.filter(user=user).filter(lookup)
            qs = (qs | qs2).distinct()
        return qs

class ProductManager(models.Manager):

    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def search(self, query, user=None):
        return self.get_queryset().search(query, user=user)

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=1)
    title = models.CharField(max_length=255)
    content = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=99.99)
    public = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    @property
    def sales_price(self):
        return "{:.2f}".format(self.price * Decimal('0.9'))
        # return self.price * 0.9
    
    def get_discount(self):
        return self.price * Decimal('0.9')
    
    objects = ProductManager()
