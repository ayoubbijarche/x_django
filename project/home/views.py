from django.shortcuts import render
from django.http import request
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    return render(request, "homepage/index.html" , {"username" : User.username})
