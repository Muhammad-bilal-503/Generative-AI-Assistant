# Jarvis - A Voice-Controlled AI Assistant

![Project Demo](https://placehold.co/800x400/2d3748/ffffff?text=Add+a+GIF+Demo+of+Your+Project+Here)
*<p align="center"><strong>(Important: Replace the image above with a GIF or video demonstrating Jarvis in action!)</strong></p>*

---

### 🇮🇳 Project by Muhammad Bilal 🇵🇰

A sophisticated, real-time, voice-controlled AI assistant inspired by Iron Man's Jarvis. This project leverages the power of modern LLMs and real-time communication frameworks to create an agent that can not only converse but also actively assist with tasks on your Windows PC.

## ✨ Key Features

Jarvis is more than just a chatbot. It's an extensible agent with a growing set of capabilities:

-   **🗣️ Real-Time Conversation:** Engage in fluid, low-latency conversations with a unique, witty, and formal Urdu-speaking persona powered by **Google Gemini**.
-   **🖥️ Full System Control:**
    -   **Application Management:** Open and close any application on your PC (e.g., "Chrome کھولو", "VS Code band karo").
    -   **Mouse & Keyboard Automation:** Control the cursor, perform clicks, scroll, type text, and press hotkeys, all through voice commands.
    -   **File System Operations:** Create, rename, delete, and open files and folders on your drives.
-   **👁️ AI Vision (Screen Reading):**
    -   Using **Tesseract-OCR**, Jarvis can "see" your screen, read its contents, and provide you with a concise summary.
-   **🌐 Real-Time Information Retrieval:**
    -   **Google Search:** Ask any question and get summarized results from the web.
    -   **Latest News:** Fetch top headlines from around the world (or specifically from Pakistan) via the **GNews API**.
    -   **Weather Updates:** Get real-time weather information for any city using the **OpenWeather API**.
-   **🧠 Intelligent & Context-Aware:**
    -   Jarvis understands context, especially regarding dates and times, ensuring the information provided is always relevant.
    -   Uses fuzzy string matching (**fuzzywuzzy**) to intelligently find the correct file or folder even if the name isn't exact.

## 🛠️ How It Works (Architecture)

The project is built on a modern, agent-based architecture:

1.  **LiveKit Agents Framework:** This is the backbone of the project, handling the real-time audio pipeline (mic input -> STT -> LLM -> TTS -> speaker output) with extremely low latency.
2.  **Google Gemini Realtime LLM:** This Large Language Model acts as the "brain" of Jarvis. It processes user speech, understands intent, and decides which tool to use.
3.  **Tool-Based Functionality:** Jarvis's skills are defined as individual Python functions (tools) decorated with `@function_tool`. The LLM intelligently chooses the right tool based on the user's command (e.g., if you say "weather batao," it calls the `get_weather` tool).
4.  **Custom Persona Prompting:** The personality, language style, and behavior of Jarvis are meticulously defined in `Jarvis_prompts.py`. This prompt guides the LLM to respond in a consistent, Jarvis-like manner.
5.  **System Interface:** Libraries like `pyautogui`, `pynput`, and `os` are used to create a bridge between the AI's decisions and the computer's operating system, allowing it to perform real-world actions.

## 🚀 Getting Started

Follow these steps to get Jarvis running on your local machine.

### Prerequisites

Make sure you have the following software installed on your Windows machine:

-   **Python 3.9+:** [Download Python](https://www.python.org/downloads/)
-   **Git:** [Download Git](https://git-scm.com/downloads)
-   **Tesseract-OCR:** This is required for the "vision" (screen reading) feature.
    -   [Download the Tesseract installer for Windows](https://github.com/UB-Mannheim/tesseract/wiki).
    -   During installation, make sure you are connected to the internet and select the option to install additional language scripts, including Urdu/Arabic.
    -   Remember the installation path (default is `C:\Program Files\Tesseract-OCR`).

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-jarvis-repo.git
    cd your-jarvis-repo
    ```

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure API Keys:**
    -   In the project's root directory, create a new file named `.env`.
    -   Copy the contents of the example below into your `.env` file and fill in your own API keys.

    ```dotenv
    # .env.example

    # --- Google AI & Search ---
    # Get from Google AI Studio: https://makersuite.google.com/app/apikey
    GOOGLE_API_KEY="YOUR_GOOGLE_AI_API_KEY"
    # Get from Google Cloud Console (Custom Search API): https://developers.google.com/custom-search/v1/overview
    GOOGLE_SEARCH_API_KEY="YOUR_GOOGLE_SEARCH_API_KEY"
    SEARCH_ENGINE_ID="YOUR_CUSTOM_SEARCH_ENGINE_ID"

    # --- OpenWeather API (for Weather) ---
    # Get from: https://openweathermap.org/api
    OPENWEATHER_API_KEY="YOUR_OPENWEATHER_API_KEY"

    # --- GNews API (for News) ---
    # Get from: https://gnews.io/
    NEWS_API_KEY="YOUR_GNEWS_API_KEY"

    # --- Cricket API (Optional, for future features) ---
    # Get from: https://www.api-cricket.com/
    CRICKET_API_KEY="YOUR_CRICKET_API_KEY"
    ```

5.  **Verify Tesseract Path:**
    -   Open the `Jarvis_vision.py` file.
    -   Ensure the path on the first line matches your Tesseract installation directory.
        ```python
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        ```

### Running the Agent

Once everything is set up, run the agent with this simple command:

```bash
python agent.py console
