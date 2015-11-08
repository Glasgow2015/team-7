from django.shortcuts import render
from pcs.forms import VolunteerRegistrationForm
from pcs.models import Volunteer
import json
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

def donate(request):
	context_dict = {'boldmessage': "Bold Font"}
	return render(request, 'pcs/donate.html', context_dict)

def map(request):
	post_codes = []

	for volunteer in Volunteer.objects.filter():
		print volunteer.postcode
		post_codes += [volunteer.postcode.decode("utf-8")]

	print post_codes
	json_post_codes = json.dumps(post_codes)

	return render(request, 'pcs/map.html', {"post_codes" :json_post_codes })

def volunteer_registration(request):
	post_codes = []

	for volunteer in Volunteer.objects.filter():
		print volunteer.postcode
		post_codes += [volunteer.postcode.decode("utf-8")]

	json_post_codes = json.dumps(post_codes)

	if request.method == 'POST':
		form = VolunteerRegistrationForm(request.POST)

		if form.is_valid():
			form.save(commit = True)
			return index(request)
		else:
			print form.errors
	else:
		form = VolunteerRegistrationForm()

	return render(request, 'pcs/volunteer_registration.html', {'form':form, "post_codes":json_post_codes})




