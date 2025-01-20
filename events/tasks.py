from celery import shared_task

from .crewai.crew import TestCrewai


@shared_task
def example_event_task():
    print("This is an event-related task.")


@shared_task
def test_openai_task():
    # return test_openai()
    print("We should be running a crew but not implemented yet...")


@shared_task
def test_crewai_task():
    inputs = {"topic": "Agentic AI applications with Django and Celery"}
    result = TestCrewai().crew().kickoff(inputs=inputs)
    return result.to_dict()
