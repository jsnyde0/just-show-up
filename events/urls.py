from django.urls import path

from .views import event_detail, test_event

urlpatterns = [
    path("", test_event, name="test_event"),
    path("<int:pk>/", event_detail, name="event_detail"),
]
