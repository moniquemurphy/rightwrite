from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('users/', include('django_registration.backends.activation.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('blog/', include('blog.urls')),
    path('friendship/', include('friendship.urls')),
]