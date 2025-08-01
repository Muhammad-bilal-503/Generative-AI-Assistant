import os
import subprocess
import sys
import logging
from fuzzywuzzy import process
from livekit.agents import function_tool
import asyncio
try:
    import pygetwindow as gw
except ImportError:
    gw = None

sys.stdout.reconfigure(encoding='utf-8')


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def focus_window(title_keyword: str) -> bool:
    if not gw:
        logger.warning("⚠ pygetwindow is not available.")
        return False

    await asyncio.sleep(1.5)
    title_keyword = title_keyword.lower().strip()

    for window in gw.getAllWindows():
        if title_keyword in window.title.lower():
            if window.isMinimized:
                window.restore()
            window.activate()
            logger.info(f"🪟 Window is in focus: {window.title}")
            return True
    logger.warning("⚠ Window not found to focus.")
    return False

async def index_files(base_dirs):
    file_index = []
    for base_dir in base_dirs:
        for root, _, files in os.walk(base_dir):
            for f in files:
                file_index.append({
                    "name": f,
                    "path": os.path.join(root, f),
                    "type": "file"
                })
    logger.info(f"✅ Indexed a total of {len(file_index)} files from {base_dirs}.")
    return file_index

async def search_file(query, index):
    choices = [item["name"] for item in index]
    if not choices:
        logger.warning("⚠ No files to match against.")
        return None

    best_match, score = process.extractOne(query, choices)
    logger.info(f"🔍 Matched '{query}' to '{best_match}' (Score: {score})")
    if score > 70:
        for item in index:
            if item["name"] == best_match:
                return item
    return None

async def open_file(item):
    try:
        logger.info(f"📂 Opening file: {item['path']}")
        if os.name == 'nt':
            os.startfile(item["path"])
        else:
            subprocess.call(['open' if sys.platform == 'darwin' else 'xdg-open', item["path"]])
        await focus_window(item["name"])  # 👈 Focus window after opening
        return f"✅ File opened successfully: {item['name']}"
    except Exception as e:
        logger.error(f"❌ Error opening file: {e}")
        return f"❌ Failed to open file. {e}"

async def handle_command(command, index):
    item = await search_file(command, index)
    if item:
        return await open_file(item)
    else:
        logger.warning("❌ File not found.")
        return "❌ File not found."

@function_tool
async def Play_file(name: str) -> str:
    # --- WE MADE A CHANGE HERE ---
    # Now the program will only scan these essential folders
    folders_to_index = [
        "C:/Users/Muhammad Bilal/Desktop",
        "C:/Users/Muhammad Bilal/Downloads",
        "C:/Users/Muhammad Bilal/Documents",
        "C:/Users/Muhammad Bilal/Pictures",
        "C:/Users/Muhammad Bilal/Music",
        "C:/Users/Muhammad Bilal/Videos",
        "D:/"  # We are also scanning the D: drive
    ]
    
    index = await index_files(folders_to_index)
    command = name.strip()
    return await handle_command(command, index)