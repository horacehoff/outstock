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