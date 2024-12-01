from django.http import request
from django.shortcuts import redirect


def mainview(request):
    return redirect('home')
