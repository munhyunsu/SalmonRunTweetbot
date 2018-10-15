from discord.ext import commands

from get_spread import get_meme_dict, get_translate_dict
from modules.file_reader import FileReader
from modules.meme_loader import MemeLoader
from modules.random_selector import RandomSelector

MEME = get_meme_dict()
(WP_EN_JP, WP_EN_KO, ST_EN_JP, ST_EN_KO) = get_translate_dict()
FILENAME = 'latest_url'


class SalmonrunCommands(object):
    def __init__(self):
        self.file_reader = FileReader('latest_url')
        self.meme_loader = MemeLoader(MEME)
        self.random_selector = RandomSelector(list(WP_EN_JP.keys()),
                                              WP_EN_JP,
                                              WP_EN_KO)

    @commands.command(name='salmonrun',
                      aliases=['연어런', '연어'])
    async def salmonrun(self, ctx, *args):
        """SalmonRunKR의 최신 트윗을 가져옵니다."""
        await ctx.send(self.file_reader.get_file_content(ctx, args))

    @commands.command(name='meme',
                      aliases=['짤'])
    async def meme(self, ctx, *args):
        """짤을 호출합니다(URL)."""
        await ctx.send(self.meme_loader.get_meme(ctx, args))

    @commands.command(name='weapon',
                      aliases=['무기'])
    async def weapon(self, ctx, *args):
        """무작위 무기를 호출합니다."""
        await ctx.send(self.random_selector.get_random(ctx, args))


def setup(bot):
    bot.add_cog(SalmonrunCommands())
