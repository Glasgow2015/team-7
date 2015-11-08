from django.shortcuts import render
from pcs.forms import VolunteerRegistrationForm

def index(request):
	context_dict = {'boldmessage': "Bold Font"}
	return render(request, 'pcs/index.html', context_dict)

def support(request):
	context_dict = {'boldmessage': "Bold Font"}
	return render(request, 'pcs/support.html', context_dict)

def statistics(request):
	context_dict = {'boldmessage': "Bold Font"}
	return render(request, 'pcs/statistics.html', context_dict)

def symptoms(request):
	context_dict = {'boldmessage': "Bold Font"}
	return render(request, 'pcs/symptoms.html', context_dict)

def getinvolved(request):
	context_dict = {'boldmessage': "Bold Font"}
	return render(request, 'pcs/getinvolved.html', context_dict)

def sharedstories(request):
	context_dict = {'boldmessage': "Bold Font"}
	return render(request, 'pcs/sharedstories.html', context_dict)

def login(request):
	context_dict = {'boldmessage': "Bold Font"}
	return render(request, 'pcs/login.html', context_dict)

def about(request):
	context_dict = {'boldmessage': "Bold Font"}
	return render(request, 'pcs/about.html', context_dict)

def volunteer_registration(request):
	if request.method == 'POST':
		form = VolunteerRegistrationForm(request.POST)

		if form.is_valid():
			form.save(commit = True)
			return index(request)
		else:
			print form.errors
	else:
		form = VolunteerRegistrationForm()

	return render(request, 'pcs/volunteer_registration.html', {'form':form})




