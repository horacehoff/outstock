import json


history = {}
with open("history", "r") as f:
    try:
        history = json.loads(f.read())
    except:
        print("Please first upload some files!")






from tkinter.filedialog import asksaveasfile
def save_file():
    f = asksaveasfile(initialfile='Untitled.txt',
                      defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
# save_file()
