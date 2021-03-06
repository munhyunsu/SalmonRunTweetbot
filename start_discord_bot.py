from discord.ext import commands

from private.discord_key import CLIENT_TOKEN

BOT_DESC = '''SalmonRun Reminder KR'''


def main():
    bot = commands.Bot(command_prefix='!',
                       case_insensitive=True,
                       description=BOT_DESC)

    extensions = ['DNLabDiscordBot.luha_bot.luha_commands',
                  'discord_bot.salmonrun_commands']

    @bot.event
    async def on_ready():
        print('Logged in as')
        print(bot.user.name)
        print(bot.user.id)
        print('----------')

    for extension in extensions:
        bot.load_extension(extension)

    bot.run(CLIENT_TOKEN)


if __name__ == '__main__':
    main()
