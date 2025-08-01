from dotenv import load_dotenv

from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import (
    google,
    noise_cancellation,
)
from Jarvis_prompts import behavior_prompts, Reply_prompts
from Jarvis_google_search import google_search, get_current_datetime
from jarvis_get_whether import get_weather
from Jarvis_window_CTRL import open, close, folder_file
from Jarvis_file_opner import Play_file
from keyboard_mouse_CTRL import move_cursor_tool, mouse_click_tool, scroll_cursor_tool, type_text_tool, press_key_tool, swipe_gesture_tool, press_hotkey_tool, control_volume_tool
load_dotenv()


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(instructions=behavior_prompts,
                         tools=[
                            google_search,
                            get_current_datetime,
                            get_weather,
                            open,  # For opening applications
                            close,
                            folder_file,  # For opening folders
                            Play_file,  # For running files like MP4, MP3, PDF, PPT, img, png etc.
                            move_cursor_tool,  # For moving the cursor
                            mouse_click_tool,  # For performing mouse clicks
                            scroll_cursor_tool,  # For scrolling the cursor
                            type_text_tool,  # For typing text
                            press_key_tool,  # For pressing a key
                            press_hotkey_tool,  # For pressing a hotkey/shortcut
                            control_volume_tool,  # For controlling volume
                            swipe_gesture_tool  # For performing swipe gestures
                         ]
                         )


async def entrypoint(ctx: agents.JobContext):
    session = AgentSession(
        llm=google.beta.realtime.RealtimeModel(
            voice="Charon"
        )
    )
    
    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            noise_cancellation=noise_cancellation.BVC(),
            video_enabled=True
        ),
    )

    await ctx.connect()

    await session.generate_reply(
        instructions=Reply_prompts
    )


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))