from django.db import models
# Create your models here.

class Product(models.Model):
    web_id = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    # class Meta:
    #     permissions = (
    #         ('can_view_item', 'Can view item'),
    #         ('can_add_item', 'Can add item'),
    #         ('can_edit_item', 'Can edit item'),
    #         ('can_delete_item', 'Can delete item'),
            
    #     )