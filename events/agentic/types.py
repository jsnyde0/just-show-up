from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field, HttpUrl, validator


class EventBasic(BaseModel):
    title: str = Field(..., description="The title of the event")
    summary: str = Field(..., description="A short summary of the event")
    detail_url: HttpUrl = Field(..., description="The URL of the event detail page")

    @classmethod
    def set_base_url(cls, base_url: str):
        cls._base_url = base_url

    @validator("detail_url", pre=True)
    def ensure_absolute_url(cls, v):
        if isinstance(v, str) and v.startswith("/"):
            base_url = getattr(cls, "_base_url", None)
            if not base_url:
                raise ValueError(
                    "Base URL not set. Call EventBasic.set_base_url() first"
                )
            return f"{base_url.rstrip('/')}{v}"
        return v

    class Config:
        json_encoders = {HttpUrl: str}


class EventFull(EventBasic):
    """Complete event information including detail page data"""

    description: Optional[str] = Field(
        None, description="The full description of the event"
    )
    location: Optional[str] = Field(None, description="The location of the event")
    start_time: datetime = Field(..., description="When the event starts")
    end_time: Optional[datetime] = Field(None, description="When the event ends")
    organizer: Optional[str] = Field(None, description="Who is organizing the event")
    event_url: Optional[HttpUrl] = Field(
        None, description="External URL (e.g., Facebook event, venue website)"
    )
    image_url: Optional[HttpUrl] = Field(
        None, description="URL to the main event image found on the detail page"
    )
    attendees: Optional[int] = Field(
        None, description="Number of attendees if available"
    )
    price: Optional[Decimal] = Field(None, description="Event price in euros")
    original_tags: list[str] = Field(
        [], description="The original tags of the event found on the detail page"
    )

    class Config:
        json_encoders = {datetime: lambda v: v.isoformat(), Decimal: lambda v: str(v)}


class EventEnriched(EventFull):
    fomo_score: Optional[int] = Field(None, description="The FOMO score of the event")
    fomo_score_reason: Optional[str] = Field(
        None, description="The reason for the FOMO score"
    )
