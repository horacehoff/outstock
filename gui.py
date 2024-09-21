from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

def fileSel():
    file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("All files", "*.*")])
    if file_path:
        with open("threads", "w") as g:
            g.write(file_path)
            g.close()
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