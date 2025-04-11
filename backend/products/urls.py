from django.urls import path, include
# from .views import ProductListAPIView
from rest_framework.authtoken.views import ObtainAuthToken
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('products', views.ProductViewset, basename='products')

urlpatterns = [
    # path('<int:pk>/', ProductDetailAPIView.as_view(), name='index'),
    # path('', ProductCreateAPIView.as_view(), name='create'),
    # path('list/', ProductListAPIView.as_view(), name='list'),
    # path('auth/', ObtainAuthToken.as_view(), name='token' ),
    path('', include(router.urls)),
]