import customtkinter as ctk

from states.app_state import state

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("TypeFlow")
app.geometry("400x250")

title_label = ctk.CTkLabel(app, text="TypeFlow", font=("Arial", 20))
title_label.pack(pady=15)

status_label = ctk.CTkLabel(app, text="Press Ctrl + Alt + R to start ▶️", font=("Arial", 14))
status_label.pack(pady=10)

if (state.mode == "text"):
    mode_var = ctk.IntVar(value=1)
elif (state.mode == "command"):
    mode_var = ctk.IntVar(value=2)
elif (state.mode == "ai"):
    mode_var = ctk.IntVar(value=3)

def change_mode():
    if state.mode == "text":
        mode_var.set(1)
    elif state.mode == "command":
        mode_var.set(2)
    elif state.mode == "ai":    
        mode_var.set(3)
    mode_radio_changed()

def mode_radio_changed():
    if mode_var.get() == 1:
        state.mode = "text"
    elif mode_var.get() == 2:
        state.mode = "command"
    elif mode_var.get() == 3:
        state.mode = "ai"

text_radio = ctk.CTkRadioButton(app, text="Text Mode ✍️", variable=mode_var, value=1, command=mode_radio_changed)
text_radio.pack(pady=5)

command_radio = ctk.CTkRadioButton(app, text="Command Mode 🧠", variable=mode_var, value=2, command=mode_radio_changed)
command_radio.pack(pady=5)

ai_radio = ctk.CTkRadioButton(app, text="AI Mode 🤖", variable=mode_var, value=3, command=mode_radio_changed)
ai_radio.pack(pady=5)
