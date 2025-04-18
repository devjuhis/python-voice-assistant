import queue
import json
import sounddevice as sd
import pyautogui
import time
from vosk import Model, KaldiRecognizer

from functions.command import handle_command
from functions.ai import get_ai_response
from functions.ai_text_processor import process_voice_prompt
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
                print(f"🗣️ text before ai: {text}")
                processed_text = process_voice_prompt(text)
                if processed_text:

                    text_lower = processed_text.lower()

                    # mode switching
                    if "activate command mode" in text_lower or "command mode" in text_lower or "stop typing" in text_lower:
                        state.mode = "command"
                        speak("Command mode activated")
                        change_mode()
                        continue

                    elif "activate text mode" in text_lower or "text mode" in text_lower or "start typing" in text_lower:
                        state.mode = "text"
                        speak("Text mode activated")
                        change_mode()
                        continue

                    elif "intelligence mode" in text_lower or "ai mode" in text_lower or "start ai" in text_lower:
                        state.mode = "ai"
                        speak("ai mode activated")
                        change_mode()
                        continue

                    if state.mode == "text":

                        # special commands in text mode
                        if "delete all" in text_lower:
                            pyautogui.hotkey('ctrl', 'a')
                            pyautogui.hotkey('backspace')
                            speak("Deleting text")
                        elif "erase" in text_lower or "delete word" in text_lower: 
                            pyautogui.hotkey('ctrl', 'backspace')
                        elif "enter" in text_lower:
                            pyautogui.press("enter")
                        elif "stop listening" in text_lower:
                            from functions.play import toggle_listening
                            toggle_listening()
                            speak("Stopping listening")
                        else:
                            time.sleep(0.5)
                            pyautogui.write(processed_text, interval=0.08)

                    elif state.mode == "command":

                        handle_command(text_lower)
                    elif state.mode == "ai":
                        get_ai_response(processed_text)
