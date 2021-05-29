from django.db import connection
from django.shortcuts import render, redirect
<<<<<<< HEAD
from .forms import ClientSearchForm, ContactForm, NewUserForm, ClientForm, NewPasswordResetForm
=======
from .forms import NewUserForm, ClientForm, NewPasswordResetForm
>>>>>>> 86219a6656630ec6481dfcda95fcf4fe824dd1fa
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm
<<<<<<< HEAD
from django.http import HttpResponse, HttpResponseRedirect
=======
from django.http import HttpResponse,HttpResponseRedirect, HttpResponseNotFound
>>>>>>> 86219a6656630ec6481dfcda95fcf4fe824dd1fa
from .utils import *
from .models import Client
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

# Create your views here.

# Index view


def index(request):
    return render(request, "main/index.html")

# Login view


def login_request(request):
    # The request method 'POST' indicates
    # that the form was submitted
    if request.method == "POST":
        # Create a form instance with the submitted data
        form = AuthenticationForm(request, data=request.POST)
        # Validate the form
        if form.is_valid():
            # If the form is valid, get the user credenetials
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # Authentication of the user
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user,
                      backend='django.contrib.auth.backends.ModelBackend')
                messages.info(request, f"You are now logged in as {username}.")
                # Redirect to homepage
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
            return HttpResponseRedirect("/login")
    form = AuthenticationForm()
    return render(request=request, template_name="main/login.html", context={"login_form": form})

# Logout view


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('/')

# # Registiration view
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
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(
                request, "Registration successful, You are now logged in")
            # Redirect to homepage
            return redirect('/')
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
        return HttpResponseRedirect("/register")
    form = NewUserForm
    return render(request=request, template_name="main/register.html", context={"register_form": form})


# Change password view
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'main/changepassword.html', {'form': form})

<<<<<<< HEAD
# Wrapper function to check user authentication


def check_user_authentication(request, path):
    if request.user.is_authenticated:
        return render(request, 'main/{0}'.format(path))
    else:
        return render(request, 'main/401.html')

=======
>>>>>>> 86219a6656630ec6481dfcda95fcf4fe824dd1fa

def dashboard_request(request):
    if request.user.is_authenticated:
        clients = Client.objects.all()
        search_form = ClientSearchForm(request.POST)
        if search_form.is_valid():
            print("Valid")
            user = search_form.cleaned_data['search_str']
            clients = Client.objects.all().filter(first_name=user)
        return render(request, 'main/dashboard.html', {'search_form':search_form,'clients': clients})
    else:
        return render(request, '401.html')


def clients_request(request):
    if request.user.is_authenticated:
        clients = Client.objects.all()
        if request.method == 'POST':
            # Create a form instance with the submitted data
            search_form = ClientSearchForm(request.POST)
            form = ClientForm(request.POST)
            print(search_form)
            # Validate the form
            if form.is_valid():
                # If the form is valid, get the user credenetials
                form.save()
                messages.success(
                    request, f"You have successfully added a new client.")
                # Redirect to clients page
                return render(request=request, template_name="main/clients.html", context={"search_form":search_form,"client_form": form, 'clients': clients})
            else:
                messages.error(request, "Error creating a new client.")
        form = ClientForm
        search_form = ClientSearchForm()
        return render(request=request, template_name="main/clients.html", context={"search_form":search_form,"client_form": form, 'clients': clients})
    else:
        return render(request, '401.html')


def dread_request(request):
    if request.user.is_authenticated:
        return render(request=request, template_name='main/dread.html')
    else:
        return render(request, '401.html')

# Password reset Main page


def password_reset_request(request):
<<<<<<< HEAD
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "main/password/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    request.session['token'] = c["token"]
                    request.session['uid'] = c["uid"]
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'CommunicationLTD@example.com',
                                  [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/reset_done")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="main/password/password_reset.html", context={"password_reset_form": password_reset_form})
=======
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "main/password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					request.session['token'] = c["token"]
					request.session['uid'] = c["uid"]
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'CommunicationLTD@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ('/reset_done')
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name='main/password/password_reset.html', context={'password_reset_form':password_reset_form})
>>>>>>> 86219a6656630ec6481dfcda95fcf4fe824dd1fa

# Password validate verification code


def password_reset_done(request):
    # The request method 'POST' indicates
    # that the form was submitted
    if request.method == "POST":
        # Create a form instance with the submitted data
        form = NewPasswordResetForm(request.POST)
        # Validate the form
        if form.is_valid():
            user_token = form.cleaned_data['verification_code']
            token = request.session['token']
            uid = request.session['uid']
            # Check user token
<<<<<<< HEAD
            if token == user_token:
                return redirect('password_reset_confirm', uidb64=uid, token=token)
            else:
                return redirect("/password_reset")
    form = NewPasswordResetForm()
    return render(request=request, template_name="main/password/password_reset_done.html", context={"form": form})
=======
			if token == user_token:
				return redirect ('password_reset_confirm',uidb64 = uid, token = token)
			else:
				return redirect('/password_reset')
	form = NewPasswordResetForm()
	return render(request=request, template_name='main/password/password_reset_done.html', context={'form':form})


>>>>>>> 86219a6656630ec6481dfcda95fcf4fe824dd1fa
