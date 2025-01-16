import os

# from crewai import Agent, Crew, Task
from openai import OpenAI


def test_openai():
    client = OpenAI()
    completion = client.chat.completions.create(
        model=os.environ["OPENAI_MODEL_NAME"],
        messages=[{"role": "user", "content": "write a haiku about multi ai agents"}],
    )
    return completion.choices[0].message.content
