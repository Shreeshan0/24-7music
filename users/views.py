from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import login as auth_login , logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
       
        if user is not None:
            auth_login(request,user)
            return redirect('/')
        else:
            messages.error(request, 'Username or password is incorrect')
    context = {}
    return render(request,'users/login.html',context)

def logoutUser(request):
    logout(request)
    
    return redirect('/')

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f"Account has been created for {username}")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/signup.html',{'form':form})




   
