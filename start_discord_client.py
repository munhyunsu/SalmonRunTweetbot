import asyncio

import discord

from private.discord_key import CLIENT_TOKEN, GUILD_ID, ADMIN_IDS


def main():
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
        if message.type != discord.message.MessageType.default:
            return
        is_delete = True
        if message.author.id in ADMIN_IDS:
            is_delete = False
        mentions = message.role_mentions
        for mention in mentions:
            if mention.name.lower() == 'admin':
                is_delete = False
        if message.content.startswith('!'):
            is_delete = False
        if is_delete:
            await message.delete()

    async def manage_voice_channel():
        await client.wait_until_ready()
        while not client.is_closed():
            guild = client.get_guild(id=GUILD_ID)
            voice_channels = guild.voice_channels
            vc_list = list()
            for vc in voice_channels:
                if not vc.name.startswith('Salmonrun'):
                    continue
                if len(vc.members) == 0:
                    vc_list.append(vc)
            if len(vc_list) == 0:
                voice_category = None
                for ct in guild.categories:
                    if ct.name == 'Voice Channels':
                        voice_category = ct
                        break
                new = await guild.create_voice_channel('Salmonrun', category=voice_category)
                await new.edit(user_limit=4)
            elif len(vc_list) > 1:
                for vc in vc_list[:-1]:
                    await vc.delete()
            await asyncio.sleep(60*1)  # x minutes

    client.loop.create_task(manage_voice_channel())
    client.run(CLIENT_TOKEN)


if __name__ == '__main__':
    main()
