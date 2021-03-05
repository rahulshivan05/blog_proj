from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from codes.forms import CodeForm
from django.contrib.auth.views import redirect_to_login, logout_then_login

from django.contrib.auth.decorators import login_required
from users.models import CustomUser
from django.contrib.auth import get_user_model
from django.core.mail import send_mail, EmailMessage, BadHeaderError

from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode 
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.conf import settings

from django.contrib import messages
from django.contrib.auth.backends import ModelBackend
import threading
import httpagentparser
import platform
import qrcode
from codes.models import Code
from .forms import CustomUserCreationForm

class EmailThread(threading.Thread):

	def __init__(self, email):
		self.email=email
		threading.Thread.__init__(self)

	def run(self):
		self.email.send()


User = get_user_model()
user = settings.AUTH_USER_MODEL





@login_required
def home_view(request):
	ip = request.META.get('REMOTE_ADDR')
	return render(request, 'users/home.html', {'ip': ip})


def auth_view(request):
	form = AuthenticationForm()
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			request.session['pk'] = user.pk
			request.session['email'] = user.email
			# login(request, user)
			return redirect('verify-view')


	return render(request, 'users/auth.html', {'form': form})



def verify_view(request):
	form = CodeForm(request.POST or None)
	pk = request.session.get('pk')	
	email = request.session.get('email')
	qr_code = Code.objects.get(pk=pk)
	# print(qr_code)

	agent = request.environ.get('HTTP_USER_AGENT')
	browser = httpagentparser.detect(agent)
	os = platform.system()

	if not browser:
		browser = agent.split('/')[0]
	else:
		browser = browser['browser']['name']



	if pk:
		user = CustomUser.objects.get(pk=pk)		
		code = user.code
		code_user = f'{user.username}: {user.code}'
		if not request.POST:
			# sending SMS or sending Email
			print(code_user)
			domain = get_current_site(request).domain			
			# send_sms(code_user, user.phone_number)			

			email_subject = 'Enter the Verification Code for Login in to '+domain

			# link = code
			email_body = 'Hi '+user.username+' Your Verification Code is.\n'+str(code)+ ' \n Your Device: '+browser+' in '+os
			email_from = 'noreplay@noreplay.domain.com'
			receipient_email = [email]


			email = EmailMessage(
			    email_subject,
			    email_body,
			    'noreplay@noreplay.domain.com',
				[email],
			)

			# email.send()

			# send_mail(email_subject, email_body, email_from, receipient_email)

			# EmailThread(email).start()


		if form.is_valid():
			num = form.cleaned_data.get('number')

			if str(code) == num:
				code.save()
				login(request, user)
				return redirect('home-view')
			else:
				return redirect('verify-view')
				

	return render(request, 'users/verify.html', {'form': form, 'qr_code': qr_code})	


def register(request):
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}!. Now you are able to login.')
			return redirect('login-view')

	else:
		form = CustomUserCreationForm()
	return render(request, 'users/registration.html', {'form': form})	


def map_time(request):
	token = 'pk.eyJ1IjoicmFodWxzaGl2YW4wNSIsImEiOiJja2wxeWFrdzYwN3UwMnZ0aDB0Z2h4Y3FqIn0._w_aiMXrl-ts_HpTqjCNCw'
	return render(request, 'users/map.html', {'token': token})



