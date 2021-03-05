from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser
from django.forms import ModelForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
	class Meta:
		models = CustomUser
		fields = "__all__"