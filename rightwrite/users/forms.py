from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'lang_1', 'lang_1_proficiency', 'lang_2', 'lang_2_proficiency', 'lang_3',
                  'lang_3_proficiency')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'lang_1', 'lang_1_proficiency', 'lang_2', 'lang_2_proficiency', 'lang_3',
                  'lang_3_proficiency')