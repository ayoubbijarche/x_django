from django.shortcuts import render
from django.http import request
from django.shortcuts import redirect
# Create your views here.

def home(request):
    if not request.user.is_authenticated:
        return redirect("login/")
    else:
        return render(request, "homepage/home.html")
