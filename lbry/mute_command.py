import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio

Client = discord.Client()
client = commands.Bot(command_prefix="+")
client.remove_command("help")


def checks(codeblock=None):
    if codeblock is not None:
        answer = "Correct"
    else:
        answer = "Missing Time"
    return answer


def duration_and_reason(durationin, reasonin = None):
    duration = float(durationin) * 60
    sentence = ' '.join(reasonin)
    return duration, sentence
