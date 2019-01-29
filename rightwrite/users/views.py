from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin
from django.forms import formset_factory
from .forms import CustomUserCreationForm, CustomUserLanguageForm


class UserSignupView(TemplateView):
    template_name = 'registration/signup.html'

    def get_context_data(self, **kwargs):
        context = super(UserSignupView, self).get_context_data(**kwargs)

        context['user_signup_form'] = CustomUserCreationForm(prefix='user_signup')

        CustomUserLanguageFormset = formset_factory(CustomUserLanguageForm, extra=2)
        context['user_language_formset'] = CustomUserLanguageFormset(prefix='user_language')

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        if context['user_signup_form'].is_valid() and context['user_language_formset'].is_valid():
            context['user_signup_form'].save()
            context['user_language_formset'].save()
        else:
            messages.error(self.request, 'Error encountered: Please see below')

        return self.render_to_response(context)