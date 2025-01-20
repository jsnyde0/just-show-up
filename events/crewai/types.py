from pydantic import BaseModel


class ResearchReport(BaseModel):
    title: str
    content: str
