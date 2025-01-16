from celery import shared_task


@shared_task
def example_event_task():
    print("This is an event-related task.")
