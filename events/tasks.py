from celery import shared_task


@shared_task
def example_event_task():
    print("This is an event-related task.")


@shared_task
def test_openai_task():
    # return test_openai()
    print("We should be running a crew but not implemented yet...")
