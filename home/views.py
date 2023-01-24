from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout, authenticate, login
from home.models import Icecream, Contact

# Create your views here.
# username and password :
#  boi, boi
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        # print('contact working')
        name    = request.POST.get('name')
        email   = request.POST.get('email')
        phone   = request.POST.get('phone')
        desc    = request.POST.get('desc')
        contact = Contact(name = name,email = email,phone = phone,desc = desc)
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')

    # return HttpResponse("this is the contact")

def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        if password == confirmpassword:
            if User.objects.filter(username = username).exists():
                messages.info(request,'Username not available')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.info(request,'e-mail already in use')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password,email=email,first_name=fname,last_name=lname)
                user.save()
                messages.info(request,'User created!')
                return redirect('login')

        else:
            messages.info(request,'Password does not match. Try again.')
        return redirect('register')
    else:
        return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password = password)

        if user is not None:
            auth.login(request, user)
            messages.info(request,'You are successfully logged in.')
            return redirect('/')
            
        else:
            messages.info(request,'Wrong credentials.')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
        
def icecream(request):
    if request.method == "POST":
        name    = request.POST.get('name')
        price   = request.POST.get('price')
        net_weight   = request.POST.get('net_weight')
        flavour    = request.POST.get('flavour')
        icecream = Icecream(name = name,price = price,net_weight = net_weight,flavour = flavour)
        icecream.save()


        
