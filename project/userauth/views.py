from django.shortcuts import render
from django.http import request , HttpResponse

# Create your views here.

def login(request):
    return render(request, "login/index.html")


def signup(request):
    return render(request , "signup/index.html")
