from django.shortcuts import render, redirect
from .forms import ContactForm, NewUserForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth import login
from django.contrib import messages #import messages
from django.http import HttpResponse

# Create your views here.
def login(request):
    return HttpResponse("Login Page.")

def homepage(request):
	return render(request, "main/home.html")

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm
	return render (request=request, template_name="main/register.html", context={"register_form":form})