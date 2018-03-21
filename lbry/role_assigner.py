import discord
from discord.ext.commands import Bot
import asyncio
import datetime
import time


tick = {}
cross = {}


async def react_dictionary_creator(client, channel):
    channel_in = channel
    print(channel_in)
    print(channel_in.id)
    async for x in client.logs_from(channel_in, limit=100):
        for reaction in x.reactions:
            reacts = reaction.emoji
            reactors = await client.get_reaction_users(reaction)
            for reactor in reactors:
                if reactor.id == "425732605342908426":
                    asd="asd"
                elif reaction.emoji == "✅":
                    joined = str(reactor.id) + str(x.content)
                    tick.update({str(joined):str(joined)})
                elif reaction.emoji == "❌":
                    joined = str(reactor.id) + str(x.content)
                    cross.update({str(joined):str(joined)})
