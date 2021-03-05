from django.contrib import admin
from django.urls import path, include
from users.views import home_view, auth_view, verify_view, register, map_time
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

User = settings.AUTH_USER_MODEL





urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('url/', include('urlshortner.urls', namespace='urlshortner')),
    path('', home_view, name='home-view'),
    path('tracking/', include('tracking.urls')),
	path('login', auth_view, name='login-view'),
	path('verify', verify_view, name='verify-view'),
    path('register', register, name='register-view'),

    # path('accounts/', include('allauth.urls')),
    # path('', TemplateView.as_view(template_name='blog/index.html')),

    path('map', map_time, name='map-view'),
    # path('verification/', include('verify_email.urls')),
	path('logout', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
