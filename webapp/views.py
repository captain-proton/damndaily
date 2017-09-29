from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views import generic
from datetime import date
from .models import DamnDaily, Today, Participation, Message
from . import services


class TodayDetailView(generic.DetailView):
    model = Today


def index(request):
    return render(request, 'webapp/welcome.html')


@login_required
def create(request):
    return render(request, 'webapp/damndaily/create.html')


@login_required
def subscribe(request, damndailyid):
    return render(request, 'webapp/damndaily/subscribe.html')


@login_required
def unsubscribe(request, damndailyid):
    pass


def save_subscription(request, damndailyid, username):
    return HttpResponse('subscribe damn daily id: %s' % (damndailyid,))


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
    return render(request, 'webapp/damndaily/index.html', context)


def update_today(request, todayid):
    today = get_object_or_404(Today, pk=todayid)
    today.time = request.POST['time']
    today.location = request.POST['location']
    today.save()
    return HttpResponseRedirect(reverse('webapp:view',
                                        args=(today.damndaily.external_id,)))


def participate(request, todayid):
    today = get_object_or_404(Today, pk=todayid)
    participation = Participation(today=today, user=request.user)
    participation.save()
    return HttpResponseRedirect(reverse('webapp:view',
                                        args=(today.damndaily.external_id,)))


def reject(request, todayid):
    pass
