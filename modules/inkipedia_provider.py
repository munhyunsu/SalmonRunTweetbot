import json

FILENAME = 'latest_inkipedia_locale.json'


class InkipediaProvider(object):
    def __init__(self, file_name=FILENAME):
        with open(file_name, 'r') as f:
            self.data = json.load(f)

    def get_regular(self, ctx, args=()):
        string = ('[Regular Battle]\n'
                  '{time}, {rule}\n'
                  '{stage1}, {stage2}\n').format_map(self.data['Regular Battle'][0])
        string = string + ('{time}, {rule}\n'
                           '{stage1}, {stage2}\n').format_map(self.data['Regular Battle'][1])
        return string

    def get_ranked(self, ctx, args=()):
        string = ('[Ranked Battle]\n'
                  '{time}, {rule}\n'
                  '{stage1}, {stage2}\n').format_map(self.data['Ranked Battle'][0])
        string = string + ('{time}, {rule}\n'
                           '{stage1}, {stage2}\n').format_map(self.data['Ranked Battle'][1])
        return string

    def get_league(self, ctx, args=()):
        string = ('[League Battle]\n'
                  '{time}, {rule}\n'
                  '{stage1}, {stage2}\n').format_map(self.data['League Battle'][0])
        string = string + ('{time}, {rule}\n'
                           '{stage1}, {stage2}\n').format_map(self.data['League Battle'][1])
        return string
