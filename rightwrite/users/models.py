from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    FRENCH = 'FR'
    ENGLISH = 'EN'
    JAPANESE = 'JA'

    LANGUAGE_CHOICES = (
        (FRENCH, 'French'),
        (ENGLISH, 'English'),
        (JAPANESE, 'Japanese'),
    )

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

    lang_1 = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)
    lang_1_proficiency = models.CharField(max_length=2, choices=PROFICIENCY_CHOICES)
    lang_2 = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, null=True, blank=True)
    lang_2_proficiency = models.CharField(max_length=2, choices=PROFICIENCY_CHOICES, null=True, blank=True)
    lang_3 = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, null=True, blank=True)
    lang_3_proficiency = models.CharField(max_length=2, choices=PROFICIENCY_CHOICES, null=True, blank=True)
    num_entries_corrected = models.IntegerField(default=0, blank=True)
    points = models.IntegerField(default=0, blank=True)


    def __str__(self):
        return self.email