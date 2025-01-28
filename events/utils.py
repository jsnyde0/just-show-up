"""Services for event-related operations."""

from typing import List

from django.db import transaction

from .agentic.flow import scrape_siegessaeule_events
from .agentic.types import EventFull
from .agentic.utils import get_urls_next_days
from .models import Event


def scrape_events(days: int = 2) -> List[EventFull]:
    """Scrape events from all URLs for the next N days."""
    all_events = []
    for url in get_urls_next_days(days):
        events = scrape_siegessaeule_events(url)
        all_events.extend(events)
    return all_events


def save_events(events: List[EventFull]) -> int:
    """Save events to database, avoiding duplicates."""
    saved_count = 0
    with transaction.atomic():
        for event_data in events:
            event_dict = event_data.model_dump()
            Event.objects.update_or_create(
                title=event_dict["title"],
                start_time=event_dict["start_time"],
                defaults={
                    **event_dict,
                    "source": "siegessaeule",
                    "processing_state": Event.ProcessingState.SCRAPED,
                },
            )
            saved_count += 1
    return saved_count
