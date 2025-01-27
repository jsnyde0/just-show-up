from django.urls import path

from .views import event_detail, test_agentic, test_celery, test_event, test_openai

app_name = "events"

urlpatterns = [
    path("", test_event, name="test_event"),
    path("<int:pk>/", event_detail, name="event_detail"),
    path("test-celery/", test_celery, name="test_celery"),
    path("test-openai/", test_openai, name="test_openai"),
    path("test-agentic/", test_agentic, name="test_agentic"),
]
