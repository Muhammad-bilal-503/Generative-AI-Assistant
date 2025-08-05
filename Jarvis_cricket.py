# Jarvis_cricket.py

import os
import requests
import logging
from livekit.agents import function_tool

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@function_tool
async def get_live_cricket_score(team_name: str = "Pakistan") -> str:
    """
    Fetches live cricket scores from API-Cricket, focusing on a specific team if provided.
    """
    api_key = os.getenv("CRICKET_API_KEY")
    if not api_key:
        return "Sorry, the Cricket API key is not configured."

    url = f"https://api.api-cricket.com/v1/cricket?api_key={api_key}"

    try:
        logger.info("Fetching live cricket matches...")
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        live_matches = data.get('data', [])

        if not live_matches:
            return "There are no live cricket matches happening right now."

        # Find a match involving the specified team
        team_match = None
        for match in live_matches:
            if team_name.lower() in match.get('t1', '').lower() or team_name.lower() in match.get('t2', '').lower():
                team_match = match
                break
        
        # If no specific team match is found, return the first live match
        if not team_match:
            team_match = live_matches[0]

        team1 = team_match.get('t1', 'Team 1')
        team2 = team_match.get('t2', 'Team 2')
        score = team_match.get('score', 'Score not available')
        status = team_match.get('status', 'Status not available')

        result = f"Live match update: {team1} versus {team2}. The current score is {score}. Status: {status}"
        return result

    except Exception as e:
        logger.error(f"Error fetching cricket scores: {e}")
        return "Sorry, I am having trouble getting live cricket scores at the moment."
    

# Yeh Sahi Code Hai

@function_tool
async def get_cricket_schedule() -> str:
    """
    Fetches the upcoming cricket schedule from API-Cricket.
    """
    api_key = os.getenv("CRICKET_API_KEY")
    if not api_key:
        return "Sorry, the Cricket API key is not configured."

    url = f"https://api.api-cricket.com/v1/schedule?api_key={api_key}"
    
    try:
        logger.info("Fetching cricket schedule...")
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        schedule = data.get('data', [])

        if not schedule:
            return "There are no upcoming cricket matches scheduled."

        formatted_schedule = "Here is the upcoming cricket schedule: ... "
        
        # Sirf top 3 aane wale matches lein
        for match in schedule[:3]:
            date = match.get('date', 'Date not available')
            team1 = match.get('t1', 'Team 1')
            team2 = match.get('t2', 'Team 2')
            match_info = f"On {date}, {team1} will play against {team2}. ... "
            formatted_schedule += match_info
            
        return formatted_schedule.strip()

    except Exception as e:
        logger.error(f"Error fetching cricket schedule: {e}")
        return "Sorry, I am having trouble getting the cricket schedule at the moment."
    