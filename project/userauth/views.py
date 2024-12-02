from django.shortcuts import render , redirect
from django.http import request , HttpResponse
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect


#login functionality & view

def loginview(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        if username and password:
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Please fill in all fields")
        
        return redirect('login')
        
    return render(request, "login/index.html")

#signup functionality & view
def signupview(request):    
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        passwordconfirm = request.POST.get("passwordconfirm")
        user_data_error = False

        if User.objects.filter(email=email).exists() or User.objects.filter(username=username).exists():
            user_data_error = True
            messages.error(request , "email or username already exists")
        if len(password)<8:
            user_data_error = True
            messages.error(request , "password should be longer than 8 characters")
        if password != passwordconfirm:
            user_data_error = True
            messages.error(request , "passwords don't match")

        if not user_data_error:
            newuser = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    )
            messages.success(request, "account successfully created")
            return redirect('login')
        else:
            return redirect('signup')

    elif request.method == "GET":
        return render(request, "signup/index.html")


#signing out view
def signoutview(request):
    logout(request)
    return redirect('login')








