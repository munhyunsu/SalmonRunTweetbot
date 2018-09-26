import datetime

from discord_key import client_id, client_secret, client_token
from file_handler import FileHandler

import discord
from discord.ext import commands
import asyncio
from get_spread import get_meme_dict

DESC = '''SalmonRun Reminder KR
'''
MEME = get_meme_dict()
MEME_TIME = datetime.datetime.now()


def main():
    bot = commands.Bot(command_prefix='$',
                       case_insensitive=True,
                       description=DESC)
    file_handler = FileHandler()

    @bot.event
    async def on_ready():
        print('Logged in as')
        print(bot.user.name)
        print(bot.user.id)
        print('------')

    @bot.command(name='salmonrun',
                 aliases=['연어런', '연어'])
    async def salmonrun(ctx, *args):
        """SalmonRunKR의 최신 트윗을 가져옵니다.
        """
        await ctx.send(file_handler.read())

    @bot.command(name='meme',
                 aliases=['짤'])
    async def meme(ctx, *args):
        """짤을 호출합니다(URL).
        """
        now = datetime.datetime.now()
        until_update = (now-MEME_TIME).total_seconds()
        if until_update >= 3600:
            global MEME, MEME_TIME
            MEME = get_meme_dict()
            MEME_TIME = now
        if len(args) < 1:
            await ctx.send('현재 짤이 {0}개 있습니다.'.format(len(MEME)))
        else:
            called_meme = args[0]
            called_meme_url = MEME.get(called_meme, None)
            if called_meme_url is None:
                await ctx.send('검색된 짤이 없습니다.')
            else:
                await ctx.send(called_meme_url)

    bot.run(client_token)


if __name__ == '__main__':
    main()