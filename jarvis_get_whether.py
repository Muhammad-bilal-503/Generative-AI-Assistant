import os
import requests
import logging
from dotenv import load_dotenv
from livekit.agents import function_tool

load_dotenv()


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def detect_city_by_ip() -> str:
    try:
        logger.info("Attempting to detect city via IP address")
        ip_info = requests.get("https://ipapi.co/json/").json()
        city = ip_info.get("city")
        if city:
            logger.info(f"Detected city from IP: {city}")
            return city
        else:
            logger.warning("Failed to detect city, using default 'Lahore'.")
            return "Lahore"
    except Exception as e:
        logger.error(f"Error detecting city from IP: {e}")
        return "Lahore"

@function_tool
async def get_weather(city: str = "") -> str:
    
    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key:
        logger.error("OpenWeather API key is missing.")
        return "OpenWeather API key not found in environment variables."

    if not city:
        city = detect_city_by_ip()

    logger.info(f"Fetching weather for city: {city}")
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params)
        if response.status_code != 200:
            logger.error(f"Error from OpenWeather API: {response.status_code} - {response.text}")
            return f"Error: Could not fetch weather for {city}. Please check the city name."

        data = response.json()
        weather = data["weather"][0]["description"].title()
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        result = (f"Weather in {city}:\n"
                  f"- Condition: {weather}\n"
                  f"- Temperature: {temperature}°C\n"
                  f"- Humidity: {humidity}%\n"
                  f"- Wind Speed: {wind_speed} m/s")

        logger.info(f"Weather result: \n{result}")
        return result

    except Exception as e:
        logger.exception(f"Exception occurred while fetching weather: {e}")
        return "An error occurred while fetching the weather."
    