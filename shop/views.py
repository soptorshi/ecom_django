from django.shortcuts import render, redirect
from django.views import View
from home.models import Icecream
from shop.models import Cart_item, Shop_item

# Create your views here.

class Shop(View):

    def get(self, request):
        shop_items = Shop_item.objects.all()
        context = {
            'shop_items':shop_items
        }
        return render(request,'shop.html',context)

    def post(self, request):
        prod_id = request.POST.get('prod_id')
        obj = Shop_item.objects.filter(id__in = [prod_id])
        name = obj.values('name')
        price = obj.values('price')
        net_weight = obj.values('net_weight')
        flavour = obj.values('flavour')
        cart_item = Cart_item(name=name,price=price,net_weight=net_weight,flavour=flavour)
        cart_item.save(self)
        return redirect('shop')

class Cart(View):
    def get(self, request):
        cart_items = Cart_item.objects.all()
        context = {
            'cart_items':cart_items
        }
        return render(request,'cart.html',context)
    
    def post(self, request):
        prod_id = request.POST.get('prod_id')
        obj = Cart_item.objects.filter(id__in = [prod_id])
        obj.delete()
        return redirect('cart')

