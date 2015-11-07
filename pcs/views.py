from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
	context = RequestContext(request)
	context_dict = {'boldmessage': "Bold Font"}
	return render(request, 'pcs/index.html', context_dict)

def support(request):
	context = RequestContext(request)
	context_dict = {'boldmessage': "Bold Font"}
	return render(request, 'pcs/support.html', context_dict)

def statistics(request):
	context = RequestContext(request)
	context_dict = {'boldmessage': "Bold Font"}
	return render(request, 'pcs/statistics.html', context_dict)

def symptoms(request):
	context = RequestContext(request)
	context_dict = {'boldmessage': "Bold Font"}
	return render(request, 'pcs/symptoms.html', context_dict)

def getinvolved(request):
	context = RequestContext(request)
	context_dict = {'boldmessage': "Bold Font"}
	return render(request, 'pcs/getinvolved.html', context_dict)

def sharedstories(request):
	context = RequestContext(request)
	context_dict = {'boldmessage': "Bold Font"}
	return render(request, 'pcs/sharedstories.html', context_dict)

def login(request):
	context = RequestContext(request)
	context_dict = {'boldmessage': "Bold Font"}
	return render(request, 'pcs/login.html', context_dict)

def about(request):
	context = RequestContext(request)
	context_dict = {'boldmessage': "Bold Font"}
	return render(request, 'pcs/about.html', context_dict)