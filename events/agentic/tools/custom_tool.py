import requests
from bs4 import BeautifulSoup
from controlflow import tool


@tool
def scrape_sex_clubs_events(url: str):
    """
    Scrape specific sections (Sex or Clubs) from the provided URL.
    Returns the HTML content as a string.
    """
    # Send GET request to the URL
    response = requests.get(url)
    response.raise_for_status()

    # Parse HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all sections that have h3 headers
    relevant_sections = []
    sections = soup.find_all("section", class_="content listing")

    for section in sections:
        h3_tag = section.find("h3")
        if h3_tag and any(category in h3_tag.text for category in ["Sex", "Clubs"]):
            relevant_sections.append(str(section))

    # Combine all relevant sections
    if not relevant_sections:
        return ""  # Return empty string if no relevant sections found

    return "\n".join(relevant_sections)


@tool
def scrape_event_details(url: str) -> str:
    """
    Scrape specific event details and return them in a clean, markdown-like format.
    """
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Initialize details dictionary
    details = []

    # Get title
    if title_elem := soup.find("h3", class_="svelte-5l0ta8"):
        details.append(f"# {title_elem.text.strip()}")

    # Get date and location
    if info_list := soup.find("ul", class_="info-list"):
        for item in info_list.find_all("li"):
            details.append(item.text.strip())

    # Get main description
    if desc_elem := soup.find("div", class_="typography--first-p--emphasized"):
        # Extract text from paragraphs
        for p in desc_elem.find_all("p"):
            if p_text := p.text.strip():
                details.append(p_text)

    # Get tags
    tags = []
    for tag in soup.find_all("span", class_="svelte-1s4c2pi"):
        if tag_text := tag.text.strip():
            tags.append(tag_text)
    if tags:
        details.append("Tags: " + " ".join(tags))

    # Get venue details
    if venue_section := soup.find("section", recursive=False):
        if venue_name := venue_section.find("h3", class_="svelte-5l0ta8"):
            details.append(f"\nVenue: {venue_name.text.strip()}")

        # Get venue address and contact
        if venue_info := venue_section.find("ul", class_="info-list"):
            for item in venue_info.find_all("li"):
                if item_text := item.text.strip():
                    details.append(item_text)

    # Join all details with newlines
    return "\n".join(details)
