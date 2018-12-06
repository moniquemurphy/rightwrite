from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'lang_1', 'lang_1_proficiency', 'lang_2', 'lang_2_proficiency', 'lang_3',
                    'lang_3_proficiency']

admin.site.register(CustomUser, CustomUserAdmin)