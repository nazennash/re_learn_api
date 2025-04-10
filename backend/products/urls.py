from django.urls import path

from .views import ProductListAPIView

urlpatterns = [
    # path('<int:pk>/', ProductDetailAPIView.as_view(), name='index'),
    # path('', ProductCreateAPIView.as_view(), name='create'),
    path('list/', ProductListAPIView.as_view(), name='list'),
]