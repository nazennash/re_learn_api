from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Product
from rest_framework.reverse import reverse
from .validators import validate_title, unique_product_title

class ProductSerializer(ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    discount = serializers.SerializerMethodField(read_only=True)
    new_url = serializers.HyperlinkedIdentityField(
        view_name='products-detail',
        lookup_field='pk',
        # source='get_absolute_url', 
        read_only=True
        )
    
    # email = serializers.EmailField(write_only=True)
    title = serializers.CharField(validators=[validate_title, unique_product_title])

    class Meta:
        model = Product
        fields = ['id', 'title', 'content', 'price', 'sales_price', 'discount', 'url', 'new_url']
        # fields = "__all__"
        read_only_fields = ['sales_price']
    
    def get_discount(self, obj):
        try:
            return obj.get_discount()
        except Exception as e:
            return None
    
    def get_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('products-detail', kwargs={'pk': obj.pk}, request=request)

    def create(self, validated_data):
        email = validated_data.pop('email')
        obj = Product.objects.create(**validated_data)
        print (obj, email) 
        return obj
        # return Super().create(validated_data)
    