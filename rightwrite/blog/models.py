from django.conf import settings
from django.db import models
from django.utils import timezone
from language.models import Language

class Entry(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    language = models.ForeignKey('Language', on_delete=models.CASCADE, related_name='entries')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class EntrySentence(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    position_index_1 = models.IntegerField()
    position_index_2 = models.IntegerField()

    def sentence(self):
        return self.entry.text[position_index_1:position_index_2]

    # entry[0] gives you the first sentence?
    # in view, can get QuerySet of EntrySentences and order by position_index?