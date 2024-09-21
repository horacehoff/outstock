from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

from backend.webhook import upload_file


def fileSel():
    file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("All files", "*.*")])
    if file_path:
        upload_file(file_path)
        buttonTest.config(text=f"Selected File: {file_path}")
        return file_path

root = Tk()
root.wm_title("Outstock")

ico = Image.open('guiAssets/outstock.ico')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)


label = Label(root, text="Hello World")
buttonTest = Button(root, text="Choose File", command=fileSel)

buttonTest.pack()
label.pack()

root.mainloop()