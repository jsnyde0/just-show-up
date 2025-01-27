from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse


class Event(models.Model):
    # Basic fields (EventBasic)
    title = models.CharField(max_length=127)
    summary = models.CharField(max_length=255, blank=True, null=True)
    detail_url = models.URLField(max_length=200, blank=True, null=True)

    # Full fields (EventFull)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    organizer = models.CharField(max_length=255, blank=True, null=True)
    source = models.CharField(max_length=100)
    source_url = models.URLField(max_length=200, blank=True, null=True)
    image_url = models.URLField(max_length=200, blank=True, null=True)
    original_tags = ArrayField(
        models.CharField(max_length=100), default=list, blank=True
    )
    attendees = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    # Enriched fields (EventEnriched)
    fomo_score = models.IntegerField(null=True, blank=True)
    fomo_score_reason = models.TextField(null=True, blank=True)

    # metadata
    class ProcessingState(models.TextChoices):
        PENDING = "pending", "Pending"
        SCRAPED = "scraped", "Basic Info Scraped"
        ENRICHED = "enriched", "Fully Enriched"

    processing_state = models.CharField(
        max_length=20, choices=ProcessingState.choices, default=ProcessingState.PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("events:event_detail", kwargs={"pk": self.pk})

    class Meta:
        indexes = [
            models.Index(fields=["processing_state"]),
        ]
