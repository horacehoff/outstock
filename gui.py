from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
from library import library

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
    help.geometry("500x350")
    help.resizable(False, False)
    help.config(bg="white")

    helpLabel = Label(help, text="Welcome to OutStock", font=("Arial", 18), bg="white")
    helpLabel.pack()

    helpLabel2 = Label(help, text="", font=("Arial", 12), bg="white")
    helpLabel2.pack()

    helpLabel3 = Label(help, text="This tool is used to save your files on the discord servers.", font=("Arial", 12), bg="white")
    helpLabel3.pack()

    helpLabel4 = Label(help, text="Our technology takes your file, breaks it down in sendable packets and then", font=("Arial", 12), bg="white")
    helpLabel4.pack()

    helpLabel5 = Label(help, text="refragments them when needed", font=("Arial", 12), bg="white")
    helpLabel5.pack()

    helpLabel6 = Label(help, text="", font=("Arial", 12), bg="white")
    helpLabel6.pack()

    helpLabel7 = Label(help, text="To use our app select a file with the button on the main page and wait to get the message:", font=("Arial", 12), bg="white")
    helpLabel7.pack()

    helpLabel8 = Label(help, text="\"SUCCESSFULLY DOWNLOADED {filename}!\"", font=("Arial", 12), bg="white")
    helpLabel8.pack()

    helpLabel9 = Label(help, text="\nTo retrieve the file go in your library click download and wait to get the message:", font=("Arial", 12), bg="white")
    helpLabel9.pack()

    helpLabel10 = Label(help, text="\"SENT {filename} SUCCESSFULLY!\"", font=("Arial", 12), bg="white")
    helpLabel10.pack()



root = ctk.CTk()

ico = Image.open('guiAssets/outstock.ico')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)
root.configure(fg_color="#2C3E50" )
root.resizable(False, False)

titleBar = Frame(root, bg='#2C3E50')
titleBar.pack(fill=X)

header_label = ctk.CTkLabel(master=root, text="OutStock export page", font=("Arial", 25, "bold"),
                            text_color="#D35400")
header_label.place(relx=0.5, y=15, anchor=CENTER)  # Add to grid with a colspan for centering

help = ctk.CTkButton(master=root, width=50, height=15, border_width=0, corner_radius=8, text="Help ?", command=help, fg_color="#1ABC9C", hover_color="#F39C12")
help.place(x=5, y=5, anchor=NW)

libraryPage = ctk.CTkButton(master=root, width=120, height=32, border_width=0, corner_radius=8, text="Go to library page", command=library, fg_color="#1ABC9C", hover_color="#F39C12")
libraryPage.place(relx=0.5, y=300, anchor=CENTER)

fileSelector = ctk.CTkButton(master=root, width=400, height=200, border_width=0, corner_radius=8, text="Select File", command=fileSel, fg_color="#1ABC9C", hover_color="#F39C12", font=("Arial", 70, "bold"))
fileSelector.place(relx=0.5, y=150, anchor=CENTER)

root.title("OutStocker - Sending")
root.geometry("500x350")




root.mainloop()