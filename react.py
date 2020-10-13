import os
import time

import discord
from discord.utils import get

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

chars = {
    "a": "🇦",
    "b": "🇧",
    "c": "🇨",
    "d": "🇩",
    "e": "🇪",
    "f": "🇫",
    "g": "🇬",
    "h": "🇭",
    "i": "🇮",
    "j": "🇯",
    "k": "🇰",
    "l": "🇱",
    "m": "🇲",
    "n": "🇳",
    "o": "🇴",
    "p": "🇵",
    "q": "🇶",
    "r": "🇷",
    "s": "🇸",
    "t": "🇹",
    "u": "🇺",
    "v": "🇻",
    "w": "🇼",
    "x": "🇽",
    "y": "🇾",
    "z": "🇿",
    "0": "0⃣",
    "1": "1⃣",
    "2": "2⃣",
    "3": "3⃣",
    "4": "4⃣",
    "5": "5⃣",
    "6": "6⃣",
    "7": "7⃣",
    "8": "8⃣",
    "9": "9⃣",
}

chars_secondary = {
    "b": "8⃣",
    "e": "3⃣",
    "g": "9⃣",
    "h": "4⃣",
    "i": "1⃣",
    "o": "0⃣",
    "s": "5⃣",
    "t": "7⃣",
    "z": "2⃣",
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

    if message.content.startswith("!r "):

        text = message.content.split()

        if len(text) > 1:
            react_text = text[1].lower()

            channel = message.channel

            react_message = None
            past_messages = await channel.history(limit=2).flatten()
            for m in past_messages:
                react_message = m

            for i in range(len(react_text)):
                past_chars = react_text[0:i]
                if react_text[i] in chars:
                    if react_text[i] not in past_chars:
                        await react_message.add_reaction(chars[react_text[i]])
                    elif react_text[i] in chars_secondary:
                        await react_message.add_reaction(chars_secondary[react_text[i]])

client.run(DISCORD_TOKEN)
