class MemeLoader(object):
    def __init__(self, memes):
        self.memes = memes

    def get_meme(self, ctx, args=()):
        if len(args) < 1:
            return '현재 짤이 {0}개 있습니다.'.format(len(self.memes))
        else:
            called_meme = args[0]
            called_meme_url = self.memes.get(called_meme, None)
            if called_meme_url is None:
                return '검색된 짤이 없습니다.'
            else:
                return called_meme_url
