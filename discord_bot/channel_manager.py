import string
import random
import discord


class ChannelManager(object):
    async def create_channel(self, ctx, args=()):
        if len(args) < 1:
            return '채널 [텍스트|보이스] [인원]'
        guild = ctx.guild
        mode = args[0].lower()
        if len(args) > 1:
            limit = min(int(args[1]), 99)
        else:
            limit = 99
        if mode in ['텍스트', 'text']:
            text_category = None
            for ct in guild.categories:
                if ct.name == 'Text Channels':
                    text_category = ct
                    break
            name = self._get_channel_name()
            await guild.create_text_channel(name, category=text_category)
        elif mode in ['보이스', 'voice']:
            voice_category = None
            for ct in guild.categories:
                if ct.name == 'Voice Channels':
                    voice_category = ct
                    break
            name = self._get_channel_name()
            new = await guild.create_voice_channel(name, category=voice_category)
            await new.edit(user_limit=limit)

    def _get_channel_name(self):
        candidate = string.ascii_letters + string.digits
        rand = ''.join(random.choices(candidate, k=5))
        return 'Salmonrun-{0}'.format(rand)
