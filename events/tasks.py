from celery import shared_task

from .crewai.crew import test_openai


@shared_task
def example_event_task():
    print("This is an event-related task.")


@shared_task
def test_openai_task():
    return test_openai()
