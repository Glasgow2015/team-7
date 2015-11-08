from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from pcs.forms import VolunteerRegistrationForm, StoryForm
from pcs.models import Volunteer, Story
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

@csrf_exempt
@login_required
def add_story(request):
    if request.method == 'POST':
        form = StoryForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit = False)
            f.user = request.user
            f.save()
        else:
            print form.errors
    else:
        form = StoryForm()

    stories = []
    user_scores = Story.objects.filter(user = request.user)
    for story in user_scores:
        dict = {"caption" :story.caption, "description":story.description, "picture":story.image}
        stories += [dict]
    print stories
    return render(request, 'pcs/add_story.html', {'form': form , 'stories':stories})





