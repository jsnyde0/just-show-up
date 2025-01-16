# from django.shortcuts import render
from django.http import HttpResponse

from .tasks import example_event_task


# Create your views here.
def test_event(request):
    pass


def event_detail(request, pk):
    # event = Event.objects.get(pk=pk)
    # return render(request, 'events/event_detail.html', {'event': event})
    pass


def test_celery(request):
    example_event_task.delay()
    return HttpResponse("Celery task started")
