from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django_registration.forms import RegistrationForm
from django.forms import BaseFormSet, formset_factory, inlineformset_factory
from .models import CustomUser, UserLanguage
from language.models import Language

# https://gist.github.com/freakboy3742/41f0cb287e65617930e4e9686b01e81a


class CustomUserLanguageForm(forms.ModelForm):

    class Meta:
        model = UserLanguage
        fields = ('language', 'proficiency')

    def save(self, commit=True):
        form = super(CustomUserLanguageForm, self).save(commit=False)
        form.user = self.user
        if commit:
            form.save()
        return form


BaseUserLanguageFormset = inlineformset_factory(
                        parent_model=CustomUser,
                        model=UserLanguage,
                        form=CustomUserLanguageForm,
                        extra=2,
                        can_delete=False,
                        fk_name='user')

class UserLanguageFormset(BaseUserLanguageFormset): # this will inherit from model formset factory
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

        if 'NA' not in proficiencies:
            raise forms.ValidationError(
                'You must choose \'Native Speaker\' for at least one language.',
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
