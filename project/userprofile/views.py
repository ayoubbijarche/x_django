from django.shortcuts import render
from django.http import request
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required()
def profileview(request):
    return render(request , "profile/index.html")
