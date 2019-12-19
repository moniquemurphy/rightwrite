from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from .forms import CustomUserCreationForm, UserLanguageFormset


class UserSignupView(TemplateView):
    template_name = 'registration/signup.html'

    def get_context_data(self, **kwargs):
        context = super(UserSignupView, self).get_context_data(**kwargs)

        if 'request' in kwargs:
            data = kwargs['request'].POST
            context['user_signup_form'] = CustomUserCreationForm(prefix='user_signup', data=data)
            context['user_language_formset'] = UserLanguageFormset(prefix='user_language', data=data)
            print(data)
        else:
            context['user_signup_form'] = CustomUserCreationForm(prefix='user_signup')
            user = context['user_signup_form'].instance
            context['user_language_formset'] = UserLanguageFormset(prefix='user_language')

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(request=request, **kwargs)

        post_data = request.POST or None

        if context['user_signup_form'].is_valid() and context['user_language_formset'].is_valid():
            context['user_signup_form'].save()
            for form in context['user_language_formset']:
                form.user = context['user_signup_form'].instance
                form.save()

            return HttpResponseRedirect(reverse('home'))

        return self.render_to_response(context)
