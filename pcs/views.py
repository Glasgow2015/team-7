from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Index")

def support(request):
	return HttpResponse("Support")

def statistics(request):
	return HttpResponse("Statistics")

def symptoms(request):
	return HttpResponse("Symptoms")

def getinvolved(request):
	return HttpResponse("Get Involved")

def sharedstories(request):
	return HttpResponse("Shared Stories")

def login(request):
	return HttpResponse("Login")
