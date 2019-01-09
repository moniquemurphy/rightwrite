from django.contrib import admin
from .models import Entry, EntrySentence

# Register your models here.
admin.site.register(Entry)
admin.site.register(EntrySentence)
