# esk8 bot by Armi-ne

import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import time
import string
import logging

logger = logging.getLogger('discord')  # Setting up the logger
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
Client = discord.Client()
client = commands.Bot(command_prefix="+")
client.remove_command("help")

# Converter Functions


def executer(a, b):  # This is the main executer Function in which all the different functions are called upon and returned answers will be input into the next one e.t.c
    original, desired_u = a, b
    formatted_speed, formatted_unit, desired_un = data_formatter(original, desired_u)
    printthis = str(speed_converter(formatted_speed, formatted_unit, desired_un))
    return printthis


def data_formatter(arg, b):  # The purpose of this function is to take the user input and seperate the words and numbers, then assign them to new variables and return them
    no_numb = str.maketrans(dict.fromkeys('0123456789'))
    no_lett = str.maketrans(dict.fromkeys(string.ascii_lowercase))
    user_speed = arg.translate(no_lett)
    user_unit = arg.translate(no_numb)
    desired = b
    return user_speed, user_unit, desired


def speed_converter(a, b, c):  # This is the final step, the formatted unit and speed are taken in and through an IF statement it will find out the desired unit and will then proceed to convert it, printing out the result.
    # Conversion Dictionary
    conversion = {"mph_kph": 1.60934, "kph_mph": 0.621371, "km_mi": 0.621371,
"mi_km": 1.60934, "Wh_km": 0.1, "Wh_mi": 0.0621371, "cm_inch": 0.393701, "inch_cm": 2.54}
    # KPH to MPH
    if b == "kph" and c == "mph":
        print("Value: " + a + ", " + "Original Unit: " + b + ", " + "Desired Unit: " + c)
        result = "{0:.2f}".format(int(float(a) * conversion["kph_mph"])) + c
    # MPH to KPH
    elif b == "mph" and c == "kph":
        print("Value: " + a + ", " + "Original Unit: " + b + ", " + "Desired Unit: " + c)
        result = "{0:.2f}".format(int(float(a) * conversion["mph_kph"])) + c
    # KM to MI
    elif b == "km" and c == "mi":
        print("Value: " + a + ", " + "Original Unit: " + b + ", " + "Desired Unit: " + c)
        result = "{0:.2f}".format(float(a) * conversion["km_mi"]) + c
    # MI to KM
    elif b == "mi" and c == "km":
        print("Value: " + a + ", " + "Original Unit: " + b + ", " + "Desired Unit: " + c)
        result = "{0:.2f}".format(float(a) * conversion["mi_km"]) + c
    # kWh
    elif b == "wh":
        print("Value: " + a + ", " + "Original Unit: " + b + ", " + "Desired Unit: " + c)
        result = a + "wh should get you: {0:.2f}".format(float(a) * conversion["Wh_mi"]) + " miles, or {0:.2f}".format(float(a) * conversion["Wh_km"]) + " kilometers. Please note that this is an ESTIMATED value."
    # Inch to CM
    elif b == "inch" and c == "cm":
        print("Value: " + a + ", " + "Original Unit: " + b + ", " + "Desired Unit: " + c)
        result = "{0:.2f}".format(float(a) * conversion["inch_cm"]) + " cm"
    # CM to Inch
    elif b == "cm" and c == "inch":
        print("Value: " + a + ", " + "Original Unit: " + b + ", " + "Desired Unit: " + c)
        result = "{0:.2f}".format(float(a) * conversion["cm_inch"]) + " inches"
    # Bad Input
    else:
        result = "Please input your values correctly"
    return result


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='+help for more info'))
    print("Hi, my name is " + client.user.name)
    print("My ID is: " + client.user.id)


@client.event
async def on_message(message):
    # Help
    if message.content.upper() == "+HELP":
        embed = discord.Embed(title="Hello %s, here are a list of commands: " % (message.author.name), color=0xFF0000)
        embed.add_field(name="+convert", value="Use \"+convert #Number#... ...\"｜kph <-> mph｜km <-> mi｜cm <-> inch｜km <- Wh -> mi", inline=False)
        embed.add_field(name="+reddit", value="Get link to the official esk8 Reddit", inline=False)
        embed.add_field(name="+forum", value="Get link to electric-skateboard.builders", inline=False)
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
        command, user_input, user_desired = message.content.split(" ")
        original_value, original_unit, desired_unit = data_formatter(user_input, user_desired)
        result = executer(user_input, user_desired)
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

client.run("")
