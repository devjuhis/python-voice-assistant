import threading
import keyboard
import pygame

from states.app_state import state
from functions.audio import listen_microphone

pygame.mixer.init()

def play_sound(filename):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

def toggle_listening():
    if not state.listening:
        state.listening = True
        if state.status_label:
            state.status_label.configure(text="Listening 🎙️")
        play_sound("sounds/on.mp3")
        threading.Thread(target=listen_microphone, daemon=True).start()
    else:
        state.listening = False
        if state.status_label:
            state.status_label.configure(text="Paused ⏸️, start again with Ctrl + Alt + R")
        play_sound("sounds/off.mp3")

def hotkey_listener():
    while True:
        keyboard.wait("ctrl+alt+r")
        toggle_listening()
