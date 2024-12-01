from django.shortcuts import render , redirect
from django.http import request , HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

# Create your views here.
@csrf_protect
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request=request , username=username , password=password)
        if user is not None:
            login(request , user)
            return redirect('home')
        else:
            messages.error(request, "invalide username or password")
            return redirect('login')
    
    return render(request, "login/index.html")


@csrf_protect
def signup(request):    
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        passwordconfirm = request.POST.get("passwordconfirm")
        user_data_has_error = False

        if User.objects.filter(username=username).exists():
            user_data_error = True
            messages.error(request , "username already exists")
        if User.objects.filter(email=email).exists():
            user_data_error = True
            messages.error(request , "email already exists")
        if len(password)<8:
            user_data_error = True
            messages.error(request , "password should be longer than 8 characters")
        if password != passwordconfirm:
            user_data_error = True
            messages.error(request , "passwords don't match")

        if not user_data_has_error:
            newuser = User.objects.create(
                    username=username,
                    email=email,
                    password=password,
                    )
            messages.success(request, "account successfully created")
            return redirect('login')
        else:
            return redirect('signup')

    return render(request , "signup/index.html")
