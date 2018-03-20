import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import datetime
import time

Client = discord.Client()
client = commands.Bot(command_prefix="+")
client.remove_command("help")


async def get_logs_from():
    async for x in client.logs_from(client.get_channel("425714572981436436"), limit=20):
        role_name= x.content
        print(role_name)
        for reaction in x.reactions:
            reacts = reaction.emoji
            print(reacts)
            reactors = await client.get_reaction_users(reaction)
            for reactor in reactors:
                reactees = reactor.id
                print(reactees)
    
