from django.db import models
from decimal import Decimal

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=99.99)
    
    def __str__(self):
        return self.title
    
    @property
    def sales_price(self):
        return "{:.2f}".format(self.price * Decimal('0.9'))
        # return self.price * 0.9
    
    def get_discount(self):
        return self.price * Decimal('0.9')
