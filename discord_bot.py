import datetime
import random

from discord_key import client_id, client_secret, client_token
from file_handler import FileHandler

import discord
from discord.ext import commands
import asyncio
from get_spread import get_meme_dict, get_translate_dict

DESC = '''SalmonRun Reminder KR
'''
MEME = get_meme_dict()
MEME_TIME = datetime.datetime.now()
(WP_EN_JP, WP_EN_KO, ST_EN_JP, ST_EN_KO) = get_translate_dict()
WEAPON_TIME = datetime.datetime.now()


def main():
    bot = commands.Bot(command_prefix='$',
                       case_insensitive=True,
                       description=DESC)
    file_handler = FileHandler()
    kbb_entry = dict()

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
        # global MEME, MEME_TIME
        # now = datetime.datetime.now()
        # until_update = (now-MEME_TIME).total_seconds()
        # if until_update >= 60*60:
        #     MEME = get_meme_dict()
        #     MEME_TIME = now
        if len(args) < 1:
            await ctx.send('현재 짤이 {0}개 있습니다.'.format(len(MEME)))
        else:
            called_meme = args[0]
            called_meme_url = MEME.get(called_meme, None)
            if called_meme_url is None:
                rand = random.randint(1, 10)
                if rand == 10:
                    await ctx.send('아, 쫌! 없다구요.')
                else:
                    await ctx.send('검색된 짤이 없습니다.')
            else:
                await ctx.send(called_meme_url)

    @bot.command(name='weapon',
                 aliases=['무기'])
    async def weapon(ctx, *args):
        """무작위 무기를 호출합니다.
        """
        # global WEAPON_TIME
        # global WP_EN_JP, WP_EN_KO, ST_EN_JP, ST_EN_KO
        # now = datetime.datetime.now()
        # until_update = (now-WEAPON_TIME).total_seconds()
        # if until_update >= 60*60*24:
        #     (WP_EN_JP, WP_EN_KO, ST_EN_JP, ST_EN_KO) = get_translate_dict()
        #     WEAPON_TIME = now
        sel_wp_en = random.choice(list(WP_EN_JP.keys()))
        await ctx.send('{0.author.mention} {1}/{2}/{3}'.format(ctx,
                                                               sel_wp_en,
                                                               WP_EN_JP[sel_wp_en],
                                                               WP_EN_KO[sel_wp_en]))

    @bot.command(name='select',
                 aliases=['선택'])
    async def select(ctx, *args):
        """고민될 때 사용합니다.
        """
        if len(args) < 2:
            await ctx.send('{0.author.mention} 최소 2개를 입력하세요.'.format(ctx))
        else:
            await ctx.send('{0.author.mention} {1}개 중에서 선택: {2}'.format(ctx, len(args), random.choice(args)))

    @bot.command(name='kbb',
                 aliases=['가위바위보', '대결'])
    async def kbb_game(ctx, *args):
        """가위바위보를 합니다."""
        if len(args) <= 0:
            return '가위/바위/보 또는 결과를 선택해야합니다.'
        if args[0] == '결과':
            result_str = '[총 {0:d}명의 선수]\n'.format(len(kbb_entry))
            for key in kbb_entry.keys():
                result_str = result_str + '{0}: {1}\n'.format(key, kbb_entry[key])
            kbb_entry.clear()
            return result_str
        elif args[0] in ['가위', '바위', '보']:
            kbb_entry[ctx.author.name] = args[0]
            return '{0.author.mention} {1} 엔트리!'.format(ctx, args[0])

    bot.run(client_token)


if __name__ == '__main__':
    main()