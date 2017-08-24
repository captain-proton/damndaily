from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date


class DamnDaily(models.Model):
    name = models.CharField(max_length=512)
    created = models.DateTimeField(default=timezone.now)
    deleted = models.DateTimeField(null=True, blank=True)
    external_id = models.CharField(max_length=24)
    admin_key = models.CharField(max_length=8)

    def __str__(self):
        return '<DamnDaily name={:s}>'.format(self.name)


class Today(models.Model):
    day = models.DateField(null=True, default=date.today)
    time = models.TimeField(null=True, blank=True)
    location = models.CharField(max_length=512)
    damn_daily = models.ForeignKey('DamnDaily', on_delete=models.CASCADE)

    def __str__(self):
        return '<Today daily={0:s}' \
            ' day={1:%d.%m.%Y}' \
            ' time={2:%H:%M}>'.format(str(self.damn_daily.name),
                                      self.day,
                                      self.time)


class Participation(models.Model):
    today = models.ForeignKey('Today', on_delete=models.CASCADE)
    user = models.ForeignKey(User)

    def __str__(self):
        return '<Participation today={:s}' \
            ' user={:s}>'.format(str(self.today), str(self.user))


class Message(models.Model):
    value = models.TextField()
    today = models.OneToOneField('Today',
                                 on_delete=models.CASCADE,
                                 primary_key=True)
    author = models.OneToOneField(User)
