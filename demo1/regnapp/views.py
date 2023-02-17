from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        usename = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=usename, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid user")
            return redirect('login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        usename = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        ema = request.POST['email']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=usename).exists():
                messages.info(request, "user exists")
                return redirect('register')
            elif User.objects.filter(password=password).exists():
                messages.info(request, "password exists")
                return redirect('register')
            elif User.objects.filter(email=ema).exists():
                messages.info(request, "email exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=usename, first_name=first_name, last_name=last_name,
                                                password=password, email=ema)
                user.save();
                return redirect("login")
        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('/')

    return render(request, 'regn.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

