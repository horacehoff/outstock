def file_to_messages(filepath):
    def read_in_chunks(file_object, chunk_size=10450000):
        while True:
            data = file_object.read(chunk_size)
            if not data:
                break
            yield data


    messages = []
    with open(filepath, 'rb') as f:
        for piece in read_in_chunks(f):
            messages.append(piece)

    return messages