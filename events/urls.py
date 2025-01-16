from django.urls import path

from .views import event_detail, test_celery, test_event

app_name = "events"

urlpatterns = [
    path("", test_event, name="test_event"),
    path("<int:pk>/", event_detail, name="event_detail"),
    path("test-celery/", test_celery, name="test_celery"),
]
