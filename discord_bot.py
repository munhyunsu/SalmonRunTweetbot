from discord_key import client_id, client_secret, client_token

import discord
from discord.ext import commands
import asyncio





def main():
    bot = commands.Bot(command_prefix='$', description='SalmonrunReminderKR')

    @bot.event
    async def on_ready():
        print('Logged in as')
        print(bot.user.name)
        print(bot.user.id)
        print('------')

    @bot.command()
    async def here():
        await bot.say('here')

    @bot.group(pass_context=True)
    async def cool(ctx):
        """Says if a user is cool.
        In reality this just checks if a subcommand is being invoked.
        """
        if ctx.invoked_subcommand is None:
            await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))

    @cool.command(name='bot')
    async def _bot():
        """Is the bot cool?"""
        await bot.say('Yes, the bot is cool.')

    bot.run(client_token)


if __name__ == '__main__':
    main()