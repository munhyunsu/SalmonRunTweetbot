from discord.ext import commands

from gspread_handler.modules.gspread_handler import GSpreadHandler
from discord_bot.file_reader import FileReader
from discord_bot.meme_loader import MemeLoader
from discord_bot.random_selector import RandomSelector
from discord_bot.inkipedia_provider import InkipediaProvider

FILENAME = 'latest_url'


class SplatoonCommands(object):
    def __init__(self):
        gspread = GSpreadHandler('private/Gspread-39d43309c65c.json')
        (wp_en_jp, wp_en_ko, st_en_jp, st_en_ko) = gspread.get_translate_dict()
        meme = gspread.get_meme_dict()
        self.file_reader = FileReader(FILENAME)
        self.meme_loader = MemeLoader(meme)

        self.random_selector = RandomSelector(list(wp_en_jp.keys()),
                                              wp_en_jp,
                                              wp_en_ko)
        self.inkipedia = InkipediaProvider()

    @commands.command(name='salmonrun',
                      aliases=['salmon', '연어런', '연어'])
    async def salmonrun(self, ctx, *args):
        """연어런 알림 봇의 최신 트윗을 가져옵니다. '!연어'"""
        await ctx.send(self.file_reader.get_file_content(ctx, args))

    @commands.command(name='meme',
                      aliases=['짤'])
    async def meme(self, ctx, *args):
        """짤방을 무작위로 호출합니다. '!짤'"""
        await ctx.send(self.meme_loader.get_meme(ctx, args))

    @commands.command(name='weapon',
                      aliases=['무기'])
    async def weapon(self, ctx, *args):
        """무작위 무기를 호출합니다. '!무기'"""
        await ctx.send(self.random_selector.get_random(ctx, args))

    @commands.command(name='regular',
                      aliases=['일반', '나와바리'])
    async def regular(self, ctx, *args):
        """레귤러/나와바리 배틀 스테이지를 확인합니다. '![나와바리or일반]'"""
        await ctx.send(self.inkipedia.get_regular(ctx, args))

    @commands.command(name='ranked',
                      aliases=['랭크'])
    async def ranked(self, ctx, *args):
        """랭크 배틀 스테이지를 확인합니다. '!랭크'"""
        await ctx.send(self.inkipedia.get_ranked(ctx, args))

    @commands.command(name='league',
                      aliases=['리그'])
    async def league(self, ctx, *args):
        """리그 배틀 스테이지를 확인합니다. '!리그'"""
        await ctx.send(self.inkipedia.get_league(ctx, args))


def setup(bot):
    bot.add_cog(SplatoonCommands())
