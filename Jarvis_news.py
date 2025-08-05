# Jarvis_news.py (Updated for GNews.io)

import os
import aiohttp
import logging
from livekit.agents import function_tool

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@function_tool
async def get_latest_news(country: str = 'pk', lang: str = 'ur') -> str:
    """
    Fetches the latest news headlines from GNews.io for a specific country using an async HTTP client.
    GNews often provides better results for Pakistan and supports Urdu.
    """
    # Key aapki .env file se hi aayegi
    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        logger.error("GNews.io API key is missing from .env file.")
        return "Sorry, the GNews API key is not configured."

    # URL ko GNews ke format ke mutabiq badla gaya hai
    # Note: GNews 'token' istemal karta hai, 'apiKey' nahi
    url = f"https://gnews.io/api/v4/top-headlines?country={country}&lang={lang}&token={api_key}"

    try:
        logger.info(f"Fetching news from GNews.io for country: {country}, lang: {lang}")
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                logger.info(f"GNews.io Response Status: {response.status}")
                
                if response.status != 200:
                    if response.status == 401:
                         return "There seems to be an issue with the GNews.io API key. It might be invalid or expired."
                    return f"Sorry, I couldn't connect to the news service. Status code: {response.status}"

                data = await response.json()
                articles = data.get("articles", [])

                if not articles or data.get("totalArticles", 0) == 0:
                    logger.warning(f"GNews.io returned 0 articles for country: {country}")
                    return f"I checked, but there are no current news headlines available for {country} in {lang} language right now."

                # Headlines ko behtar tareeqe se format karein (newline ke sath)
                headlines = [f"{i+1}. {article.get('title', 'No Title')}" for i, article in enumerate(articles[:5])] # 5 headlines de rahe hain
                formatted_response = "Here are the top headlines:\n" + "\n".join(headlines)
                
                return formatted_response

    except Exception as e:
        logger.error(f"An unexpected error occurred while fetching news: {e}")
        return "An unexpected error occurred while fetching the news."