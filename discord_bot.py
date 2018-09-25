from discord_key import client_id, client_secret, client_token
from file_handler import FileHandler


import discord
from discord.ext import commands
import asyncio


DESC = '''SalmonRun Reminder KR
'''


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

    @bot.command(name='salmonrun', aliases=['연어런', '연어'])
    async def salmonrun():
        '''SalmonRunKR의 최신 트윗을 가져옵니다.
        '''
        await bot.say(file_handler.read())

    bot.run(client_token)


if __name__ == '__main__':
    main()