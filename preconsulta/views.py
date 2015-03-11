from django.shortcuts import render, render_to_response, RequestContext, redirect

# Create your views here.
def login(request):
	return render_to_response('preconsulta/index.html', context_instance=RequestContext(request))