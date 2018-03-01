# esk8 bot by Armi-ne

import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
import time
import string

Client = discord.Client()
client = commands.Bot(command_prefix="++")


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
        result = str(int(float(a) * conversion["kph_mph"])) + c
    # MPH to KPH
    elif b == "mph" and c == "kph":
        print("Value: " + a + ", " + "Original Unit: " + b + ", " + "Desired Unit: " + c)
        result = str(int(float(a) * conversion["mph_kph"])) + c
    # KM to MI
    elif b == "km" and c == "mi":
        print("Value: " + a + ", " + "Original Unit: " + b + ", " + "Desired Unit: " + c)
        result = str(float(a) * conversion["km_mi"]) + c
    # MI to KM
    elif b == "mi" and c == "km":
        print("Value: " + a + ", " + "Original Unit: " + b + ", " + "Desired Unit: " + c)
        result = str(float(a) * conversion["mi_km"]) + c
    # kWh
    elif b == "wh":
        print("Value: " + a + ", " + "Original Unit: " + b + ", " + "Desired Unit: " + c)
        result = a + "wh should get you: " + str(float(a) * conversion["Wh_mi"]) + " miles, or " + str(float(a) * conversion["Wh_km"]) + " kilometers. Please note that this is an ESTIMATED value."
    # Inch to CM
    elif b == "inch" and c == "cm":
        print("Value: " + a + ", " + "Original Unit: " + b + ", " + "Desired Unit: " + c)
        result = str(float(a) * conversion["inch_cm"]) + " cm"
    # CM to Inch
    elif b == "cm" and c == "inch":
        print("Value: " + a + ", " + "Original Unit: " + b + ", " + "Desired Unit: " + c)
        result = str(float(a) * conversion["cm_inch"]) + " inches"
    # Bad Input
    else:
        result = "Please input your values correctly"
    return result


@client.event
async def on_ready():  # This will print a message in the console when the bot is ready
    print("Bot is ready :)")


@client.event
async def on_message(message):  # When you receive a message, the following if statements will execute
    # Conversion Command
    if message.content.upper().startswith("++CONVERT"):
        command, user_input, user_desired = message.content.split(" ")
        await client.send_message(message.channel, executer(user_input, user_desired))
    # Who's your daddy?
    if message.content.upper() == "WHO'S YOUR DADDY?":
        await client.send_message(message.channel, "Armin Senpai")
    # Ben Pls
    if message.content.upper() == "BEN PLS":
        await client.send_message(message.channel, "<:benpls:382239983240478724>")
    # Convert Help
    if message.content.upper().startswith("++CONVERSION HELP"):
        await client.send_message(message.channel, "Use \"++convert #Number#... ...\" kph <-> mph, km <-> mi, cm <-> inch, km <- Wh -> mi")

client.run("NDE3Mzg2MDM5NjkxMTgyMDgw.DXnTvg.s1iUUrbwKHQGJ2YJgJdbvHHituc")
