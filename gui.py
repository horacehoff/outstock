from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk

from backend.webhook import upload_file


def fileSel():
    file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("All files", "*.*")])
    if file_path:
        upload_file(file_path)
        fileSelector.config(text=f"Selected File: {file_path}")
        return file_path

def help():
    help = Toplevel()
    help.title("Help")
    help.geometry("500x200")
    help.resizable(False, False)
    help.config(bg="white")

    helpLabel = Label(help, text="Welcome to OutStock", font=("Arial", 12), bg="white")
    helpLabel.pack()

    helpLabel2 = Label(help, text="", font=("Arial", 12), bg="white")
    helpLabel2.pack()

    helpLabel3 = Label(help, text="This tool is used to save your files on the discord servers.", font=("Arial", 12), bg="white")
    helpLabel3.pack()

    helpLabel4 = Label(help, text="Our technology takes your file, breaks it down in sendable packets and then", font=("Arial", 12), bg="white")
    helpLabel4.pack()

    helpLabel5 = Label(help, text="recompiles them when needed", font=("Arial", 12), bg="white")
    helpLabel5.pack()

    helpLabel6 = Label(help, text="", font=("Arial", 12), bg="white")
    helpLabel6.pack()

    helpLabel7 = Label(help, text="", font=("Arial", 12), bg="white")
    helpLabel7.pack()

    helpLabel8 = Label(help, text="", font=("Arial", 12), bg="white")
    helpLabel8.pack()

    helpLabel9 = Label(help, text="", font=("Arial", 12), bg="white")
    helpLabel9.pack()

root = ctk.CTk()

ico = Image.open('guiAssets/outstock.ico')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

help = ctk.CTkButton(master=root, width=120, height=32, border_width=0, corner_radius=8, text="Help ?", command=help)
help.place(x=0.5, y=0.5, anchor=NW)

fileSelector = ctk.CTkButton(master=root, width=120, height=32, border_width=0, corner_radius=8, text="Select File", command=fileSel)
fileSelector.place(relx=0.5, rely=0.5, anchor=CENTER)

root.title("OutStocker - Sending")
root.geometry("500x500")




root.mainloop()