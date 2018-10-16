import urllib.request
from urllib.error import URLError

FILENAME = 'latest.html'


class InkipediaCrawler(object):
    def __init__(self, base_url='https://splatoonwiki.org', file_name=FILENAME):
        self.base_url = base_url
        self.file_name = file_name

    def crawl_main_page(self):
        try:
            with urllib.request.urlopen(self.base_url) as request:
                with open(self.file_name, 'w') as f:
                    f.write(request.read().decode('utf-8'))
        except URLError as error:
            print('[URLError] {0}'.format(error))
            return False
        return True
