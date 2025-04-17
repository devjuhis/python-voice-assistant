import subprocess
import pyautogui
from functions.speak import speak 

def handle_command(text):
    from functions.play import toggle_listening
    print(f"🧠 Command received: {text}")
    text = text.lower()

    # Chrome
    if "open chrome" in text:
        subprocess.Popen("start chrome", shell=True)
        speak("Opening Chrome")
    elif "close chrome" in text:
        subprocess.Popen("taskkill /F /IM chrome.exe", shell=True)
        speak("Closing Chrome")

    # Notepad
    elif "open notepad" in text or "open notebook" in text:
        subprocess.Popen("notepad.exe", shell=True)
        speak("Opening Notepad")
    elif "close notepad" in text or "close notebook" in text:
        subprocess.Popen("taskkill /F /IM notepad.exe", shell=True)
        speak("Closing Notepad")
    
    # VS Code
    elif "open vs code" in text or "open visual studio code" in text:
        subprocess.Popen("code", shell=True)
        speak("Opening Visual Studio Code")
        
    elif "close vs code" in text or "close visual studio code" in text:
        subprocess.Popen("taskkill /F /IM Code.exe", shell=True)
        speak("Closing Visual Studio Code")

    # CMD
    elif "open command prompt" in text or "open cmd" in text:
        subprocess.Popen("cmd.exe /K cd C:\\", shell=True)
        speak("Opening Command Prompt")
    elif "close command prompt" in text or "close cmd" in text:
        subprocess.Popen("taskkill /F /IM cmd.exe", shell=True)
        speak("Closing Command Prompt")

    # Calculator
    elif "open calculator" in text:
        subprocess.Popen("calc.exe", shell=True)
        speak("Opening Calculator")
    elif "close calculator" in text:
        subprocess.Popen("taskkill /F /IM calc.exe", shell=True)
        speak("Closing Calculator")

    # Paint
    elif "open paint" in text:
        subprocess.Popen("mspaint.exe", shell=True)
        speak("Opening Paint")
    elif "close paint" in text:
        subprocess.Popen("taskkill /F /IM mspaint.exe", shell=True)
        speak("Closing Paint")

    # Close tab
    elif "close tab" in text:
        pyautogui.hotkey("ctrl", "f4")
        speak("Closing current tab")

    # Stop listening
    elif "stop listening" in text:
        toggle_listening()
        speak("Voice control stopped")
    
    # Thanks
    elif "thank you" in text or "thanks" in text:
        speak("You're welcome!")

    else:
        speak("Sorry, can you repeat that?")
