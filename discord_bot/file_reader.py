class FileReader(object):
    def __init__(self, file_path):
        self.file_path = file_path

    def get_file_content(self, ctx, args=()):
        with open(self.file_path, 'r') as f:
            return f.read()
