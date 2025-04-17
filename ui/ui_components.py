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
else:
    mode_var = ctk.IntVar(value=2)

def mode_radio_changed():
    from states.app_state import state
    print("mode changed to", state.mode)
    if state.mode == "text":
        mode_var.set(1)
        if state.status_label:
            state.status_label.configure(text="Text Mode ✍️")
    elif state.mode == "command":
        mode_var.set(2)
        if state.status_label:
            state.status_label.configure(text="Command Mode 🧠")

text_radio = ctk.CTkRadioButton(app, text="Text Mode ✍️", variable=mode_var, value=1, command=mode_radio_changed)
text_radio.pack(pady=5)

command_radio = ctk.CTkRadioButton(app, text="Command Mode 🧠", variable=mode_var, value=2, command=mode_radio_changed)
command_radio.pack(pady=5)
