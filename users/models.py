from django.db import models
import unicodedata

from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)
from django.contrib.auth.hashers import (
    UNUSABLE_PASSWORD_PREFIX, identify_hasher,
)
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ValidationError
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.text import capfirst
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.conf import settings

user = settings.AUTH_USER_MODEL



class CustomUser(AbstractUser):
	phone_number = models.CharField(max_length=13, help_text='Please enter your Region code (+91, +1, +92)')


class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile.pics')
	# ip_address = models.GenericIPAddressField(disabled = True)

	def __str__(self):
		return f'{self.user.username} Profile'
	
	# def save(self, *args, **kwargs):
	# 	super(Profile, self).save(*args, **kwargs)

	# 	img = Image.open(self.image.path)

	# 	if img.height > 300 or img.width > 300:
	# 		output_size = (300, 300)
	# 		img.thumbnail(output_size)
	# 		img.save(self.image.path)	


