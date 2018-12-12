from django.db import models
from django.conf import settings
from django.utils import timezone
from blog.models import Entry, EntrySentence


# These seem like two separate entities now, since CorrectedSentence points to a particular EntrySentence, but still
# want Correction to store user who corrected and date

class Correction(models.Model):
    original_entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    user_who_corrected = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.user_who_corrected) + ' ' + str(self.created_date)


class CorrectedSentence(models.Model):
    original_sentence = models.ForeignKey(EntrySentence, on_delete=models.CASCADE)
    corrected_sentence = models.TextField()
