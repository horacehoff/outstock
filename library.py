from tkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk
import json
from backend.download import retrieve_downloads

root = ctk.CTk()

ico = Image.open('guiAssets/outstock.ico')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

label = ctk.CTkLabel(master=root, text="OutStock download page", font=("Arial", 25))
label.place(relx=0.5, y=15, anchor=CENTER)

print(retrieve_downloads())



root.title("OutStocker - Library")
root.geometry("500x500")
root.resizable(False, False)

root.mainloop()