# TypeFlow 🗣️➡️⌨️  
TypeFlow is a simple speech-to-text automation tool for Windows. It listens to your voice and types out what you say — directly into any text input field. This is useful for fast note-taking, hands-free writing, or accessibility purposes.

## 🚀 Features
- Converts spoken words to typed text in real-time
- Automatically presses Enter after each transcription
- Uses a global hotkey (e.g., `Ctrl + Alt + R`) to toggle listening
- Includes a minimalistic UI built with `customtkinter`
- Starts automatically when Windows boots

## 🧰 Tech Stack
- **Python 3.12**
- [Vosk](https://alphacephei.com/vosk/) for offline speech recognition
- `pyautogui` for keyboard control
- `sounddevice` for microphone input
- `customtkinter` for the GUI
- Optional: Script integration for Windows autostart

## 💻 How to Use

1. **Clone the project** and navigate to the folder.
2. **Install the requirements** inside a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
3. **Run the Script**
   ```bash
   python autowriter.py
5. **Start and stop recording**
   - Ctrl+Alt+r


