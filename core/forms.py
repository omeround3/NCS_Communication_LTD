from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import ModelForm
from core.models import Client

# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class ClientForm(ModelForm):
	class Meta:
		model = Client
		fields = ['first_name', 'last_name', 'email', 'cellphone', 'bandwidth', 'cost']

class NewPasswordResetForm(forms.Form):
	verification_code = forms.CharField(required=True,label='Verification Code')
