import threading
import keyboard

from states.app_state import state
from functions.audio import listen_microphone

def toggle_listening():
    if not state.listening:
        state.listening = True
        if state.status_label:
            state.status_label.configure(text="Listening 🎙️")
        threading.Thread(target=listen_microphone, daemon=True).start()
    else:
        state.listening = False
        if state.status_label:
            state.status_label.configure(text="Paused ⏸️, start again with Ctrl + Alt + R")

def hotkey_listener():
    while True:
        keyboard.wait("ctrl+alt+r")
        print("hotkey pressed")
        toggle_listening()
