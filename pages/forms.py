# from logging import PlaceHolder
# from unicodedata import name
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from django import forms
# from django.forms import ModelForm

# class CreateUserForm(UserCreationForm):

#     #adding placeholder in form method1
#     username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Yourname"}))
#     email = forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Email"}))
#     password1 = forms.CharField(widget=forms.TextInput(attrs={"class":"input", "placeholder":"Password", "type": "password"}))
#     password2 = forms.CharField(widget=forms.TextInput(attrs={"class":"input", "placeholder":"Re:Password","type": "password"}))

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
