from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import Http404
from django.shortcuts import redirect

def redirect_view(home):
	@login_required(login_url='/login/')
	def wrapper(request):
		if request.user.is_superuser == True:
			return home(request)
		else:
			try:
				request.user.groups.get(name='Preconsulta')
				"""try:					
					request.user.groups.get(name='Informacion')
				except Group.DoesNotExist:
					raise Http404
				else:
					return home(request)"""
			except Group.DoesNotExist:
				raise Http404
			else:
					return home(request)

	return wrapper

def validViewPermissionRevisionMedica(view):
	@login_required(login_url='/login/')
	def wrapper(request, paciente):
		if request.user.is_superuser == True:
			return view(request, paciente)
		else:
			try:
				request.user.groups.get(name='Preconsulta')
				try:					
					request.user.groups.get(name='RevisionMedica')
				except Group.DoesNotExist:
					raise Http404
				else:
					return view(request, paciente)
			except Group.DoesNotExist:
				raise Http404
			else:
					return view(request, paciente)
	return wrapper

def validViewPermissionRevisionPsicologica(view):
	@login_required(login_url='/login/')
	def wrapper(request, paciente):
		if request.user.is_superuser == True:
			return view(request, paciente)
		else:
			try:
				request.user.groups.get(name='Preconsulta')
				try:					
					request.user.groups.get(name='RevisionPsicologica')
				except Group.DoesNotExist:
					raise Http404
				else:
					return view(request, paciente)
			except Group.DoesNotExist:
				raise Http404
			else:
					return view(request, paciente)
	return wrapper

def validViewPermissionTrabajoSocial(view):
	@login_required(login_url='/login/')
	def wrapper(request, paciente):
		if request.user.is_superuser == True:
			return view(request, paciente)
		else:
			try:
				request.user.groups.get(name='Preconsulta')
				try:					
					request.user.groups.get(name='TrabajoSocial')
				except Group.DoesNotExist:
					raise Http404
				else:
					return view(request, paciente)
			except Group.DoesNotExist:
				raise Http404
			else:
					return view(request, paciente)
	return wrapper