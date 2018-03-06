# esk8 bot by Armi-ne

import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import time
import string
import logging
import lbry.converter as conv
import lbry.websites as web
import lbry.battery as batt


logger = logging.getLogger('discord')  # Setting up the logger
logger.setLevel(logging.DEBUG)
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
        embed = discord.Embed(title="Hello %s, here are a list of commands" % (message.author.name), color=0xFF0000)
        embed.add_field(name="+about", value="Learn more about Electric SkateBot", inline=False)
        embed.add_field(name="+batteryhelp", value="learn more about the +battery calculator", inline=False)
        embed.add_field(name="+brandhelp 1 (/) 2 (/) 3", value="Learn more about the Brand command, Page 1/2/3")
        embed.add_field(name="+convert", value="Use \"+convert #Number# #Unit# #Desired Unit#\"｜kph <-> mph｜km <-> mi｜cm <-> inch｜km <- Wh -> mi", inline=False)
        embed.add_field(name="+easter eggs", value="Easter Eggs", inline=False)
        embed.add_field(name="+forum", value="Get link to electric-skateboard.builders", inline=False)
        embed.add_field(name="+reddit", value="Get link to the official esk8 Reddit", inline=False)
        embed.add_field(name="+server", value="Server Information", inline=False)
        await client.send_message(message.author, embed=embed)
    # Easter Eggs
    if (message.content.upper() == "+EASTER EGGS" or message.content.upper() == "+EASTER EGG"):
        embed = discord.Embed(title="Hello %s, here are a list of easter eggs" % (message.author.name), color=0xFF0000)
        embed.add_field(name="Ben Pls", value="Everyone knows this one", inline=False)
        embed.add_field(name="Moshi Moshi", value="*UserName* Desu", inline=False)
        embed.add_field(name="Who's your daddy?", value="Want to know who was responsible for the bots birth?", inline=False)
        await client.send_message(message.author, embed=embed)
    # Battery Help
    if message.content.upper() == "+BATTERYHELP":
        embed = discord.Embed(title="Hello %s, here's an explanation of how the +battery command works" % (message.author.name), color=0xFF0000)
        embed.add_field(name="Usage:", value="In order to make use of this command you are first required to have 4 pieces of information. 1) Parallel count. 2) Series count. 3) Amp hours per cell. 4) Nominal voltage per cell (for li-ion 3.6 is best)")
        embed.add_field(name="Command Format:", value="+battery #parallel value# #series value# #amp hour value# #nominal voltage value#")
        await client.send_message(message.author, embed=embed)
    # Brand Help 1
    if message.content.upper() == "+BRANDHELP 1":
        embed = discord.Embed(title="Hello %s, here are a list of Brand's Sub-Commands, Page 1" % (message.author.name), color=0xFF0000)
        embed.add_field(name="+brand acton", value="Acton", inline=True)
        embed.add_field(name="+brand arc", value="Arc Boards", inline=True)
        embed.add_field(name="+brand backfire", value="Backfire", inline=True)
        embed.add_field(name="+brand boosted", value="Boosted", inline=True)
        embed.add_field(name="+brand carvon", value="Carvon", inline=True)
        embed.add_field(name="+brand diyeboard", value="DiyEboard", inline=True)
        await client.send_message(message.author, embed=embed)
    # Brand Help 2
    if message.content.upper() == "+BRANDHELP 2":
        embed = discord.Embed(title="Hello %s, here are a list of Brand's Sub-Commands, Page 2" % (message.author.name), color=0xFF0000)
        embed.add_field(name="+brand enertion", value="Enertion", inline=True)
        embed.add_field(name="+brand evolve", value="Evolve", inline=True)
        embed.add_field(name="+brand jed", value="Jed Board", inline=True)
        embed.add_field(name="+brand max", value="Max", inline=True)
        embed.add_field(name="+brand meepo", value="Meepo", inline=True)
        embed.add_field(name="+brand metroboard", value="Metroboard", inline=True)
        await client.send_message(message.author, embed=embed)
    # Brand Help 3
    if message.content.upper() == "+BRANDHELP 3":
        embed = discord.Embed(title="Hello %s, here are a list of Brand's Sub-Commands, Page 3" % (message.author.name), color=0xFF0000)
        embed.add_field(name="+brand onewheel", value="Onewheel", inline=True)
        embed.add_field(name="+brand predator", value="Predator", inline=True)
        embed.add_field(name="+brand pulseboard", value="Pulse Board", inline=True)
        embed.add_field(name="+brand riptide", value="Riptide", inline=True)
        embed.add_field(name="+brand trampa", value="Trampa", inline=True)
        embed.add_field(name="+brand wowgo", value="Wowgo", inline=True)
        await client.send_message(message.author, embed=embed)
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
    # Battery Conversion Command
    if message.content.upper().startswith("+BATTERY"):
        command, in_a, in_b, in_c, in_d = message.content.split(" ")
        nom_volt, tot_ah, tot_wh, rang_km, rang_mi = batt.executer(in_a, in_b, in_c, in_d)
        embed = discord.Embed(title="Electric SkateBot Battery Calculator", color=0xFF0000)
        embed.add_field(name="Input Parallel:", value="{0:.2f}".format(float(in_a)) + "p", inline=True)
        embed.add_field(name="Input Series:", value="{0:.2f}".format(float(in_b)) + "s", inline=True)
        embed.add_field(name="Input Amp Hours:", value="{0:.2f}".format(float(in_c)) + "ah", inline=True)
        embed.add_field(name="Input Nominal Voltage:", value="{0:.2f}".format(float(in_d)) + "v", inline=True)
        embed.add_field(name="Nominal Voltage of Pack:", value="{0:.2f}".format(float(nom_volt)) + "v", inline=False)
        embed.add_field(name="Total Amp Hours:", value="{0:.2f}".format(float(tot_ah)) + "ah", inline=False)
        embed.add_field(name="Total Watt Hours:", value="{0:.2f}".format(float(tot_wh)) + "wh", inline=False)
        embed.add_field(name="Estimated Ranges:", value="{0:.2f}".format(float(rang_km)) + "km, or " + "{0:.2f}".format(float(rang_mi)) + "mi")
        await client.send_message(message.channel, embed=embed)
    # Reddit
    if message.content.upper() == "+REDDIT":
        embed = discord.Embed(title="Electric Skateboarding Reddit", description="https://www.reddit.com/r/ElectricSkateboarding/", color=0xFF0000)
        await client.send_message(message.channel, embed=embed)
    # Forum
    if message.content.upper() == "+FORUM":
        embed = discord.Embed(title="Electric Skateboarding Forum", description="https://www.electric-skateboard.builders/", color=0xFF0000)
        await client.send_message(message.channel, embed=embed)
    # Brand
    if message.content.upper().startswith("+BRAND"):
        brand, desired_brand = message.content.split()
        website, email, facebook, reddit, logo = web.sitefinder(desired_brand)
        embed = discord.Embed(title="%s's Info" % str(desired_brand.capitalize()), color=0xFF0000)
        embed.add_field(name="Website: ", value=website, inline=True)
        embed.add_field(name="eMail: ", value=email, inline=True)
        embed.add_field(name="Facebook: ", value=facebook, inline=False)
        embed.add_field(name="Reddit: ", value=reddit, inline=False)
        embed.set_thumbnail(url=logo)
        await client.send_message(message.channel, embed=embed)
    # About
    if message.content.upper() == "+ABOUT":
        embed = discord.Embed(title="Hello %s, here's more information on the bot" % (message.author.name), color=0xFF0000)
        embed.add_field(name="Source Code: ", value="https://github.com/armi-ne/python-tests", inline=False)
        embed.add_field(name="More Info: ", value="This bot was created by Armin as a project and aide for the Electric Skateboarding channel. Feel free to look at the source code and should you have any suggestions please feel free to message Armin :)", inline=False)
        embed.add_field(name="Mentions", value="Special thanks to Weinbee, Jinra, NeoZeon (helping with code) and Howser (custom logo)", inline=False)
        await client.send_message(message.author, embed=embed)
    # Moshi Moshi
    if message.content.upper() == "MOSHI MOSHI":
        await client.send_message(message.channel, "{} desu".format(message.author.name))
    # Ben Pls
    if message.content.upper() == "BEN PLS":
        await client.send_message(message.channel, "<:benpls:382239983240478724>")
    # Who's your daddy?
    if message.content.upper().startswith("WHO\'S YOUR DADDY") or message.content.upper().startswith("WHOS YOUR DADDY") or message.content.upper().startswith("WHO’S YOUR DADDY") or message.content.upper().startswith("WHO IS YOUR DADDY"):
        await client.send_message(message.channel, "Armin Senpai")
    await client.process_commands(message)

client.run("")
