from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.contrib.auth.models	import User
from django.core.paginator import Paginator
from django.views.generic import (
									ListView,
									DetailView,
									CreateView,
									UpdateView,
									DeleteView
								)
from .models import Post
import whois
import platform


def home(request):
	info = {}
	platform_details = platform.platform()
	system_name = platform.system()
	processor_name = platform.processor()
	architecture_details = platform.architecture()

	info = platform_details
	info2 = system_name
	info3 = processor_name
	info4 = architecture_details

	# print(info)



	context = {
		'posts': Post.objects.all(),
		'info': info,
		'info2': info2,
		'info3': info3,
		'info4': info4,
	}
	return render(request, 'blog/home.html', context)

def domain_info(request, *args, **kwargs):
	text = request.GET.get('domain')
	print(text)
	info = whois.whois(str(text))
	# print(info)
	context = {
		'info': info,
	}
	return render(request, 'blog/domain.html', context)