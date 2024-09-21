import json
import requests
from tqdm import tqdm
import os


def download(url: str, fname: str, chunk_size=1024, total_files=10):
    resp = requests.get(url, stream=True)
    total = int(resp.headers.get('content-length', 0))
    with open(fname, 'wb') as file, tqdm(
        desc=fname+f"/ {total_files}",
        total=total,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in resp.iter_content(chunk_size=chunk_size):
            size = file.write(data)
            bar.update(size)


history = {}
with open("history", "r") as f:
    try:
        history = json.loads(f.read())
    except:
        print("Please first upload some files!")


# for x in list(history.keys()):
print(history[list(history.keys())[0]][0])
# download(history[list(history.keys())[0]][0], fname="fragment0")






from tkinter.filedialog import asksaveasfile
def save_file():
    f = asksaveasfile(initialfile='Untitled.txt',
                      defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
save_file()
