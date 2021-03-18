from django.shortcuts import render
from . models import Dota
from django.http import HttpResponse

def index(request):
	return HttpResponse('Hello')
