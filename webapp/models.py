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


class Subscription(models.Model):
    start = models.DateTimeField(default=timezone.now)
    end = models.DateTimeField(null=True, blank=True)
    damndaily = models.ForeignKey('DamnDaily', on_delete=models.CASCADE)
    user = models.ForeignKey(User)

    def __str__(self):
        fmt = '<Subscription daily={0:s}  user={1:s}'
        fmt_obj = [self.damndaily.name, self.user.username]
        fmt = ''.join([fmt, '>'])
        return fmt.format(*fmt_obj)


class Today(models.Model):
    day = models.DateField(null=True, default=date.today)
    time = models.TimeField(null=True, blank=True)
    location = models.CharField(max_length=512)
    damndaily = models.ForeignKey('DamnDaily', on_delete=models.CASCADE)

    def __str__(self):
        fmt = '<Today daily={0:s}  day={1:%d.%m.%Y}'
        fmt_obj = [self.damndaily.name, self.day]
        if self.time:
            fmt = ''.join([fmt, ' time={2:%H:%M}'])
            fmt_obj.append(self.time)
        fmt = ''.join([fmt, '>'])
        return fmt.format(*fmt_obj)


class Participation(models.Model):
    today = models.ForeignKey('Today', on_delete=models.CASCADE)
    user = models.ForeignKey(User)

    def __str__(self):
        return '<Participation today={:s}' \
            ' user={:s}>'.format(str(self.today), str(self.user))


class Message(models.Model):
    value = models.TextField()
    send = models.DateTimeField(auto_now_add=True)
    today = models.OneToOneField('Today',
                                 on_delete=models.CASCADE,
                                 primary_key=True)
    author = models.OneToOneField(User)


class GeneratedUsername(models.Model):
    """See https://github.com/mattconsto/fantasy-names for generation
    """
    username = models.CharField(max_length=128, unique=True)
    group = models.CharField(max_length=64)
    individual = models.CharField(max_length=64)
    gender = models.SmallIntegerField()

    def __str__(self):
        fmt = '<GeneratedUsername username={0.username}' \
            ' group={0.group}' \
            ' individual={0.individual}' \
            ' gender={0.gender}'
        return fmt.format(self)
