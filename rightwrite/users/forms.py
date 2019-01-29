from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django_registration.forms import RegistrationForm
from .models import CustomUser, UserLanguage
from language.models import Language

class CustomUserCreationForm(RegistrationForm):

    class Meta(RegistrationForm.Meta):
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserLanguageForm(forms.ModelForm):

    class Meta:
        model = UserLanguage
        fields = ('language', 'proficiency')

    # def __init__(self, *args, **kwargs):
    #     self.request = kwargs.pop('request')
    #     self.user = self.request.user
    #     super(CustomUserLanguageForm, self).__init__(**kwargs)
    #
    # def save(self, commit=True):
    #     form = super(CustomUserLanguageForm, self).save(commit=False)
    #     form.user = self.user
    #     if commit:
    #         form.save()
    #     return form
