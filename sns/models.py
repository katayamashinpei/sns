from email.policy import default
from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='message_owner')
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    share_id = models.IntegerField(default=-1)
