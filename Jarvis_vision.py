# Jarvis_vision.py

import pyautogui
import pytesseract
import logging
from livekit.agents import function_tool

# --- YAHAN APNA TESSERACT KA PATH DAALEIN ---
# Agar aapne default location par install kiya hai to isko change karne ki zaroorat nahi
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@function_tool
async def read_current_screen() -> str:
    """
    Takes a screenshot of the current screen, uses OCR to extract all visible text,
    and returns the text for the AI to summarize. This tool gives Jarvis "eyes".
    """
    try:
        logger.info("Taking a screenshot to read the screen...")
        # Screenshot lein
        screenshot = pyautogui.screenshot()
        
        # Screenshot se text nikalein
        extracted_text = pytesseract.image_to_string(screenshot)
        
        if not extracted_text.strip():
            logger.warning("OCR could not detect any text on the screen.")
            return "I looked, but I could not find any readable text on the screen."
            
        logger.info(f"Successfully extracted text from the screen. Length: {len(extracted_text)}")
        
        # AI ko summarize karne ke liye text wapas bhejein
        return f"Here is the text I found on the screen: {extracted_text}"

    except FileNotFoundError:
        logger.error("Tesseract is not installed or the path is incorrect in Jarvis_vision.py.")
        return "Sorry, my vision module is not configured correctly. Please ensure Tesseract-OCR is installed."
    except Exception as e:
        logger.error(f"An error occurred while reading the screen: {e}")
        return "I encountered an error while trying to read the screen."
    