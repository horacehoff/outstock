from tkinter import *
from tkinter import filedialog
from types import NoneType
import customtkinter as ctk
from PIL import Image, ImageTk
from library import library
from threading import Thread
from backend.webhook import upload_file, get_number_of_files, increase_current_step

total_files = 0

def update_loading_bar(current_step, total_files):
    while current_step < total_files:
        if total_files != 0:
            current_step = increase_current_step(False)
        total_files = get_number_of_files(0, False)
        download_label.configure(text=str(current_step + 1) + "/" + str(total_files))
    loading_bar.destroy()


def thread_file_sel():
    global total_files
    file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("All files", "*.*")])
    if file_path:
        Thread(target=lambda path=file_path: upload_file(path), daemon=False).start()
    else:
        return

    global loading_bar
    loading_bar = Toplevel()
    loading_bar.title("OutStock - Uploading...")
    loading_bar.geometry("500x100")
    loading_bar.resizable(False, False)
    loading_bar.configure(bg="white")

    global sending_text_label
    sending_text_label = Label(loading_bar, text="SENDING...", font=("Geneva", 18), bg="white")
    sending_text_label.place(relx=0.5, y=15, anchor=CENTER)

    current_step = -5
    global download_label
    download_label = Label(loading_bar, text="0/" + str(total_files), font=("Arial", 18), bg="white")
    download_label.place(relx=0.5, rely=0.5, anchor=CENTER)

    while get_number_of_files(0, False) == NoneType:
        total_files = 0
    total_files = get_number_of_files(0, False)

    Thread(target=lambda step=current_step, tot_files=total_files: update_loading_bar(step, tot_files),
           daemon=False).start()


def help_page_launch():
    help_page = Toplevel()
    help_page.title("Help")
    help_page.geometry("350x90")
    help_page.resizable(False, False)
    help_page.config(bg="white")

    help_label = Label(help_page, text="Welcome to OutStock", font=("Arial", 18), bg="white")
    help_label.pack()

    help_label2 = Label(help_page, text="\n"
                                        "This tool is used to save your files on the discord servers.\n"
                                        "It fragments your file in smaller ones that can be sent on discord, and\n"
                                        "refragments them when you want to download your file back.\n", font=("Arial", 11), bg="white")
    help_label2.pack()


root = ctk.CTk()

ico = Image.open('guiAssets/outstock.ico')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)
root.configure(fg_color="#fff")
root.resizable(False, False)

titleBar = Frame(root, bg='#fff')
titleBar.pack(fill=X)

header_label = ctk.CTkLabel(master=root, text="OutStock", font=("Geneva", 25, "bold"),
                            text_color="#000")
header_label.place(relx=0.5, y=25, anchor=CENTER)

helpButton = ctk.CTkButton(master=root, width=50, height=32, border_width=0, corner_radius=4, text="Help",
                           command=help_page_launch, fg_color="#0033ff", hover_color="#0C0E1B")
helpButton.place(x=100, y=140, anchor=CENTER)

libraryPage = ctk.CTkButton(master=root, width=70, height=32, border_width=0, corner_radius=2, text="Library",
                            command=library, fg_color="#0033ff", hover_color="#0C0E1B", )
libraryPage.place(x=170, y=140, anchor=CENTER)

fileSelector = ctk.CTkButton(master=root, width=200, height=50, border_width=0, corner_radius=2, text="Upload a file",
                             command=thread_file_sel, fg_color="#0033ff", hover_color="#0C0E1B",
                             font=("Arial", 20, "bold"))
fileSelector.place(relx=0.5, y=80, anchor=CENTER)

root.title("OutStock")
root.geometry("275x175")

root.mainloop()
