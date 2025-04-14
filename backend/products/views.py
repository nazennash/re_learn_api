# # from django.shortcuts import render
# # from . models import Product
# # import json
# # from django.forms.models import model_to_dict
# # from rest_framework.response import Response
# # from rest_framework.decorators import api_view
# # from rest_framework import status
# # from .serializers import ProductSerializer
# # # Create your views here.

# # @api_view(['GET', 'POST'])
# # def index(request):

# #     if request.method == 'GET':

# #         model_data = Product.objects.all().order_by('?').first()
# #         data = {}

# #         # # print(dir(model_data))
# #         # print(model_data.sales_price)

# #         if model_data:
# #             serializer = ProductSerializer(model_data)
# #             data = serializer.data

# #         # if model_data:
# #         #     data = model_to_dict(model_data, fields=['id', 'title', 'content', 'price', 'sales_price'])

# #         return Response(data, status=status.HTTP_200_OK)
    
# #     elif request.method == 'POST':
# #         data = request.data
# #         # print(data)
# #         serializer = ProductSerializer(data=data)

# #         if serializer.is_valid(raise_exception=True):
# #             print(f"Validated Data: {serializer.validated_data}")
# #             # serializer.save()
# #             print(f"Output Data: {serializer.data}")
            
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)

# #         # return Response(data, status=status.HTTP_201_CREATED)
        
# #         # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# from rest_framework import generics
# from .models import Product
# from .serializers import ProductSerializer
# from rest_framework.response import Response
# from rest_framework import status, permissions, authentication
# from .permissions import IsStaffEditorPermission
# from .authentication import Tokenizer

# # class ProductDetailAPIView(generics.RetrieveAPIView):
# #     queryset = Product.objects.all()
# #     serializer_class = ProductSerializer
# #     lookup_field = 'pk' 

# # class ProductCreateAPIView(generics.CreateAPIView):
# #     queryset = Product.objects.all()
# #     serializer_class = ProductSerializer

# class ProductListAPIView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     # authentication_classes = [authentication.SessionAuthentication]
#     permission_classes = [permissions.IsAuthenticated]
#     authentication_classes = [
#         # authentication.SessionAuthentication,
#         # authentication.TokenAuthentication,
#         Tokenizer
#         ]

#     def get(self, request, *args, **kwargs):
#         # print(request.user)
#         # print(request.user.is_authenticated)
#         # print(dir(request.auth))
#         queryset = self.get_queryset()
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     # permission_classes = [IsStaffEditorPermission]
#     # authentication_classes = [authentication.SessionAuthentication]
#     # authentication_classes = [authentication.TokenAuthentication]

from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializers import ProductSerializer

class ProductViewset(ModelViewSet):
    """
    nash
    """

    # oliver
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        # user = self.request.user
        # print(user)
        # return Product.objects.filter(user=user)
        return qs.filter(user=user)