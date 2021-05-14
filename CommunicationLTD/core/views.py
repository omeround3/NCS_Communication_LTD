from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Welcome to Communication LTD Website.")

def login(request):
    return HttpResponse("Login Page.")