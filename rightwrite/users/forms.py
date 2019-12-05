from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django_registration.forms import RegistrationForm
from django.forms import BaseFormSet, formset_factory
from .models import CustomUser, UserLanguage
from language.models import Language


class BaseUserLanguageFormset(BaseFormSet):
    def clean(self):
        """Adds validation to make sure that at least one native language and one foreign language was included and that
        there are no duplicates"""
        if any(self.errors):
            return

        languages = []
        proficiencies = []
        language_duplicates = False

        for form in self.forms:
            if form.cleaned_data:
                print(form.cleaned_data)
                if form.cleaned_data['language'] in languages:
                    language_duplicates = True
                languages.append(form.cleaned_data['language'])

                proficiencies.append(form.cleaned_data['proficiency'])

        if language_duplicates:
            raise forms.ValidationError(
                'You may not list the same language twice.',
                code='duplicate_languages'
            )

        if not 'NA' in proficiencies:
            raise forms.ValidationError(
                'You must choose at least one native language.',
                code='no_native_language'
            )

        if len(languages) < 2:
            raise forms.ValidationError(
                'You must enter at least one language that you are learning.',
                code='no_foreign_language'
            )


class CustomUserCreationForm(UserCreationForm):

    class Meta(RegistrationForm.Meta):
        model = CustomUser
        fields = ('username', 'email')


# class BaseUserCreationFormset(BaseFormSet):
#     def get_form_kwargs(self, index):
#         kwargs = super().get_form_kwargs(index)
#         kwargs['user'] = self.request.user
#         return kwargs


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

    # def save(self, commit=True):
    #     form = super(CustomUserLanguageForm, self).save(commit=False)
    #     form.user = self.user
    #     if commit:
    #         form.save()
    #     return form


class CustomUserLanguageForm(forms.ModelForm):

    class Meta:
        model = UserLanguage
        fields = ('language', 'proficiency')


    # def __init__(self, *args, **kwargs):
    #     self.request = kwargs.pop('request')
    #     self.user = self.request.user
    #     super(CustomUserLanguageForm, self).__init__(**kwargs)
    #
    def test(self):
        print(self.cleaned_data)

    def save(self, commit=True):
        form = super(CustomUserLanguageForm, self).save(commit=False)
        form.user = self.user
        if commit:
            form.save()
        return form

