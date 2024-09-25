from tkinter import *
from tkinter import filedialog
import customtkinter as ctk
from PIL import Image, ImageTk
from library import library
from threading import Thread

from backend.webhook import upload_file


def file_sel():
    global libraryPage
    file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("All files", "*.*")])
    if file_path:
        thread = Thread(target=lambda lambda_file_path = file_path: upload_file(lambda_file_path), daemon=False)
        libraryPage.configure(state=DISABLED, fg_color="grey")
        thread.start()
        return file_path

def help_page_launch():
    help_page = Toplevel()
    help_page.title("Help")
    help_page.geometry("500x350")
    help_page.resizable(False, False)
    help_page.config(bg="white")

    help_label = Label(help_page, text="Welcome to OutStock", font=("Arial", 18), bg="white")
    help_label.pack()

    help_label2 = Label(help_page, text="", font=("Arial", 12), bg="white")
    help_label2.pack()

    help_label3 = Label(help_page, text="This tool is used to save your files on the discord servers.", font=("Arial", 12), bg="white")
    help_label3.pack()

    help_label4 = Label(help_page, text="Our technology takes your file, breaks it down in sendable packets and then", font=("Arial", 12), bg="white")
    help_label4.pack()

    help_label5 = Label(help_page, text="refragments them when needed", font=("Arial", 12), bg="white")
    help_label5.pack()

    help_label6 = Label(help_page, text="", font=("Arial", 12), bg="white")
    help_label6.pack()

    help_label7 = Label(help_page, text="To use our app select a file with the button on the main page and wait to get the message:", font=("Arial", 12), bg="white")
    help_label7.pack()

    help_label8 = Label(help_page, text="\"SUCCESSFULLY DOWNLOADED {filename}!\"", font=("Arial", 12), bg="white")
    help_label8.pack()

    help_label9 = Label(help_page, text="\nTo retrieve the file go in your library click download and wait to get the message:", font=("Arial", 12), bg="white")
    help_label9.pack()

    help_label10 = Label(help_page, text="\"SENT {filename} SUCCESSFULLY!\"", font=("Arial", 12), bg="white")
    help_label10.pack()


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

helpButton = ctk.CTkButton(master=root, width=50, height=15, border_width=0, corner_radius=8, text="Help ?", command=help_page_launch, fg_color="#1ABC9C", hover_color="#F39C12")
helpButton.place(x=5, y=5, anchor=NW)

libraryPage = ctk.CTkButton(master=root, width=120, height=32, border_width=0, corner_radius=8, text="Go to library page", command=library, fg_color="#1ABC9C", hover_color="#F39C12",  )
libraryPage.place(relx=0.5, y=300, anchor=CENTER)

fileSelector = ctk.CTkButton(master=root, width=400, height=200, border_width=0, corner_radius=8, text="Select File", command=file_sel, fg_color="#1ABC9C", hover_color="#F39C12", font=("Arial", 70, "bold"))
fileSelector.place(relx=0.5, y=150, anchor=CENTER)

root.title("OutStocker - Sending")
root.geometry("500x350")



root.mainloop()