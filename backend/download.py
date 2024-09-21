import json
import requests
from tqdm import tqdm
import os

from backend.converter import fragments_to_file


def download(url: str, fname: str, chunk_size=1024, total_files=10):
    resp = requests.get(url, stream=True)
    total = int(resp.headers.get('content-length', 0))
    with open("temp/"+fname, 'wb') as file, tqdm(
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

# print(list(history.keys()))

def download_file(filename):
    if not os.path.exists("temp/"):
        os.makedirs("temp/")
    i = 0
    for url in history[filename]:
        download(url, "fragment"+str(i+1), total_files=len(history[filename]))
        i += 1

# download_file("sample.zip-**-1726915693322")
fragments_to_file("temp/")


# for x in list(history.keys()):
# download(history[list(history.keys())[0]][0], fname="fragment0")






from tkinter.filedialog import asksaveasfile
def save_file():
    f = asksaveasfile(initialfile='Untitled.txt',
                      defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
# save_file()
