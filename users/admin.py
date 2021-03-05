from django.contrib import admin
from .models import CustomUser, Profile
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
	model = CustomUser
	add_form = CustomUserCreationForm

	fieldsets = (
		*UserAdmin.fieldsets,
		(
			'User role',
			{
				'fields': (
					'phone_number',
				)
			}
		)
	)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)



