import json
import requests
from tqdm import tqdm
import os
from shutil import rmtree
from backend.converter import fragments_to_file

# https://gist.github.com/yanqd0/c13ed29e29432e3cf3e7c38467f42f51
def download(url: str, fname: str, chunk_size=1024, total_files=10):
    resp = requests.get(url, stream=True)
    total = int(resp.headers.get('content-length', 0))
    with open("temp/" + fname, 'wb') as file, tqdm(
            desc=fname.replace("fragment", "fragment ") + f"/{total_files}",
            total=total,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
    ) as bar:
        for data in resp.iter_content(chunk_size=chunk_size):
            size = file.write(data)
            bar.update(size)

history = {}
with open("./history", "r") as f:
    try:
        history = json.loads(f.read())
    except:
        print("Please first upload some files!")

def download_file(filename):
    if not os.path.exists("temp/"):
        os.makedirs("temp/")
    i = 0
    for url in history[filename]:
        download(url, "fragment" + str(i + 1), total_files=len(history[filename]))
        i += 1
    fragments_to_file("temp/", filename.split("-**-")[0])
    rmtree("temp/")


def retrieve_downloads():
    return [(x.split("-**-")[0], x.split("-**-")[1]) for x in list(history.keys())]