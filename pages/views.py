
from re import template
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.


class HomePageView(TemplateView):
    template_name = 'pages/Landingpage.html'

class AboutusView(TemplateView):
    template_name = 'pages/about.html'
    

class FaqView(TemplateView):
    template_name = 'pages/FAQ.html'

