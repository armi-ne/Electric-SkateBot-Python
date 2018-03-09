import discord
from discord.ext import commands
from discord.ext.commands import bot
import logging
import lbry.battery as batt
import lbry.brand as brand_
import lbry.converter as conv

Client = discord.Client()
client = commands.Bot(command_prefix="+")
client.remove_command("help")

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
async def convert(ctx, inputval, inputuni, to_text, desireduni):
    upcase1, upcase2, upcase4 = inputval.upper(), inputuni.upper(), desireduni.upper()
    answer = conv.executer(float(upcase1), upcase2, upcase4)
    embed = discord.Embed(title="Electric SkateBot Converter", color=0xFF0000)
    embed.add_field(name="Input Value:", value=inputval, inline=True)
    embed.add_field(name="Input Unit:", value=inputuni, inline=True)
    embed.add_field(name="Output Unit:", value=desireduni, inline=False)
    embed.add_field(name="Result", value=answer, inline=False)
    await client.say(embed=embed)   


@client.command(pass_context=True)
async def brand(ctx, brandin):
    upcase1 = brandin.upper()
    website, email, facebook, reddit, thumbnail = brand_.brandfinder(upcase1)
    embed = discord.Embed(title="%s's Info" % brandin.capitalize(), color=0xFF0000)
    embed.add_field(name="Website: ", value=website, inline=True)
    embed.add_field(name="eMail: ", value=email, inline=True)
    embed.add_field(name="Facebook: ", value=facebook, inline=False)
    embed.add_field(name="Reddit: ", value=reddit, inline=False)
    embed.set_thumbnail(url=thumbnail)
    await client.say(embed=embed)


client.run("")
