from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import EntryView


urlpatterns = [
    path('', EntryView.as_view(), name='new_post'),
]