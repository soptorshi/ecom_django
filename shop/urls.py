from django.urls import path
from shop import views

urlpatterns = [
    path('shop',views.Shop.as_view(), name='shop'),
    path('cart',views.Cart.as_view(), name='cart'),
]
