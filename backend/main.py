from wandb.docker import shell

from bot import *
import time
import threading
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import subprocess
import os

is_running = False
file = ""

if __name__ == "__main__":
    def ui():
        pass

    start_thread = threading.Thread(target=start)
    ui_thread = threading.Thread(target=ui)

    start_thread.start()
    ui_thread.start()

    start_thread.join()
    ui_thread.join()

