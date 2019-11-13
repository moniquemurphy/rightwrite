from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin
from django.forms import formset_factory
from .forms import CustomUserCreationForm, CustomUserLanguageForm, BaseUserLanguageFormset
from .helpers import *


CustomUserLanguageFormset = formset_factory(CustomUserLanguageForm, formset=BaseUserLanguageFormset, extra=2)

class TestingView(TemplateView):
    template_name = 'mainsite/testing.html'

    # https://whoisnicoleharris.com/2015/01/06/implementing-django-formsets.html

class UserSignupView(TemplateView):
    template_name = 'registration/signup.html'

    def get_context_data(self, **kwargs):
        context = super(UserSignupView, self).get_context_data(**kwargs)

        if 'request' in kwargs:
            data = kwargs['request'].POST
            # context['user_signup_form'] = CustomUserCreationForm(prefix='user_signup', data=data)
            context['user_language_formset'] = CustomUserLanguageFormset(prefix='user_language', data=data)
        else:
            # context['user_signup_form'] = CustomUserCreationForm(prefix='user_signup')
            # user = context['user_signup_form'].instance
            context['user_language_formset'] = CustomUserLanguageFormset(prefix='user_language')

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(request=request, **kwargs)

        post_data = request.POST or None
        print(post_data)

        if context['user_language_formset'].is_valid():
            print("valid formset!")
        # if context['user_signup_form'].is_valid():
        #     print('is valid')
            # this works but i don't want to clutter up the db
            # context['user_signup_form'].save()
        # else:
        #     print('is not valid')
        #     print(context['user_signup_form'].errors)

        # need to check if there are at least two languages included! One must be native language

        return self.render_to_response(context)
