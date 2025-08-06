<div align="center">
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSI0VCNzCEaCT6KPuVrwClciPTprHVJSLpW3A&s" alt="Jarvis Logo">
  <h1>Jarvis - Your Personal AI Voice Assistant</h1>
  <p>
    An advanced, voice-controlled AI assistant inspired by Iron Man's Jarvis. Designed to understand, assist, and interact with your Windows PC in real-time.
  </p>
  <p>
    <a href="#-key-features"><strong>Features</strong></a> ·
    <a href="#-tech-stack"><strong>Tech Stack</strong></a> ·
    <a href="#-getting-started"><strong>Installation</strong></a> ·
    <a href="#-how-to-run"><strong>Usage</strong></a> ·
    <a href="#-project-structure"><strong>Project Structure</strong></a> ·
    <a href="#-contributing"><strong>Contributing</strong></a>
  </p>
  <p>
    <img src="https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python" alt="Python Version">
    <img src="https://img.shields.io/badge/Framework-LiveKit_Agents-orange?style=for-the-badge" alt="Framework">
    <img src="https://img.shields.io/badge/LLM-Google_Gemini-4285F4?style=for-the-badge&logo=google" alt="LLM">
    <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
  </p>
</div>

![Project Demo]([![Alt Text](thumbnail.png.png)](https://youtu.be/kXe_pFqz27M?si=tWDRIMHglqcP6tUE))
*<p align="center"><strong>(Important: Replace the image above with a GIF or video demonstrating Jarvis in action!)</strong></p>*

---

## 📖 Overview

This project brings the concept of a futuristic AI assistant to life. **Jarvis** is not just a chatbot; it is a powerful, extensible agent built with the **LiveKit Agents Framework** and powered by the **Google Gemini Realtime LLM**. It listens to your voice, understands your commands in natural language (Urdu and English), and interacts directly with your operating system to perform a wide variety of tasks.

The core philosophy is to create a seamless human-computer interaction experience, making you more productive and your workflow more efficient, all while enjoying the company of a witty and intelligent AI.

## ✨ Key Features

Jarvis is equipped with a versatile set of tools, allowing it to perform numerous functions:

| Feature Category        | Description                                                                                                                              |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| 🗣️ **Real-Time Voice**  | Engage in fluid, low-latency conversations with a unique, polite, and witty Urdu-speaking persona.                                       |
| 🖥️ **System Control**    | **Open/Close Apps**, manage files/folders, and control your mouse and keyboard with simple voice commands.                               |
| 👁️ **AI Vision (OCR)**  | Jarvis can **"see" and read the text on your screen** using Tesseract-OCR, summarizing it for you on command.                              |
| 🌐 **Live Information** | Get **latest news headlines** (GNews API), **real-time weather updates** (OpenWeather API), and perform **Google searches** instantly. |
| 🧠 **Intelligent & Aware** | Understands context, especially regarding dates and times, to provide relevant answers and uses fuzzy string matching for smart file searches. |
| 🛠️ **Extensible**        | The tool-based architecture makes it incredibly easy to add new skills and capabilities to Jarvis.                                         |
| 📝 **Command Logging**    | All keyboard and mouse actions are logged in `controller_log.txt` for debugging and transparency.                                        |



## 🛠️ Tech Stack

This project is built using a combination of modern AI technologies and robust Python libraries:

-   **Core Framework:** `livekit-agents` for the real-time, low-latency agent architecture.
-   **Large Language Model (LLM):** `google-generativeai` (Google Gemini Realtime Model) for understanding, reasoning, and response generation.
-   **System Automation:** `pyautogui`, `pynput` for controlling the mouse, keyboard, and screen.
-   **File/App Management:** `pywin32`, `pygetwindow` for interacting with Windows applications and the file system.
-   **AI Vision:** `pytesseract` for Optical Character Recognition (OCR).
-   **Web & APIs:** `aiohttp`, `requests` for asynchronous and synchronous API calls.
-   **Utility:** `python-dotenv`, `fuzzywuzzy` for environment management and smart searching.

## 🚀 Getting Started

Follow these steps to set up and run Jarvis on your local Windows machine.

### 1. Prerequisites

Ensure you have the following installed:

-   **Python 3.9 or newer:** [Download Python](https://www.python.org/downloads/)
-   **Git:** [Download Git](https://git-scm.com/downloads)
-   **Tesseract-OCR:** Required for the "vision" feature.
    -   [Download the Tesseract installer for Windows](https://github.com/UB-Mannheim/tesseract/wiki).
    -   **Important:** During installation, ensure you are connected to the internet and select the option to install additional language scripts, including **Urdu/Arabic**.
    -   Note down the installation path (default is `C:\Program Files\Tesseract-OCR`).

### 2. Installation & Configuration

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/your-jarvis-repo.git
    cd your-jarvis-repo
    ```

2.  **Create and Activate a Virtual Environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install All Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Up API Keys:**
    -   Create a file named `.env` in the project's root directory.
    -   Copy the content below into your `.env` file and replace the placeholder values with your actual API keys.

    **`.env` file content:**
    ```dotenv
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
    -   Confirm that the `pytesseract.pytesseract.tesseract_cmd` path matches your Tesseract installation directory.
        ```python
        # In Jarvis_vision.py
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        ```

        ## 🛠️ How It Works (Architecture)

The project is built on a modern, agent-based architecture:

1.  **LiveKit Agents Framework:** This is the backbone of the project, handling the real-time audio pipeline (mic input -> STT -> LLM -> TTS -> speaker output) with extremely low latency.
2.  **Google Gemini Realtime LLM:** This Large Language Model acts as the "brain" of Jarvis. It processes user speech, understands intent, and decides which tool to use.
3.  **Tool-Based Functionality:** Jarvis's skills are defined as individual Python functions (tools) decorated with `@function_tool`. The LLM intelligently chooses the right tool based on the user's command (e.g., if you say "weather batao," it calls the `get_weather` tool).
4.  **Custom Persona Prompting:** The personality, language style, and behavior of Jarvis are meticulously defined in `Jarvis_prompts.py`. This prompt guides the LLM to respond in a consistent, Jarvis-like manner.
5.  **System Interface:** Libraries like `pyautogui`, `pynput`, and `os` are used to create a bridge between the AI's decisions and the computer's operating system, allowing it to perform real-world actions

## ▶️ How to Run

After completing the setup, launch the Jarvis agent with this simple command:

```bash
python agent.py console



## ▶Project Structure 
.
├── agent.py                  # Main entry point. Initializes and runs the agent.
├── Jarvis_prompts.py         # Defines the personality, instructions, and persona of Jarvis.
├── Jarvis_google_search.py   # Tool for Google Search and getting current date/time.
├── jarvis_get_whether.py     # Tool for fetching real-time weather.
├── Jarvis_news.py            # Tool for fetching the latest news headlines.
├── Jarvis_vision.py          # Tool for OCR screen reading ("AI Vision").
├── Jarvis_window_CTRL.py     # Tools for opening/closing apps and managing folders.
├── Jarvis_file_opner.py      # Tool for finding and opening specific files.
├── keyboard_mouse_CTRL.py    # All tools related to mouse and keyboard automation.
|── Jarvis_cricket.py         # (Future) Tool for fetching cricket scores.
├── .env                    # (You create this) Stores all your secret API keys.
├── requirements.txt        # Lists all Python dependencies for the project.
|── README.md                 # You are reading it!
