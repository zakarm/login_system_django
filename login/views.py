from django.shortcuts import render
from django.http import HttpResponse
from .models import SignIn
from django.utils.dateparse import parse_datetime
from django.contrib.auth.decorators import login_required
import os
import datetime

# Create your views here.

def sign_in(request) :
    if request.method == "POST" :
        email = request.POST["email"]
        password = request.POST["email"]
        data = SignIn.objects.filter(email=email, password=password)
    return render(request, "login/sign_in.html")
    #return render(request, "")

def sign_up(request) :
    if (request.method == "POST"):
        fullname = request.POST["fullname"]
        city = request.POST["city"]
        age = request.POST["age"]
        email = request.POST["email"]
        password = request.POST["email"]
    return render(request, "login/sign_up.html")
