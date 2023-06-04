<<<<<<< HEAD
from django.urls import path
from shop import views

urlpatterns = [
    path('shop',views.Shop.as_view(), name='shop'),
    path('cart',views.Cart.as_view(), name='cart'),
]
=======
from django.urls import path
from shop import views

urlpatterns = [
    # path('shop',views.Shop.as_view(), name='shop'),
    path('shop',views.Shop.as_view(),name='shop'),
    path('search_icecreams',views.Search_icecreams.as_view(),name='search_icecreams'),
    path('cart',views.Cart.as_view(), name='cart'),
    # path('checkout',views.checkout, name='checkout'),
    path('success',views.success,name='success'),
]
>>>>>>> b8f1ac3 (added payment gateway)
