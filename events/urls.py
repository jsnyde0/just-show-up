from django.urls import path

from .views import event_detail, test_celery, test_event, test_openai

app_name = "events"

urlpatterns = [
    path("", test_event, name="test_event"),
    path("<int:pk>/", event_detail, name="event_detail"),
    path("test-celery/", test_celery, name="test_celery"),
    path("test-openai/", test_openai, name="test_openai"),
    # path("test-crewai/", test_crewai, name="test_crewai"),
]
