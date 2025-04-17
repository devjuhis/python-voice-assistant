import queue
import json
import sounddevice as sd
import pyautogui
from vosk import Model, KaldiRecognizer

from functions.command import handle_command
from functions.ai import get_ai_response
from states.app_state import state
from ui.ui_components import change_mode
from functions.speak import speak

q = queue.Queue()
model = Model("C:/projects/typeflow/vosk-model-en-us-s")
recognizer = KaldiRecognizer(model, 16000)

def callback(indata, frames, time, status):
    q.put(bytes(indata))

def listen_microphone():
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        while state.listening:
            data = q.get()
            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                result_dict = json.loads(result)
                text = result_dict.get("text", "")
                if text:
                    text = text.lower()
                    print(f"🗣️ Heard: {text}")

                    # mode switching
                    if "activate command mode" in text:
                        state.mode = "command"
                        speak("Command mode activated")
                        change_mode()
                        continue

                    elif "activate text mode" in text:
                        state.mode = "text"
                        speak("Text mode activated")
                        change_mode()
                        continue

                    elif "activate intelligence mode" in text:
                        state.mode = "ai"
                        speak("ai mode activated")
                        change_mode()
                        continue

                    if state.mode == "text":
                        pyautogui.write(text, interval=0.05)
                        pyautogui.press("enter")
                    elif state.mode == "command":
                        handle_command(text)
                    elif state.mode == "ai":
                        get_ai_response(text)
