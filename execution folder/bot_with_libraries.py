# esk8 bot by Armi-ne

import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import time
import string
import logging
import lbry.converter as conv

logger = logging.getLogger('discord')  # Setting up the logger
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
Client = discord.Client()
client = commands.Bot(command_prefix="+")
client.remove_command("help")


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='+help for more info'))
    print("Hi, my name is " + client.user.name)
    print("My ID is: " + client.user.id)


@client.command(pass_context=True)
async def server(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="", color=0xFF0000)
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Number of e-Boarders", value=(len(ctx.message.server.members) - 3))
    embed.add_field(name="Number of Channels", value=(len(ctx.message.server.channels)))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await client.say(embed=embed)


@client.event
async def on_message(message):
    # Help
    if message.content.upper() == "+HELP":
        embed = discord.Embed(title="Hello %s, here are a list of commands: " % (message.author.name), color=0xFF0000)
        embed.add_field(name="+convert", value="Use \"+convert #Number# #Unit# #Desired Unit#\"｜kph <-> mph｜km <-> mi｜cm <-> inch｜km <- Wh -> mi", inline=False)
        embed.add_field(name="+reddit", value="Get link to the official esk8 Reddit", inline=False)
        embed.add_field(name="+forum", value="Get link to electric-skateboard.builders", inline=False)
        embed.add_field(name="+server", value="Server Information", inline=False)
        embed.add_field(name="+easter eggs", value="Easter Eggs", inline=False)
        await client.send_message(message.channel, embed=embed)
    # Easter Eggs
    if message.content.upper() == "+EASTER EGGS":
        embed = discord.Embed(title="Hello %s, here are a list of easter eggs: " % (message.author.name), color=0xFF0000)
        embed.add_field(name="Moshi Moshi", value="*UserName* Desu", inline=False)
        embed.add_field(name="Ben Pls", value="Everyone knows this one", inline=False)
        embed.add_field(name="Who's your daddy?", value="Want to know who was responsible for the bots birth?", inline=False)
        await client.send_message(message.channel, embed=embed)
    # Conversion Command
    if message.content.upper().startswith("+CONVERT"):
        convert, input_value, user_input, user_desired = message.content.split(" ")
        original_value, original_unit, desired_unit = conv.data_formatter(input_value, user_input, user_desired)
        result = conv.executer(input_value, user_input, user_desired)
        embed = discord.Embed(title="Electric SkateBot Converter", color=0xFF0000)
        embed.add_field(name="Input Value:", value=original_value, inline=True)
        embed.add_field(name="Input Unit:", value=original_unit, inline=True)
        embed.add_field(name="Output Unit:", value=desired_unit, inline=False)
        embed.add_field(name="Result", value=result, inline=False)
        await client.send_message(message.channel, embed=embed)
    # Reddit
    if message.content.upper() == "+REDDIT":
        embed = discord.Embed(title="Electric Skateboarding Reddit", description="https://www.reddit.com/r/ElectricSkateboarding/", color=0xFF0000)
        await client.send_message(message.channel, embed=embed)
    # Forum
    if message.content.upper() == "+FORUM":
        embed = discord.Embed(title="Electric Skateboarding Forum", description="https://www.electric-skateboard.builders/", color=0xFF0000)
        await client.send_message(message.channel, embed=embed)
    # Moshi Moshi
    if message.content.upper() == "MOSHI MOSHI":
        await client.send_message(message.channel, "{} Desu".format(message.author.name))
    # Ben Pls
    if message.content.upper() == "BEN PLS":
        await client.send_message(message.channel, "<:benpls:382239983240478724>")
    # Who's your daddy?
    if message.content.upper().startswith("WHO\'S YOUR DADDY") or message.content.upper().startswith("WHOS YOUR DADDY") or message.content.upper().startswith("WHO’S YOUR DADDY") or message.content.upper().startswith("WHO IS YOUR DADDY"):
        await client.send_message(message.channel, "Armin Senpai")
    # Server Info
    # if message.content.upper() == "+SERVER":
    #     await client.send_message(message.channel, message.server.name)
    await client.process_commands(message)

client.run("")
