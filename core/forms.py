from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import ModelForm
from django.core.exceptions import ValidationError
from core.models import Client

# Create your forms here.


class ContactForm(forms.Form):
	first_name = forms.CharField(max_length = 50)
	last_name = forms.CharField(max_length = 50)
	email_address = forms.EmailField(max_length = 150)
	message = forms.CharField(widget = forms.Textarea, max_length = 2000)
    
class NewUserForm(UserCreationForm):
	# email = forms.EmailField(required=True)
	email = forms.CharField(required=True)


	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		print("Im here")
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

	# Uncomment to protect against register SQLI
	def clean(self):
		email = self.cleaned_data.get('email')
		if User.objects.filter(email=email).exists():
			raise ValidationError("Email exists")
		return self.cleaned_data
	

class ClientForm(ModelForm):
	class Meta:
		model = Client
		fields = ['first_name', 'last_name', 'email', 'cellphone', 'bandwidth', 'cost']

class ClientSearchForm(forms.Form):
	search_str = forms.CharField(label='search user')

class NewPasswordResetForm(forms.Form):
	verification_code = forms.CharField(label='verification code')
