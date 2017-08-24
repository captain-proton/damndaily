from django.shortcuts import render, HttpResponse
from datetime import date
from .models import DamnDaily, Today, Participation


# Create your views here.
def index(request):
    return HttpResponse('hello damn daily')


def view(request, damndailyid):
    participations = Participation.objects \
        .filter(today__day=date.today()) \
        .filter(today__damn_daily__external_id=damndailyid)
    damndaily = DamnDaily.objects.get(external_id=damndailyid)
    today = Today.objects \
        .filter(damn_daily__external_id=damndailyid) \
        .get(day=date.today())
    context = {
        'participations': participations,
        'damndaily': damndaily,
        'today': today
    }
    print(context)
    return render(request, 'webapp/view.html', context)


def edit(request, damndailyid):
    return HttpResponse('edit damn daily id: %s' % (damndailyid,))
