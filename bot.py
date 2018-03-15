import discord
from discord.ext import commands
from discord.ext.commands import bot
import lbry.battery as batt
import lbry.brand as brand_
import lbry.converter as conv
import lbry.easter_eggs as eastereggs

Client = discord.Client()
client = commands.Bot(command_prefix="+")
client.remove_command("help")


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='+help for more info'))
    print("Hi, my name is " + client.user.name)
    print("My ID is: " + client.user.id)


@client.event  # Help Commands
async def on_message(message):
    # About
    if message.content.upper() == "+ABOUT":
        embed = discord.Embed(title="Hello %s, here's more information on the bot" % (message.author.name), color=0xFF0000)
        embed.add_field(name="Source Code: ", value="https://github.com/armi-ne/python-tests", inline=False)
        embed.add_field(name="More Info: ", value="This bot was created by Armin as a project and aide for the Electric Skateboarding channel. Feel free to look at the source code and should you have any suggestions please feel free to message Armin :)", inline=False)
        embed.add_field(name="Mentions", value="Special thanks to Weinbee, Jinra, NeoZeon (helping with code) and Howser (custom logo)", inline=False)
        await client.send_message(message.author, embed=embed)
    # Ben Pls
    if message.content.upper() in eastereggs.ben_pls:
        await client.send_message(message.channel, "<:benpls:382239983240478724>")
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
    # Easter Eggs
    if (message.content.upper() == "+EASTER EGGS" or message.content.upper() == "+EASTER EGG" or message.content.upper() == "+EASTEREGG" or message.content.upper() == "+EASTEREGGS"):
        embed = discord.Embed(title="Hello %s, here are a list of easter eggs" % (message.author.name), color=0xFF0000)
        embed.add_field(name="Ben Pls", value="Everyone knows this one", inline=False)
        embed.add_field(name="Moshi Moshi", value="*UserName* Desu", inline=False)
        embed.add_field(name="Who's your daddy?", value="Want to know who was responsible for the bots birth?", inline=False)
        await client.send_message(message.author, embed=embed)
    # Help
    if message.content.upper() == "+HELP":
        embed = discord.Embed(title="Hello %s, here are a list of commands" % (message.author.name), color=0xFF0000)
        embed.add_field(name="+about", value="Learn more about Electric SkateBot", inline=False)
        embed.add_field(name="+battery", value="learn more about the +battery calculator", inline=False)
        embed.add_field(name="+brand", value="Learn more about the Brand command")
        embed.add_field(name="+convert", value="learn more about the +convert conversion tool", inline=False)
        embed.add_field(name="+easter eggs", value="Easter Eggs", inline=False)
        embed.add_field(name="+forum", value="Get link to electric-skateboard.builders", inline=False)
        embed.add_field(name="+reddit", value="Get link to the official esk8 Reddit", inline=False)
        embed.add_field(name="+server", value="Server Information", inline=False)
        await client.send_message(message.author, embed=embed)
    # Moshi Moshi
    if message.content.upper() in eastereggs.moshi_moshi:
        await client.send_message(message.channel, "Electric Skatebot Desu, {} san".format(message.author.name))
    # Who's your daddy?
    if message.content.upper() in eastereggs.whos_your_daddy:
        await client.send_message(message.channel, "Armin Senpai")
    await client.process_commands(message)


@client.command(pass_context=True)
async def battery(ctx, series=None, parallel=None, amphour=None, nominal_volt=None):
    if all((series, parallel, amphour, nominal_volt)) and ((len(series) or len(parallel) or len(amphour) or len(nominal_volt)) <= 2):
        total_amphour, total_watthour, total_range_km, total_range_mi, total_nominal_voltage = batt.executer(series, parallel, amphour, nominal_volt)
        embed = discord.Embed(title="Electric SkateBot Battery Calculator", color=0xFF0000)
        embed.add_field(name="In Series:", value=series + "s", inline=True)
        embed.add_field(name="In Parallel:", value=parallel + "p", inline=True)
        embed.add_field(name="In Amp Hours:", value="%0.2f" % float(amphour) + "ah", inline=True)
        embed.add_field(name="In Nom Volt:", value="{0:.2f}".format(float(nominal_volt)) + "v", inline=True)
        embed.add_field(name="Nominal Voltage of Pack:", value="{0:.2f}".format(float(total_nominal_voltage)) + "v", inline=False)
        embed.add_field(name="Total Amp Hours:", value="{0:.2f}".format(float(total_amphour)) + "ah", inline=False)
        embed.add_field(name="Total Watt Hours:", value="{0:.2f}".format(float(total_watthour)) + "wh", inline=False)
        embed.add_field(name="Estimated Ranges:", value="{0:.2f}".format(float(total_range_km)) + "km, or " + "{0:.2f}".format(float(total_range_mi)) + "mi")
        await client.say(embed=embed)
    elif series == parallel == amphour == nominal_volt is None:
        embed = discord.Embed(title="Hello %s, here's an explanation of how the +battery command works" % (ctx.message.author.name), color=0xFF0000)
        embed.add_field(name="Usage:", value="In order to make use of this command you are first required to have 4 pieces of information. 1) Series count. 2) Parallel count. 3) Amp hours per cell. 4) Nominal voltage per cell (for li-ion 3.6 is best)")
        embed.add_field(name="Command Format:", value="+battery #Series value# #Parallel value# #Amp Hour value# #Nominal Voltage value#")
        await client.send_message(ctx.message.author, embed=embed)
    elif ((len(series) or len(parallel) or len(amphour) or len(nominal_volt)) > 2):
        embed = discord.Embed(title="Electric SkateBot Battery Calculator", color=0xFF0000)
        embed.add_field(name="Value length error:", value="Sorry but the bot only accepts values from 0-99 for each field.", inline=True)
        await client.say(embed=embed)
    else:
        embed = discord.Embed(title="Hello %s, here's an explanation of how the +battery command works" % (ctx.message.author.name), color=0xFF0000)
        embed.add_field(name="Usage:", value="In order to make use of this command you are first required to have 4 pieces of information. 1) Series count. 2) Parallel count. 3) Amp hours per cell. 4) Nominal voltage per cell (for li-ion 3.6 is best)")
        embed.add_field(name="Command Format:", value="+battery #Series value# #Parallel value# #Amp Hour value# #Nominal Voltage value#")
        await client.send_message(ctx.message.author, embed=embed)


@client.command(pass_context=True)  # +brand
async def brand(ctx, brandin=None):
    if brandin is not None:
        upcase1 = brandin.upper()
        website, email, facebook, reddit, thumbnail = brand_.brandfinder(upcase1)
        embed = discord.Embed(title="%s's Info" % brandin.capitalize(), color=0xFF0000)
        embed.add_field(name="Website: ", value=website, inline=True)
        embed.add_field(name="eMail: ", value=email, inline=True)
        embed.add_field(name="Facebook: ", value=facebook, inline=False)
        embed.add_field(name="Reddit: ", value=reddit, inline=False)
        embed.set_thumbnail(url=thumbnail)
        await client.say(embed=embed)
    else:
        embed = discord.Embed(title="Hello %s, here's an explanation of how the +brand command works" % (ctx.message.author.name), color=0xFF0000)
        embed.add_field(name="Command Format: ", value="+brand #brand#")
        embed.add_field(name="List of Brands Available: ", value="Please use +brandhelp 1/2/3 for the corresponding pages of brands we have available")
        await client.send_message(ctx.message.author, embed=embed)


@client.command(pass_context=True)  # +convert
async def convert(ctx, inputval=None, inputuni=None, to_text=None, desireduni=None):
    if all((inputval, inputuni, to_text, desireduni)):
        upcase1, upcase2, upcase4 = inputval.upper(), inputuni.upper(), desireduni.upper()
        answer = conv.executer(float(upcase1), upcase2, upcase4)
        embed = discord.Embed(title="Electric SkateBot Converter", color=0xFF0000)
        embed.add_field(name="Input Value:", value=inputval, inline=True)
        embed.add_field(name="Input Unit:", value=inputuni, inline=True)
        embed.add_field(name="Output Unit:", value=desireduni, inline=False)
        embed.add_field(name="Result", value=answer, inline=False)
        await client.say(embed=embed)
    else:
        embed = discord.Embed(title="Hello %s, here's an explanation of how the +convert command works" % (ctx.message.author.name), color=0xFF0000)
        embed.add_field(name="Command Format: ", value="Use \"+convert #Number# #Unit# #to# #Desired Unit#\"")
        embed.add_field(name="Current Conversion Pairs: ", value="kph <-> mph｜km <-> mi｜cm <-> inch｜km <- Wh -> mi")
        await client.send_message(ctx.message.author, embed=embed)


@client.command(pass_context=True)
async def server(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="", color=0xFF0000)
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="Number of e-Boarders", value=(len(ctx.message.server.members) - 3))
    embed.add_field(name="Number of Channels", value=(len(ctx.message.server.channels)))
    embed.add_field(name="Owner", value=(ctx.message.server.owner))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await client.say(embed=embed)

client.run("")
