import string
import random
import discord


class ChannelManager(object):
    async def create_channel(self, ctx, args=()):
        if len(args) < 1:
            return '채널 [텍스트|보이스] [인원]'
        guild = ctx.guild
        mode = args[0]
        if len(args) > 1:
            limit = min(int(args[1]), 99)
        else:
            limit = 99
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            guild.me: discord.PermissionOverwrite(read_messages=True,
                                                  send_messages=True,
                                                  manage_roles=True)
        }
        rand = self._get_channel_rand()
        name = 'Salmonrun-{0}'.format(rand)
        if mode.lower() in ['텍스트', 'text']:
            text_category = None
            for ct in guild.categories:
                if ct.name == 'Text Channels':
                    text_category = ct
                    break
            await guild.create_text_channel(name, category=text_category, overwrites=overwrites)
            rand = rand.lower()
        elif mode.lower() in ['보이스', 'voice']:
            voice_category = None
            for ct in guild.categories:
                if ct.name == 'Voice Channels':
                    voice_category = ct
                    break
            new = await guild.create_voice_channel(name, category=voice_category, overwrites=overwrites)
            await new.edit(user_limit=limit)
        else:  # assign rule for connect private channel
            for channel in guild.channels:
                if channel.name.endswith(mode):
                    await channel.set_permissions(ctx.author,
                                                  read_messages=True,
                                                  send_messages=True)
                    return '{0.author.mention} {1} 권한 설정 완료.'.format(ctx, mode)
            return '{0.author.mention} {1} 채널을 찾지 못 했습니다.'.format(ctx, mode)
        return '{0.author.mention} 채널 {1}을 입력하여 입장하세요.'.format(ctx, rand)

    def _get_channel_rand(self):
        candidate = string.ascii_letters + string.digits
        rand = ''.join(random.choices(candidate, k=5))
        return rand
