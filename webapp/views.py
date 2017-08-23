from django.shortcuts import render, HttpResponse


# Create your views here.
def view(request, damndailyid):
    return HttpResponse('damn daily id: %s' % damndailyid)
