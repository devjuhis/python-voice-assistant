import customtkinter as ctk
import pyautogui
import sounddevice as sd
import queue
import json
import threading
import keyboard
from vosk import Model, KaldiRecognizer

q = queue.Queue()

model = Model("C:/projects/typeflow/vosk-model-en-us-s")
recognizer = KaldiRecognizer(model, 16000)

listening = False

def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))

def listen_microphone():
    global listening
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        while listening:
            data = q.get()
            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                result_dict = json.loads(result)
                text = result_dict.get("text", "")
                if text:
                    print(f"Kirjoitetaan: {text}")
                    pyautogui.write(text, interval=0.05)
                    pyautogui.press("enter")

def toggle_listening():
    global listening
    if not listening:
        listening = True
        status_label.configure(text="Listening 🎙️")
        threading.Thread(target=listen_microphone, daemon=True).start()
    else:
        listening = False
        status_label.configure(text="Paused ⏸️, start again with Ctrl + Alt + r")

def hotkey_listener():
    while True:
        keyboard.wait("ctrl+alt+r")
        toggle_listening()

threading.Thread(target=hotkey_listener, daemon=True).start()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("TypeFlow")
app.geometry("400x200")

title_label = ctk.CTkLabel(app, text="TypeFlow", font=("Arial", 20))
title_label.pack(pady=20)

status_label = ctk.CTkLabel(app, text="Press Ctrl + Alt + R to start ▶️", font=("Arial", 14))
status_label.pack(pady=10)

app.mainloop()
