import threading
from functions.play import hotkey_listener
from ui.ui_components import app, status_label
from states.app_state import state

state.status_label = status_label

threading.Thread(target=hotkey_listener, daemon=True).start()

app.mainloop()
