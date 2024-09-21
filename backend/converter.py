import os

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
    for x in fragments:
        with open("temp/fragment"+str(x),"rb") as f:
            total += f.read()

    with open("test.zip","wb") as f:
        f.write(total)
    print(fragments)

fragments_to_file("temp/")