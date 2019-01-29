from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django_registration.backends.activation.views import RegistrationView
from users.forms import CustomUserCreationForm

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/register/', RegistrationView.as_view(form_class=CustomUserCreationForm),
         name='django_registration_register'),
    path('accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('user_test/', include('users.urls')),
    path('blog/', include('blog.urls')),
    path('friendship/', include('friendship.urls')),
]