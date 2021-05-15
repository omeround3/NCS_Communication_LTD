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
	# The request method 'POST' indicates
    # that the form was submitted
	if request.method == "POST":
		# Create a form instance with the submitted data
		form = NewUserForm(request.POST)
		# Validate the form
		if form.is_valid():
			 # If the form is valid, save the user and login
			user = form.save()
			# login(request, user)
			messages.success(request, "Registration successful." )
			# Redirect to homepage
			return redirect('/')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm
	return render (request=request, template_name="main/register.html", context={"register_form":form})