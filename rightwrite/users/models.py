from django.contrib.auth.models import AbstractUser
from django.db import models
from language.models import Language


class CustomUser(AbstractUser):

    num_entries_corrected = models.IntegerField(default=0, blank=True)
    points = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.email


class UserLanguage(models.Model):

    NATIVE = 'NA'
    BEGINNER = 'BG'
    INTERMEDIATE = 'IN'
    ADVANCED = 'AD'

    PROFICIENCY_CHOICES = (
        (NATIVE, 'Native Speaker'),
        (BEGINNER, 'Beginner'),
        (INTERMEDIATE, 'Intermediate'),
        (ADVANCED, 'Advanced'),
    )

    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='user_language')
    proficiency = models.CharField(max_length=2, choices=PROFICIENCY_CHOICES)