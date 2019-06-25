import asyncio
import logging
from logging.handlers import RotatingFileHandler
import datetime

import discord

from private.discord_key import CLIENT_TOKEN, GUILD_ID, ADMIN_IDS, LOGPATH


def main():
    client = discord.Client()
    logger = logging.getLogger('Salmonrun')
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler(LOGPATH)
    logger.addHandler(handler)

    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')

    @client.event
    async def on_message(message):
        # Log all data
        log_data = {'created_at': message.created_at,
                    'channel': message.channel,
                    'author': message.author,
                    'content': message.content}
        ## replace quote word for csv compatible
        for key in log_data.keys():
            log_data[key] = str(log_data[key]).replace('"', '""')
        msg = '"{created_at}","{channel}","{author}","{content}"'.format_map(log_data)
        logger.info(msg)
        # Check allowed status
        if message.author == client.user:
            return
        if message.type != discord.message.MessageType.default:
            return
        # Check other status
        if message.author.id in ADMIN_IDS:
            return
        mentions = message.role_mentions
        for mention in mentions:
            if mention.name.lower() == 'admin':
                return
        if message.content.startswith('!'):
            return
        if message.channel.name.startswith('salmonrun'):
            return
        # delete message when flow reached here
        await message.delete()

    async def manage_voice_channel():
        # Automatic voice channel remove
        await client.wait_until_ready()
        while not client.is_closed():
            guild = client.get_guild(id=GUILD_ID)

            # manage voice channel
            voice_channels = guild.voice_channels
            vc_list = list()
            for vc in voice_channels:
                if not vc.name.startswith('Salmonrun'):
                    continue
                if len(vc.members) == 0:
                    if vc.name == 'Salmonrun':
                        vc_list.append(vc)
                    else:
                        await vc.delete()
            if len(vc_list) == 0:
                voice_category = None
                for ct in guild.categories:
                    if ct.name == 'Voice Channels':
                        voice_category = ct
                        break
                new = await guild.create_voice_channel('Salmonrun', category=voice_category)
                await new.edit(user_limit=4)
            elif len(vc_list) > 1:
                for vc in vc_list[1:]:
                    await vc.delete()

            # manage text channel
            text_channels = guild.text_channels
            for tc in text_channels:
                if not tc.name.startswith('salmonrun'):
                    continue
                message = await tc.history(limit=1).flatten()
                if len(message) == 0:
                    await tc.send('New text channel')
                else:
                    message = message[0]
                    latest_dt = message.created_at
                    current_dt = datetime.datetime.utcnow()
                    if (current_dt - latest_dt).total_seconds() > (60*60):
                        await tc.delete()

            await asyncio.sleep(60*5)  # x minutes

    client.loop.create_task(manage_voice_channel())
    client.run(CLIENT_TOKEN)


if __name__ == '__main__':
    main()

