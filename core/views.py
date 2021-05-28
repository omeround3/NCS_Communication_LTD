from django.shortcuts import render, redirect
from .forms import ContactForm, NewUserForm, ClientForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.http import HttpResponse
from .utils import MyPasswordChangeForm
from .models import Client

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
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                # Redirect to homepage
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="main/login.html", context={"login_form": form})

# Logout view
def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('/')

# Registiration views
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
            login(request, user)
            messages.success(
                request, "Registration successful, You are now logged in")
            # Redirect to homepage
            return redirect('/')
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm
    return render(request=request, template_name="main/register.html", context={"register_form": form})

# Change password view
def change_password(request):
    if request.method == 'POST':
        form = MyPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = MyPasswordChangeForm(request.user)
    return render(request, 'main/changepassword.html', {'form': form})

# Wrapper function to check user authentication
def check_user_authentication(request, path):
    if request.user.is_authenticated:
        return render(request, 'main/{0}'.format(path))
    else:
        return render(request, 'main/401.html')


def dashboard_request(request):
    if request.user.is_authenticated:
        clients = Client.objects.all()
        return render(request, 'main/dashboard.html', {'clients': clients})
    else:
        return render(request, 'main/401.html')
    # return check_user_authentication(request, 'dashboard.html')


def clients_request(request):
    if request.user.is_authenticated:
        clients = Client.objects.all()
        if request.method == "POST":
            # Create a form instance with the submitted data
            form = ClientForm(request.POST)
            # Validate the form
            if form.is_valid():
                # If the form is valid, get the user credenetials
                form.save()
                messages.success(request, f"You have successfully added a new client.")
                # Redirect to clients page
                return render(request=request, template_name="main/clients.html", context={"client_form": form, 'clients': clients})
            else:
                messages.error(request, "Error creating a new client.")
        form = ClientForm
        return render(request=request, template_name="main/clients.html", context={"client_form": form, 'clients': clients})
    else:
        return render(request, 'main/401.html')
    # return check_user_authentication(request, 'clients.html')

