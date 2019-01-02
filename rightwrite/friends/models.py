from django.db import models
from users.models import CustomUser

# Create your models here.
class Friend(models.Model):
    base_user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='friend_self')
    friend = models.ForeignKey('User', on_delete=models.CASCADE, related_name='friend_friend')
