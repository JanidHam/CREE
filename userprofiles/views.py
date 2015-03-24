from django.shortcuts import render, render_to_response, RequestContext, redirect
from django.contrib.auth import login, logout
from .forms import LoginForm
from django.views.generic import FormView

# Create your views here.
class Login(FormView):
	#model = UsuarioPromotor
	template_name = 'login.html'
	success_url = '/preconsulta/'
	form_class = LoginForm

	def form_valid(self, form):
		login(self.request, form.user_cache)
		return super(Login, self).form_valid(form)

#def login(request):
#	return render_to_response('userprofiles/login.html', context_instance=RequestContext(request))