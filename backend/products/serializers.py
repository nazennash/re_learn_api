from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Product

class ProductSerializer(ModelSerializer):

    discount = serializers.SerializerMethodField(read_only=True)

    def get_discount(self, obj):
        # try:
        #     return obj.get_discount()
        # except Exception as e:
        #     return None
        if not hasattr(obj, 'id'):
            return None


    class Meta:
        model = Product
        fields = ['id', 'title', 'content', 'price', 'sales_price', 'discount']
        read_only_fields = ['sales_price']