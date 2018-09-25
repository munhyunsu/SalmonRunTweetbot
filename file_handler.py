FILENAME = 'latest_url'


class FileHandler(object):
    def __init__(self, file_name=FILENAME):
        self.file_name = file_name

    def write(self, txt):
        with open(self.file_name, 'w') as f:
            f.write(txt)

    def read(self):
        with open(self.file_name, 'r') as f:
            return f.read()


def main():
    file_handler = FileHandler()
    file_handler.write('https://twitter.com/SalmonRunKR/status/1044375970151428097')
    print(file_handler.read())


if __name__ == '__main__':
    main()