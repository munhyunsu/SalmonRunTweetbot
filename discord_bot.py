from discord.ext import commands

from discord_key import client_token

BOT_DESC = '''SalmonRun Reminder KR'''


def main():
    bot = commands.Bot(command_prefix='$',
                       case_insensitive=True,
                       description=BOT_DESC)

    extensions = ['DNLabDiscordBot.luha_commands', 'salmonrun_commands']

    @bot.event
    async def on_ready():
        print('Logged in as')
        print(bot.user.name)
        print(bot.user.id)
        print('----------')

    for extension in extensions:
        bot.load_extension(extension)

    bot.run(client_token)


if __name__ == '__main__':
    main()
