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
from Jarvis_window_CTRL import open_app, close, folder_file
from Jarvis_file_opner import Play_file
from Jarvis_news import get_latest_news
from Jarvis_cricket import get_live_cricket_score, get_cricket_schedule
from Jarvis_vision import read_current_screen
from keyboard_mouse_CTRL import move_cursor_tool, mouse_click_tool, scroll_cursor_tool, type_text_tool, press_key_tool, swipe_gesture_tool, press_hotkey_tool, control_volume_tool
load_dotenv()


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(instructions=behavior_prompts,
                         tools=[
                            google_search,
                            get_current_datetime,
                            get_weather,
                            open_app, 
                            get_latest_news,
                            read_current_screen,
                            close, 
                            get_live_cricket_score,   
                            get_cricket_schedule,  
                            folder_file, #folder
                            Play_file,  #file  MP4, MP3, PDF, PPT, img, png etc.
                            move_cursor_tool, #cursor move 
                            mouse_click_tool, # mouse click 
                            scroll_cursor_tool, #cursor scroll 
                            type_text_tool, # text type 
                            press_key_tool, #key press 
                            press_hotkey_tool, # hotkey press 
                            control_volume_tool, #volume control 
                            swipe_gesture_tool #gesture wipe 
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


