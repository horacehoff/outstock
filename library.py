from fileinput import filename
from tkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk
import json
from backend.download import retrieve_downloads
import datetime

def downloadFile(filename, timestamp):
    print(filename, timestamp)

root = ctk.CTk()

ico = Image.open('guiAssets/outstock.ico')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

label = ctk.CTkLabel(master=root, text="OutStock download page", font=("Arial", 25))
label.place(relx=0.5, y=15, anchor=CENTER)

for index,i in enumerate(retrieve_downloads()):
    if len(i[0])>=15:
        name = i[0][:12] + "..."
    else:
        name = i[0]

    timeStamp = datetime.datetime.fromtimestamp(int(i[1]) / 1000).strftime('%c')

    label = ctk.CTkLabel(master=root, text=name, font=("Arial", 15), bg_color="transparent")
    label.place(x=10, y=50 + index * 30, anchor=W)

    timeStampLabel = ctk.CTkLabel(master=root, text=timeStamp, font=("Arial", 15), bg_color="transparent")
    timeStampLabel.place(x=150, y=50 + index * 30, anchor=W)

    downloadButton = ctk.CTkButton(master=root, width=120, height=32, border_width=0, corner_radius=8, text="Download",
                                   command=lambda filename=name, creationDate=i[1]: downloadFile(filename, creationDate))
    downloadButton.place(x=400, y=50 + index * 30, anchor=E)


root.title("OutStocker - Library")
root.geometry("500x500")
root.resizable(False, False)

root.mainloop()