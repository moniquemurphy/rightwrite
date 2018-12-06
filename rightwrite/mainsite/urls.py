from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import PostView


urlpatterns = [
    path('', PostView.as_view(), name='new_post'),
]