from backend.bot import *
import threading

is_running = False
file = ""

if __name__ == "__main__":
    start_thread = threading.Thread(target=start)
    ui_thread = threading.Thread(target=ui)

    start_thread.start()
    import gui