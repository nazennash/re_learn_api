from django.shortcuts import render
from . models import Product
import json
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ProductSerializer
# Create your views here.

@api_view(['GET', 'POST'])
def index(request):

    if request.method == 'GET':

        model_data = Product.objects.all().order_by('?').first()
        data = {}

        # # print(dir(model_data))
        # print(model_data.sales_price)

        if model_data:
            serializer = ProductSerializer(model_data)
            data = serializer.data

        # if model_data:
        #     data = model_to_dict(model_data, fields=['id', 'title', 'content', 'price', 'sales_price'])

        return Response(data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        data = request.data
        # print(data)
        serializer = ProductSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            print(f"Validated Data: {serializer.validated_data}")
            # serializer.save()
            print(f"Output Data: {serializer.data}")
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # return Response(data, status=status.HTTP_201_CREATED)
        
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)