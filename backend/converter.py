def read_in_chunks(file_object, chunk_size=9900000):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data


file_path = "../sample.zip"

messages = []
with open(file_path, 'rb') as f:
    for piece in read_in_chunks(f):
        messages.append(piece)

print(len(messages))

with open("test","wb") as f:
    f.write(messages[0])
    f.close()