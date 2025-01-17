# basic test
import os

import pytest
from openai import OpenAI


@pytest.mark.crewai
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


@pytest.mark.crewai
def test_crewai():
    a = True
    b = True
    assert a == b
