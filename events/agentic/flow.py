import controlflow as cf

from .tools.custom_tool import scrape_event_details, scrape_sex_clubs_events
from .types import EventBasic, EventFull


@cf.flow
def scrape_siegessaeule_events(url: str) -> list[EventFull]:
    basic_events = cf.run(
        objective="Scrape events from the provided URL",
        instructions="Identify the events on the page of the provided URL and \
            return the title, summary, and full detail URL for each event",
        context={"url": url},
        tools=[scrape_sex_clubs_events],
        result_type=list[EventBasic],
    )

    full_events = cf.run(
        objective="Enrich the events with data from their detail pages",
        instructions="Scrape the main content of each event detail page \
                      to enrich the event data",
        context={"events": basic_events},
        tools=[scrape_event_details],
        result_type=list[EventFull],
    )

    return full_events
