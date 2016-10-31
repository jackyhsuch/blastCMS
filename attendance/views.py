from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from users.models import Users
from .models import Events
from .models import Attendances
from datetime import datetime

# Create your views here.
def index(request):
    event_list = Events.objects.order_by('id')
    context = {
        'event_list': event_list,
    }
    return render(request, 'attendance/index.html', context)


def new(request):
    context = {}

    if request.method == 'POST':
        # print(request.POST)
        name = request.POST['name']
        date = request.POST['date']
        years = request.POST.getlist('years')

        # create event
        newEvent = Events(
            name=name,
            date=date,
            isCompulsory=True
        )
        newEvent.save()

        eventId = newEvent.id


        # get all the users
        usersList = []
        for year in years:
            batchYear = datetime.now().year - int(year)
            users = list(Users.objects.filter(batch_year=batchYear))
            usersList += users


        # populate to attendance
        for user in usersList:
            print(user.name)
            print(user.batch_year)
            newRow = Attendances(
                event_id=eventId,
                user_id=user.id
            )

            newRow.save()

    return render(request, 'attendance/new.html', context)


# show each event details with name list
def show(request, event_id):
    context = {}

    event = get_object_or_404(Events, pk=event_id)
    context['event'] = event

    attendanceObjects = Attendances.objects.filter(event_id=event.id)
    context['attendanceObjects'] = attendanceObjects

    users = []
    for attendanceObject in attendanceObjects:
        user = Users.objects.get(pk=attendanceObject.user_id)
        user.status = attendanceObject.status
        users.append(user)

    context['user_list'] = users
    context['this_year'] = datetime.now().year

    return render(request, 'attendance/show.html', context)

def submit(request):
    eventId = request.POST['event_id']

    for key in request.POST:
        if key != 'event_id':
            print(key)
            value = request.POST[key]
            print(value)

            Attendances.objects.filter(
                user_id=key
            ).filter(
                event_id=eventId
            ).update(
                status=request.POST[key].lower()
            )

    return HttpResponse(
            content_type="application/json"
        )
