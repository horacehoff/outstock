import os
from tkinter.filedialog import asksaveasfile


def file_to_messages(filepath):
    # https://stackoverflow.com/a/519653
    def chunks(file):
        while True:
            data = file.read(10450000)
            if not data:
                break
            yield data

    messages = []
    with open(filepath, 'rb') as f:
        for piece in chunks(f):
            messages.append(piece)

    return messages

def fragments_to_file(folder, filename):
    fragments = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    fragments = sorted([int(f.replace("fragment","")) for f in fragments])
    total = b""
    print("GROUPING FRAGMENTS...")
    i = 0
    for x in fragments:
        i += 1
        with open("temp/fragment"+str(x),"rb") as f:
            total += f.read()
        print(f"{i} / {len(fragments)}")
    print(str(os.path.splitext(filename)[1]))
    file_path = asksaveasfile(initialfile=filename,
                      defaultextension=str(os.path.splitext(filename)[1]), filetypes=[("All Files", "*.*")])
    print(f)
    with open(file_path.name,"wb") as f:
        f.write(total)