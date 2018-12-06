from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    FRENCH = 'FR'
    ENGLISH = 'EN'
    JAPANESE = 'JA'

    LANGUAGE_CHOICES = (
        (FRENCH, 'French'),
        (ENGLISH, 'English'),
        (JAPANESE, 'Japanese'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Correction(models.Model):
    original_entry = models.ForeignKey('Post', on_delete=models.CASCADE)
    corrected_entry = models.TextField()
    user_who_corrected = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def save_correction(self):
        self.corrected_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.user_who_corrected) + ' ' + str(self.corrected_date)