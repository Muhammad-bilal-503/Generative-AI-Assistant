import os
import requests
import logging
from dotenv import load_dotenv
from livekit.agents import function_tool  # ✅ Correct decorator
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
        logger.error("API key या Search Engine ID missing है।")
        return "Environment variables में API key या Search Engine ID missing है।"

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
        logger.error(f"Google API में error आया: {response.status_code} - {response.text}")
        return f"Google Search API में error आया: {response.status_code} - {response.text}"

    data = response.json()
    results = data.get("items", [])

    if not results:
        logger.info("कोई results नहीं मिले।")
        return "कोई results नहीं मिले।"

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
    # Pakistan ka time zone set karein
    pakistan_tz = pytz.timezone('Asia/Karachi')
    
    # Pakistan ke time zone ke hisab se abhi ka waqt haasil karein
    now_pakistan = datetime.now(pakistan_tz)
    
    # Time ko bolne ke liye asaan format mein badal dein
    formatted_time = now_pakistan.strftime("In Pakistan, the current time is %I:%M %p on %A, %d %B %Y.")
    
    return formatted_time
