from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, 'Landingpage.html')

def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')

def faq(request):
    return render(request, 'FAQ.html')