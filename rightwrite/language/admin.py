from django.contrib import admin
from .models import Language


class CustomLanguageAdmin(admin.ModelAdmin):
    list_display = ['language']


admin.site.register(Language, CustomLanguageAdmin)


