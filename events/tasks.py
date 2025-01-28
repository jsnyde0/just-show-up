from celery import shared_task
from celery.utils.log import get_task_logger

from .utils import save_events, scrape_events

logger = get_task_logger(__name__)


@shared_task
def example_event_task():
    print("This is an event-related task.")


@shared_task
def test_openai_task():
    # return test_openai()
    print("We should be running a crew but not implemented yet...")


@shared_task
def test_agentic_event_scraping(days: int = 2):
    """Scrape events and save them to the database."""
    logger.info(f"Starting event scraping for next {days} days")

    try:
        # 1. Scrape events
        events = scrape_events(days)
        logger.info(f"Scraped {len(events)} events")

        # 2. Save to database
        saved_count = save_events(events)
        logger.info(f"Saved {saved_count} events")

        return saved_count

    except Exception as e:
        logger.error(f"Error in scraping task: {e}")
        raise
