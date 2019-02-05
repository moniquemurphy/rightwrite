from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin
from django.forms import formset_factory
from .forms import CustomUserCreationForm, CustomUserLanguageForm


class UserSignupView(TemplateView):
    template_name = 'registration/signup.html'

    part_one_form = CustomUserCreationForm(prefix='user_signup')
    formset_fun_times = CustomUserLanguageFormset = formset_factory(CustomUserLanguageForm, extra=2)


    def get_context_data(self, **kwargs):
        context = super(UserSignupView, self).get_context_data(**kwargs)

        context['user_signup_form'] = self.part_one_form
        context['user_language_formset'] = self.formset_fun_times

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(request=request, **kwargs)

        post_data = request.POST or None

        print(post_data)

        if self.part_one_form.is_valid():
            print('is valid')
        else:
            print('is not valid')
            print(context['user_signup_form'].errors)

        # for form in self.formset_fun_times:
        #     if form.is_valid():
        #         print('at least one form of the second part is valid')
        #     else:
        #         print('not valid: ')
        #         for key, value in form.errors:
        #             print(key, value)
        #     messages.error(self.request, 'Error encountered: Please see below')

        return self.render_to_response(context)