
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

def hello_world(request):
	return HttpResponse("Hello world")
