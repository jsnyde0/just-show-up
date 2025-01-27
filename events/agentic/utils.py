from datetime import date, timedelta
from typing import List


def construct_siegessaeule_url(target_date: date) -> str:
    """
    Construct a Siegessäule events URL for a specific date.

    Args:
        target_date: The date to get events for

    Returns:
        The complete URL for that date
    """
    base_url = "https://www.siegessaeule.de/en/events/"
    return f"{base_url}?date={target_date.strftime('%Y-%m-%d')}"


def get_urls_for_date_range(start_date: date, end_date: date) -> List[str]:
    """
    Generate URLs for a range of dates.

    Args:
        start_date: First date to include
        end_date: Last date to include

    Returns:
        List of URLs, one for each date in the range
    """
    urls = []
    current_date = start_date

    while current_date <= end_date:
        urls.append(construct_siegessaeule_url(current_date))
        current_date += timedelta(days=1)

    return urls


def get_urls_next_days(days: int) -> List[str]:
    """
    Generate URLs for today and the next `days` days.

    Returns:
        List of `days` URLs, one for each day
    """
    today = date.today()
    end_date = today + timedelta(days=days - 1)
    return get_urls_for_date_range(today, end_date)
