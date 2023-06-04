<<<<<<< HEAD
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

=======
from django.shortcuts import render, redirect
from django.views import View
from home.models import Icecream
from shop.models import Cart_item, Shop_item
import razorpay
from django.views.decorators.csrf import csrf_exempt

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


class Search_icecreams(View):

    def get(self, request):
        searched = request.POST.get('searched', False)
        shop_items = Shop_item.objects.filter(name__contains = searched)
        context = {
            'searched':searched,
            'shop_items':shop_items
        }
        return render(request,'search.html',context)

    def post(self, request):
        prod_id = request.POST.get('prod_id')
        obj = Shop_item.objects.filter(id__in = [prod_id])
        name = obj.values('name')
        price = obj.values('price')
        net_weight = obj.values('net_weight')
        flavour = obj.values('flavour')
        cart_item = Cart_item(name=name,price=price,net_weight=net_weight,flavour=flavour)
        cart_item.save(self)
        return redirect('search_icecreams')


class Cart(View):
    def get(self, request):
        cart_items = Cart_item.objects.all()
        cart_prices = cart_items.values('price')
        sum_total = 0
        for i in cart_prices:
            sum_total += i['price']
        context = {
            'cart_items':cart_items,
            'sum_total':sum_total,
            'sum_total_paise':sum_total*100,
        }
        client = razorpay.Client(auth=("rzp_test_1SwcwlEpZjr8MN", "ipQMFSqbma23ZiSIsvwkZakl"))

        DATA = {
            "amount": 100,
            "currency": "INR",
            "receipt": "receipt#1",
            "payment_capture": "1"
        }
        payment = client.order.create(data=DATA)
        return render(request,'cart.html',context)
    
    def post(self, request):
        prod_id = request.POST.get('prod_id')
        obj = Cart_item.objects.filter(id__in = [prod_id])
        obj.delete()
        return redirect('cart')

@csrf_exempt
def success(request):
    return render(request,'success.html')

# def checkout(request):
#     cart_prices = Cart_item.objects.all().values('price')
#     sum_total = 0
#     for i in cart_prices:
#        sum_total += i['price']
#     context = {
#             'sum_total':sum_total,
#             'sum_total_paise':sum_total_paise
#     }
    
#     return render(request, 'checkout.html', context)


>>>>>>> b8f1ac3 (added payment gateway)
