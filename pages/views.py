
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
    return render(request, 'Landingpage.html')

def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def faq(request):
    return render(request, 'FAQ.html')

