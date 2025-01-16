from django.db import models
from django.urls import reverse


class Event(models.Model):
    title = models.CharField(max_length=127)
    summary = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    organizer = models.CharField(max_length=255, blank=True, null=True)
    source = models.CharField(max_length=100)
    source_url = models.URLField(max_length=200, blank=True, null=True)
    url = models.URLField(max_length=200, blank=True, null=True)
    image_url = models.URLField(max_length=200, blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True, null=True)
    attendees = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=50, default="scheduled")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("events:event_detail", kwargs={"pk": self.pk})
