import discord

from private.discord_key import client_token


def main():
    print('here')
    client = discord.Client()

    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        if not message.content.startswith('!'):
            await message.delete()

    client.run(client_token)


if __name__ == '__main__':
    main()
