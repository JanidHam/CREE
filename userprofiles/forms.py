from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, Group

class LoginForm(AuthenticationForm):
	username = forms.CharField(max_length=100)
	password = forms.CharField(max_length=100)