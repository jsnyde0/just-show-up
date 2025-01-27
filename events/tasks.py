import json

from celery import shared_task

from .agentic.flow import scrape_siegessaeule_events
from .agentic.utils import get_urls_next_days


@shared_task
def example_event_task():
    print("This is an event-related task.")


@shared_task
def test_openai_task():
    # return test_openai()
    print("We should be running a crew but not implemented yet...")


@shared_task
def test_agentic_event_scraping():
    # set up urls
    urls = get_urls_next_days(2)
    print("Generated URLs:")
    for url in urls:
        print(f"- {url}")

    # scrape events
    events = []
    for url in urls:
        events.extend(scrape_siegessaeule_events(url))

    # convert to json?
    event_json = json.dumps(
        [event.model_dump() for event in events], indent=2, default=str
    )
    print(event_json)
    return event_json
