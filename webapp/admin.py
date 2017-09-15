from django.contrib import admin
from .models import DamnDaily, Today, Participation, Message, GeneratedUsername

# Register your models here.
admin.site.register(DamnDaily)
admin.site.register(Today)
admin.site.register(Participation)
admin.site.register(Message)
admin.site.register(GeneratedUsername)
