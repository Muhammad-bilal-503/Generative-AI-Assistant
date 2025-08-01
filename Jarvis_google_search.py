import os
import requests
import logging
from dotenv import load_dotenv
from livekit.agents import function_tool
from datetime import datetime
import pytz

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@function_tool
async def google_search(query: str) -> str:
    logger.info(f"Query received: {query}")

    api_key = os.getenv("GOOGLE_SEARCH_API_KEY")
    search_engine_id = os.getenv("SEARCH_ENGINE_ID")

    if not api_key or not search_engine_id:
        logger.error("API key or Search Engine ID is missing.")
        return "API key or Search Engine ID is missing in environment variables."

    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": api_key,
        "cx": search_engine_id,
        "q": query,
        "num": 3
    }

    logger.info("Sending request to Google Custom Search API...")
    response = requests.get(url, params=params)

    if response.status_code != 200:
        logger.error(f"Error from Google API: {response.status_code} - {response.text}")
        return f"Error from Google Search API: {response.status_code} - {response.text}"

    data = response.json()
    results = data.get("items", [])

    if not results:
        logger.info("No results found.")
        return "No results found."

    formatted = ""
    logger.info("Search results:")
    for i, item in enumerate(results, start=1):
        title = item.get("title", "No title")
        link = item.get("link", "No link")
        snippet = item.get("snippet", "")
        formatted += f"{i}. {title}\n{link}\n{snippet}\n\n"
        logger.info(f"{i}. {title}\n{link}\n{snippet}\n")

    return formatted.strip()

@function_tool
async def get_current_datetime() -> str:
    """
    Returns the current date and time for the Pakistan (Asia/Karachi) time zone
    in a user-friendly format.
    """
    # Set the time zone for Pakistan
    pakistan_tz = pytz.timezone('Asia/Karachi')
    
    # Get the current time according to the Pakistan time zone
    now_pakistan = datetime.now(pakistan_tz)
    
    # Change the time into an easy-to-speak format
    formatted_time = now_pakistan.strftime("In Pakistan, the current time is %I:%M %p on %A, %d %B %Y.")
    
    return formatted_time