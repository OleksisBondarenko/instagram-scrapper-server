   
def read_data_from_file(path=HTML_PATH, mode='r', encoding=ENCODING_FILE):
    with open(path, mode, encoding=encoding) as file:
        return file.read()


def write_data_to_file(data, path=HTML_PATH, mode="w", encoding=ENCODING_FILE):
    with open(path, mode , encoding=encoding) as file:
        file.write(data)
