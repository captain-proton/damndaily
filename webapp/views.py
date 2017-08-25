from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import date
from .models import DamnDaily, Today, Participation, Message
from . import services


# Create your views here.
def index(request):
    return HttpResponse('hello damn daily')


def create(request):
    return render(request, 'webapp/create.html')


def save_damn_daily(request):
    daily = DamnDaily(name=request.POST['name'],
                      external_id=services.create_damndaily_id(),
                      admin_key=services.random_string(8))
    daily.save()
    return HttpResponseRedirect(reverse('webapp:view',
                                        args=(daily.external_id,)))


def view(request, damndailyid):
    damndaily = get_object_or_404(DamnDaily, external_id=damndailyid)

    participations = Participation.objects \
        .filter(today__day=date.today()) \
        .filter(today__damndaily__external_id=damndailyid)

    try:
        today = Today.objects \
            .filter(damndaily__external_id=damndailyid) \
            .get(day=date.today())
    except Today.DoesNotExist:
        today = Today(day=date.today(), damndaily=damndaily)
        today.save()

    messages = Message.objects.filter(today=today)

    context = {
        'participations': participations,
        'damndaily': damndaily,
        'today': today,
        'messages': messages
    }
    return render(request, 'webapp/index.html', context)


def update_today(request, todayid):
    today = get_object_or_404(Today, pk=todayid)
    today.time = request.POST['time']
    today.location = request.POST['location']
    today.save()
    return HttpResponseRedirect(reverse('webapp:view',
                                        args=(today.damndaily.external_id,)))


def partake(request, damndailyid):
    return HttpResponse('partake damn daily id: %s' % (damndailyid,))
