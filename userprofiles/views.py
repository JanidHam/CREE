from django.shortcuts import render, render_to_response, RequestContext, redirect
from django.contrib.auth import login, logout
from .forms import LoginForm
from django.views.generic import FormView
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
class Login(FormView):
	template_name = 'userprofiles/login.html'
	success_url = '/preconsulta/'
	form_class = LoginForm

	def form_valid(self, form):
		login(self.request, form.user_cache)
		return super(Login, self).form_valid(form)

# Logout -----------------------------------------------------------------------------------------------------
def logout_view(request):
	logout(request)
	return redirect('/login/')

#def login(request):
#	return render_to_response('userprofiles/login.html', context_instance=RequestContext(request))