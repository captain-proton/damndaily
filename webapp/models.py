from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class DamnDaily(models.Model):
    name = models.CharField(max_length=512)
    created = models.DateTimeField(default=datetime.today())
    deleted = models.DateTimeField(null=True, blank=True)
    external_id = models.CharField(max_length=24)

    def __str__(self):
        return '<DamnDaily name={:s}' \
            ' created={:%d.%m.%Y %H:%M}>'.format(self.name, self.created)


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
