from django.contrib import admin
from .models import Correction, CorrectedSentence

admin.site.register(Correction)
admin.site.register(CorrectedSentence)
