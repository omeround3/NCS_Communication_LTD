from django.shortcuts import render, redirect
from .forms import ContactForm, NewUserForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth import login
from django.contrib import messages #import messages
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Welcome to Communication LTD Website.")

def login(request):
    return HttpResponse("Login Page.")

def homepage(request):
	return render(request, "main/home.html")

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("main:homepage")
      
	form = ContactForm()
	return render(request, "templates/main/contact.html", {'form':form})

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