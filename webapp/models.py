from django.db import models
from django.contrib.auth.models import User


class DamnDaily(models.Model):
    name = models.CharField(max_length=512)
    created = models.DateTimeField()
    deleted = models.DateTimeField(null=True)
    external_id = models.CharField(max_length=24)


class Today(models.Model):
    at = models.DateTimeField(null=True)
    location = models.CharField(max_length=512)
    damn_daily = models.OneToOneField('DamnDaily', on_delete=models.CASCADE)


class Participation(models.Model):
    today = models.ForeignKey('Today', on_delete=models.CASCADE)
    user = models.ForeignKey(User)


class Message(models.Model):
    value = models.TextField()
    today = models.OneToOneField('Today',
                                 on_delete=models.CASCADE,
                                 primary_key=True)
    author = models.OneToOneField(User)
