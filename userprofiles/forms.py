# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, Group

class LoginForm(AuthenticationForm):
	username = forms.CharField(max_length=100)
	password = forms.CharField(max_length=100)

	error_messages = {
		'invalid_login': ("Por favor introduce un nombre de usuario o contraseña correcto. "
							"Nota que ambos campos pueden ser con mayúsculas y minúsculas. "),
		'inactive': ("Esta cuenta esta inactiva."),
	}