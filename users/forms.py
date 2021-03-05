from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.forms import ModelForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = CustomUser
		# fields = "__all__"
		fields = ['username', 'first_name', 'email', 'phone_number']