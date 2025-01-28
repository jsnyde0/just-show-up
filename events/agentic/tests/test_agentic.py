# basic test
import os

import pytest
from controlflow import run
from openai import OpenAI

from ..tools.custom_tool import scrape_event_details, scrape_sex_clubs_events
from ..types import EventBasic, EventFull


@pytest.mark.agentic
def test_openai_api():
    client = OpenAI()
    prompt = "write a 3-line haiku about multi ai agents, \
                 containing 'AI' exactly once."
    completion = client.chat.completions.create(
        model=os.environ["OPENAI_MODEL_NAME"],
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )
    result = completion.choices[0].message.content

    assert len(result.split("\n")) == 3  # result should contain 3 lines
    assert "AI" in result  # result should contain the word "AI"


@pytest.mark.agentic
def test_agentic():
    a = True
    b = True
    assert a == b


@pytest.mark.agentic
def test_scrape_sex_clubs_events():
    test_url = "https://www.siegessaeule.de/en/events/?date=2025-01-21"
    EventBasic.set_base_url("https://www.siegessaeule.de")

    result = run(
        "Scrape the sex and clubs events from the provided URL",
        tools=[scrape_sex_clubs_events],
        context={"url": test_url},
        result_type=list[EventBasic],
    )

    # Basic structure validation
    assert isinstance(result, list)
    assert len(result) > 0

    # Validate EventBasic fields
    for event in result:
        assert isinstance(event, EventBasic)
        assert event.title
        assert event.summary
        assert str(event.detail_url).startswith("https://www.siegessaeule.de")


@pytest.mark.agentic
def test_scrape_event_details():
    # Setup
    detail_url = "https://www.siegessaeule.de/en/events/sex/naked-sex-party-lab/2025-01-23/21:00/"
    EventFull.set_base_url("https://www.siegessaeule.de")

    # Execute
    result = run(
        "Get the main content of the event detail page of the provided URL",
        tools=[scrape_event_details],
        context={"url": detail_url},
        result_type=EventFull,
    )

    # Content validation
    assert result.title == "Naked Sex Party"
    assert "Lab.oratory" in result.location
    assert result.start_time.isoformat().startswith("2025-01-23T20:00:00")
    assert str(result.detail_url) == detail_url

    # Tags validation
    assert len(result.original_tags) > 0
    assert "#gay" in result.original_tags
    assert "#sex" in result.original_tags
