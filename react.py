import os
import time

import discord
from discord.utils import get

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

letters = {
    ":regional_indicator_a:": "🇦",
    ":regional_indicator_b:": "🇧",
    ":regional_indicator_c:": "🇨",
    ":regional_indicator_d:": "🇩",
    ":regional_indicator_e:": "🇪",
    ":regional_indicator_f:": "🇫",
    ":regional_indicator_g:": "🇬",
    ":regional_indicator_h:": "🇭",
    ":regional_indicator_i:": "🇮",
    ":regional_indicator_j:": "🇯",
    ":regional_indicator_k:": "🇰",
    ":regional_indicator_l:": "🇱",
    ":regional_indicator_m:": "🇲",
    ":regional_indicator_n:": "🇳",
    ":regional_indicator_o:": "🇴",
    ":regional_indicator_p:": "🇵",
    ":regional_indicator_q:": "🇶",
    ":regional_indicator_r:": "🇷",
    ":regional_indicator_s:": "🇸",
    ":regional_indicator_t:": "🇹",
    ":regional_indicator_u:": "🇺",
    ":regional_indicator_v:": "🇻",
    ":regional_indicator_w:": "🇼",
    ":regional_indicator_x:": "🇽",
    ":regional_indicator_y:": "🇾",
    ":regional_indicator_z:": "🇿",
    ":regional_indicator_0:": "0⃣",
    ":regional_indicator_1:": "1⃣",
    ":regional_indicator_2:": "2⃣",
    ":regional_indicator_3:": "3⃣",
    ":regional_indicator_4:": "4⃣",
    ":regional_indicator_5:": "5⃣",
    ":regional_indicator_6:": "6⃣",
    ":regional_indicator_7:": "7⃣",
    ":regional_indicator_8:": "8⃣",
    ":regional_indicator_9:": "9⃣",
}

@client.event
async def on_ready():
    pass

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!allreacts"):
        channel = message.channel

        react_message = None
        past_messages = await channel.history(limit=2).flatten()
        for m in past_messages:
            react_message = m

        for emoji in client.emojis:
            await react_message.add_reaction(emoji)

    if message.content.startswith("!closs"):

        react_text = "clos5"

        channel = message.channel

        react_message = None
        past_messages = await channel.history(limit=2).flatten()
        for m in past_messages:
            react_message = m

        for char in react_text:
            emoji = ":regional_indicator_" + char + ":"
            await react_message.add_reaction(letters[emoji])

    if message.content.startswith("!wipergang"):

        for role in message.author.roles:
            if role.name == "Wiper Gang":
                react_text = "wipergan9"

                channel = message.channel

                react_message = None
                past_messages = await channel.history(limit=2).flatten()
                for m in past_messages:
                    react_message = m

                for char in react_text:
                    emoji = ":regional_indicator_" + char + ":"
                    await react_message.add_reaction(letters[emoji])
                break

client.run(DISCORD_TOKEN)
