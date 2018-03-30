import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import datetime
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import lbry.admins as adminslist
import lbry.ban_command as banc
import lbry.ban_list as banl
import lbry.battery as batt
import lbry.brand as brand_
import lbry.converter as conv
import lbry.easter_eggs as eastereggs
import lbry.input_check as incheck
import lbry.mute_command as mutec
import lbry.mute_list as mutel
import lbry.role_assigner as roleassi
import lbry.store_in_drive as dstore

# Google Sheets
scope = ["https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("C:/Users/Administrator/Dropbox/Coding/Coding Projects/Python/Electric-SkateBot_Server_Test/client_secret.json", scope)
client = gspread.authorize(credentials)
bot = commands.Bot(command_prefix="+")
bot.remove_command("help")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel("342965746948636672")
    server_ = channel.server
    role_to_assign = discord.utils.get(server_.roles, name="Muted")
    if member.id in mutel.muted_users:
        await bot.add_roles(member, role_to_assign)


@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='+help for more info'))
    print("Hi, my name is " + bot.user.name)
    print("My ID is: " + bot.user.id)
    while True:
        # Print Mutes
        mutel.write_to_file()
        print("Mutes List Saved")
        # Role Auto Assigner
        channel = bot.get_channel("425714572981436436")  # Getting the channel where roles are assigned
        tick = {}  # Creating 2 dictionaries for Ticks and Crosses
        cross = {}
        # Reacts Dictionary Creator
        async for x in bot.logs_from(channel, limit=100):
            for reaction in x.reactions:
                reactors = await bot.get_reaction_users(reaction)
                for reactor in reactors:
                    if reactor.id == "425732605342908426":
                        asd = "asd"
                    elif reaction.emoji == "✅":
                        joined = str(reactor.id) + str(x.content)
                        tick.update({str(joined):str(joined)})
                    elif reaction.emoji == "❌":
                        joined = str(reactor.id) + str(x.content)
                        cross.update({str(joined):str(joined)})
        await react_messages(cross, tick)
        print("Roles Assigned")
        tick.clear()
        cross.clear()
        print("Dictionaries Cleared")
        print("Going to sleep for 2 Minutes")
        print(" ")
        # Sleep for 2 minutes then run again
        await asyncio.sleep(120)


async def react_messages(cross, tick):
    channel = bot.get_channel("425714572981436436")
    server_ = channel.server
    async for x in bot.logs_from(channel, limit=100):
        role_name = x.content
        role_to_assign = discord.utils.get(server_.roles, name=role_name)
        for reaction in x.reactions:
            reacts = reaction.emoji
            reactors = await bot.get_reaction_users(reaction)
            for reactor in reactors:
                reactor_name_id = reactor.id
                reactees = server_.get_member(reactor_name_id)
                joined = str(reactor.id) + str(x.content)
                check_in_cross = not(str(joined) in tick)
                check_in_tick = not(str(joined) in cross)
                if reactor.id == "425732605342908426" or reactor.id == "224311966058020875":
                    asd = "asd"
                elif check_in_tick is False and check_in_cross is False:
                    azy = "yza"
                elif (role_to_assign in reactees.roles) and reacts == "❌":
                    await bot.remove_roles(reactees, role_to_assign)
                elif (len(reactees.roles) < 7) and (role_to_assign not in reactees.roles) and reacts == "✅":
                    await bot.add_roles(reactees, role_to_assign)
                else:
                    azy = "yza"


@bot.event  # Help Commands
async def on_message(message):
    # About
    if message.content.upper() == "+ABOUT":
        embed = discord.Embed(title="Hello %s, here's more information on the bot" % (message.author.name), color=0xFF0000)
        embed.add_field(name="Source Code: ", value="https://github.com/armi-ne/python-tests", inline=False)
        embed.add_field(name="More Info: ", value="This bot was created by Armin as a project and aide for the Electric Skateboarding channel. Feel free to look at the source code and should you have any suggestions please feel free to message Armin :)", inline=False)
        embed.add_field(name="Mentions", value="Special thanks to Weinbee, Jinra, NeoZeon (helping with code) and Howser (custom logo)", inline=False)
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.send_message(message.author, embed=embed)
    # Ben Pls
    if message.content.upper() in eastereggs.ben_pls:
        await bot.send_message(message.channel, "<:benpls:382239983240478724>")
    # Brand Help 1
    if message.content.upper() == "+BRANDHELP 1":
        embed = discord.Embed(title="Hello %s, here are a list of Brand's Sub-Commands, Page 1" % (message.author.name), color=0xFF0000)
        embed.add_field(name="+brand acton", value="Acton", inline=True)
        embed.add_field(name="+brand arc", value="Arc Boards", inline=True)
        embed.add_field(name="+brand backfire", value="Backfire", inline=True)
        embed.add_field(name="+brand boosted", value="Boosted", inline=True)
        embed.add_field(name="+brand carvon", value="Carvon", inline=True)
        embed.add_field(name="+brand diyeboard", value="DiyEboard", inline=True)
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.send_message(message.author, embed=embed)
    # Brand Help 2
    if message.content.upper() == "+BRANDHELP 2":
        embed = discord.Embed(title="Hello %s, here are a list of Brand's Sub-Commands, Page 2" % (message.author.name), color=0xFF0000)
        embed.add_field(name="+brand enertion", value="Enertion", inline=True)
        embed.add_field(name="+brand evolve", value="Evolve", inline=True)
        embed.add_field(name="+brand jed", value="Jed Board", inline=True)
        embed.add_field(name="+brand max", value="Max", inline=True)
        embed.add_field(name="+brand meepo", value="Meepo", inline=True)
        embed.add_field(name="+brand metroboard", value="Metroboard", inline=True)
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.send_message(message.author, embed=embed)
    # Brand Help 3
    if message.content.upper() == "+BRANDHELP 3":
        embed = discord.Embed(title="Hello %s, here are a list of Brand's Sub-Commands, Page 3" % (message.author.name), color=0xFF0000)
        embed.add_field(name="+brand onewheel", value="Onewheel", inline=True)
        embed.add_field(name="+brand predator", value="Predator", inline=True)
        embed.add_field(name="+brand pulseboard", value="Pulse Board", inline=True)
        embed.add_field(name="+brand riptide", value="Riptide", inline=True)
        embed.add_field(name="+brand trampa", value="Trampa", inline=True)
        embed.add_field(name="+brand wowgo", value="Wowgo", inline=True)
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.send_message(message.author, embed=embed)
    # Easter Eggs
    if (message.content.upper() == "+EASTER EGGS" or message.content.upper() == "+EASTER EGG" or message.content.upper() == "+EASTEREGG" or message.content.upper() == "+EASTEREGGS"):
        embed = discord.Embed(title="Hello %s, here are a list of easter eggs" % (message.author.name), color=0xFF0000)
        embed.add_field(name="Ben Pls", value="Everyone knows this one", inline=False)
        embed.add_field(name="Moshi Moshi", value="*UserName* Desu", inline=False)
        embed.add_field(name="+Popcorn", value = "Only certain users can use this.")
        embed.add_field(name="@ mention Sophia '@Sofu'", value="You can thank Jinra for this", inline=False)
        embed.add_field(name="Who's your daddy?", value="Want to know who was responsible for the bots birth?", inline=False)
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.send_message(message.author, embed=embed)
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
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.send_message(message.author, embed=embed)
        embed2 = discord.Embed(title="Hello %s" % (message.author.name), color=0xFF0000)
        embed2.add_field(name="Help Messages: ", value="All help messages are sent to PM's to reduce clutter, please check your PM's.")
        embed2.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.send_message(message.channel, embed=embed2)
    # Moshi Moshi
    if message.content.upper() in eastereggs.moshi_moshi:
        await bot.send_message(message.channel, "Electric Skatebot Desu, {} san".format(message.author.name))
    # Popcorn
    if ("344579589592580096" in message.author.id) and message.content.upper() == "+POPCORN":
        await bot.send_message(message.channel, "Get your popcorn here :popcorn:")
    # Sofu
    if ("209852808977973250" in message.raw_mentions):
        await bot.send_message(message.channel, "💸 :bird: T W I T T E R  E N G  M O N E Y :bird: 💸")
    # Who's your daddy?
    if message.content.upper() in eastereggs.whos_your_daddy:
        await bot.send_message(message.channel, "Armin Senpai")
    await bot.process_commands(message)


@bot.command(pass_context=True)  # +adminhelp
async def admin(ctx, help=None):
    if (ctx.message.author.id in adminslist.admin_id) is False:
        embed = discord.Embed(title="Hello %s" % (ctx.message.author.name), color=0xFF0000)
        embed.add_field(name=">:(", value="You're not an admin :(", inline=True)
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.say(embed=embed)
    elif help is None and ctx.message.author.id in adminslist.admin_id:
        embed = discord.Embed(title="Hello %s, here's the available Admin Commands" % (ctx.message.author.name), color=0xFF0000)
        embed.add_field(name="Ban", value="Use \"+admin ban\" for more info", inline=False)
        embed.add_field(name="Clear", value="Use \"+admin clear\" for more info", inline=False)
        embed.add_field(name="Mute", value="Use \"+admin mute\" for more info", inline=False)
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.say(embed=embed)
    elif help == "ban":
        embed = discord.Embed(title="Hello %s, here's more information on +ban" % (ctx.message.author.name), color=0xFF0000)
        embed.add_field(name="+ban #user# #reason#", value="The ban function will ban the user in question.")
        embed.add_field(name="+unban #userid#", value="The unban function will unban the user in question.")
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.say(embed=embed)
    elif help == "clear":
        embed = discord.Embed(title="Hello %s, here's more information on +clear" % (ctx.message.author.name), color=0xFF0000)
        embed.add_field(name="+clear #number of messages#", value="The clear function will delete 2-40 messages, specified by the admin")
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.say(embed=embed)
    elif help == "mute" and ctx.message.author.id in adminslist.admin_id:
        embed = discord.Embed(title="Hello %s, here's more information on +mute" % (ctx.message.author.name), color=0xFF0000)
        embed.add_field(name="+mute #user# #duration# #reason#", value="The mute function allows you to mute a certain user for a specific period of time. Make sure you include the duration and reason.", inline=False)
        embed.add_field(name="+unmute #user#", value="The unmute function allows you to remove the \"Muted\" role from a certain user", inline=False)
        embed.add_field(name="+mutelist", value="The mutelist function will provide the user ID's of currently muted users", inline=False)
        embed.add_field(name="+printmute #user#", value="The printmute function will provide more information on a mute incident, if the mute is still Active", inline=False)
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.say(embed=embed)


@bot.command(pass_context = True)  # +ban
async def ban(ctx, member: discord.Member, codeblock=None, *reason):
    checkanswer = banc.checks(codeblock)  # Checks input
    time = datetime.datetime.now()
    import_time = time.strftime("%D, %H:%M:%S")
    if ctx.message.author.id in adminslist.admin_id and checkanswer == "Correct":
        await bot.ban(member, delete_message_days=6)
        reason = banc.reason(codeblock, reason)
        banned_Name, banned_By, banned_Time, banned_Reason = banl.mute_data_formatter(member.name, ctx.message.author.name,  import_time, reason)
        banned_ID = str(member.id)
        embed = discord.Embed(title="User Banned!", description="**{0}** was banned by **{1}**!".format(banned_Name, banned_By), color=0xFF0000)
        embed.add_field(name="Reason", value=banned_Reason)
        embed.add_field(name="User ID: ", value=banned_ID)
        embed.add_field(name="Time of Banning", value=banned_Time)
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.say(embed=embed)  # Sending to message where command was incited
        await bot.send_message(bot.get_channel(id='371587856042557440'), embed=embed)  # Sending to automod log channel
    elif checkanswer == "Missing Reason":
        embed = discord.Embed(title="No Reason.", description="Please include the ban reason", color=0xFF0000)
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.say(embed=embed)
    else:
        embed = discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xFF0000)
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.say(embed=embed)


@bot.command(pass_context=True)  # +unban
async def unban(ctx, userarg1):
    user_to_unban = await bot.get_user_info(userarg1)
    if ctx.message.author.id in adminslist.admin_id:
        await bot.unban(ctx.message.server, user_to_unban)
        embed = discord.Embed(title="User Unbanned!", description="**{0}** was unbanned by **{1}**!".format(user_to_unban.name, ctx.message.author), color=0xFF0000)
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.say(embed=embed)
        await bot.send_message(bot.get_channel(id='371587856042557440'), embed=embed)
    else:
        embed = discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xFF0000)
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.say(embed=embed)


@bot.command(pass_context=True)  # +battery
async def battery(ctx, series=None, parallel=None, amphour=None, codeblock=None):
    checkanswer = incheck.batterycheck(series, parallel, amphour, codeblock)
    if checkanswer == "NoValues":  # No arguments
        embed = discord.Embed(title="Hello %s, here's an explanation of how the +battery command works" % (ctx.message.author.name), color=0xFF0000)
        embed.add_field(name="Usage:", value="In order to make use of this command you are first required to have 3 pieces of information. 1) Series count. 2) Parallel count. 3) Amp hours per cell.")
        embed.add_field(name="Command Format:", value="+battery #Series value# #Parallel value# #Amp Hour value#")
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.send_message(ctx.message.author, embed=embed)
        embed2 = discord.Embed(title="Hello %s" % (ctx.message.author.name), color=0xFF0000)
        embed2.add_field(name="Help Messages: ", value="All help messages are sent to PM's to reduce clutter, please check your PM's.")
        embed2.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.say(embed=embed2)
    elif checkanswer == "TypeError":  # Type Error
        embed = discord.Embed(title="Electric SkateBot Battery Calculator", color=0xFF0000)
        embed.add_field(name="Arguments Error:", value="Please input numbers.", inline=True)
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.say(embed=embed)
    elif checkanswer == "NoDecimals":  # Series and Parallel whole numbers check
        embed = discord.Embed(title="Electric SkateBot Battery Calculator", color=0xFF0000)
        embed.add_field(name="Series/Parallel Error:", value="Sorry but Series and Parallel only accept whole numbers.", inline=True)
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.say(embed=embed)
    elif checkanswer == "Correct":  # Correct Input
        total_amphour, total_watthour, total_range_km, total_range_mi, total_nominal_voltage = batt.executer(series, parallel, amphour)
        embed = discord.Embed(title="Electric SkateBot Battery Calculator", color=0xFF0000)
        embed.add_field(name="In Series:", value=series + "s", inline=True)
        embed.add_field(name="In Parallel:", value=parallel + "p", inline=True)
        embed.add_field(name="In Amp Hours:", value="%0.2f" % float(amphour) + "ah", inline=True)
        embed.add_field(name="Nominal Voltage of Pack:", value="{0:.2f}".format(float(total_nominal_voltage)) + "v", inline=False)
        embed.add_field(name="Total Amp Hours:", value="{0:.2f}".format(float(total_amphour)) + "ah", inline=False)
        embed.add_field(name="Total Watt Hours:", value="{0:.2f}".format(float(total_watthour)) + "wh", inline=False)
        embed.add_field(name="Estimated Ranges:", value="{0:.2f}".format(float(total_range_km)) + "km, or " + "{0:.2f}".format(float(total_range_mi)) + "mi")
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.say(embed=embed)
    elif checkanswer == "TooMany":  # Too many arguments
        embed = discord.Embed(title="Electric SkateBot Battery Calculator", color=0xFF0000)
        embed.add_field(name="Arguments Error:", value="Sorry but the bot only accepts 3 inputs which are: Series, Parallel and AmpHours.", inline=True)
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.say(embed=embed)
    elif checkanswer == "ValuesTooHigh":  # Values given are too high
        embed = discord.Embed(title="Electric SkateBot Battery Calculator", color=0xFF0000)
        embed.add_field(name="Value length error:", value="Sorry but the bot only accepts values from 0-99 for each field.", inline=True)
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.say(embed=embed)
    else:  # Just in case
        embed = discord.Embed(title="Hello %s, here's an explanation of how the +battery command works" % (ctx.message.author.name), color=0xFF0000)
        embed.add_field(name="Usage:", value="In order to make use of this command you are first required to have 3 pieces of information. 1) Series count. 2) Parallel count. 3) Amp hours per cell.")
        embed.add_field(name="Command Format:", value="+battery #Series value# #Parallel value# #Amp Hour value#")
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.send_message(ctx.message.author, embed=embed)
        embed2 = discord.Embed(title="Hello %s" % (ctx.message.author.name), color=0xFF0000)
        embed2.add_field(name="Help Messages: ", value="All help messages are sent to PM's to reduce clutter, please check your PM's.")
        embed2.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.say(embed=embed2)


@bot.command(pass_context=True)  # +brand
async def brand(ctx, brandin=None):
    if brandin is not None:
        upcase1 = brandin.upper()
        website, email, facebook, reddit, thumbnail = brand_.brandfinder(upcase1)
        embed = discord.Embed(title="%s's Info" % brandin.capitalize(), color=0xFF0000)
        embed.add_field(name="Website: ", value=website, inline=True)
        embed.add_field(name="Email: ", value=email, inline=True)
        embed.add_field(name="Facebook: ", value=facebook, inline=False)
        embed.add_field(name="Reddit: ", value=reddit, inline=False)
        embed.set_thumbnail(url=thumbnail)
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.say(embed=embed)
    else:
        embed = discord.Embed(title="Hello %s, here's an explanation of how the +brand command works" % (ctx.message.author.name), color=0xFF0000)
        embed.add_field(name="Command Format: ", value="+brand #brand#")
        embed.add_field(name="List of Brands Available: ", value="Please use +brandhelp 1/2/3 for the corresponding pages of brands we have available")
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.send_message(ctx.message.author, embed=embed)


@bot.command(pass_context = True)  # +clear
async def clear(ctx, number):
    if ctx.message.author.id in adminslist.admin_id and int(number) < 101:
        mgs = []  # Creates an empty list to place all the message objects
        number = int(number)  # Converts the number string into an int
        async for x in bot.logs_from(ctx.message.channel, limit = number):  # For each message sent, with a limit defined by the number
            mgs.append(x)  # Adds the message to be deleted to the mgs list
        await bot.delete_messages(mgs)  # Deletes the messages in the mgs list
        dstore.upload_to_drive_new(ctx, mgs)  # Runs the function to store the deleted messages and their information on google drive
    elif int(number) >= 101:
        embed = discord.Embed(title="Clear", color=0xFF0000)
        embed.add_field(name= "Too Many Messages", value="Sorry but the bot can only delete 2-100 messages at a time")
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.say(embed=embed)
    else:
        await bot.say("No :(")


@bot.command(pass_context=True)  # +convert
async def convert(ctx, inputval=None, inputuni=None, to_text=None, desireduni=None, codeblock=None):
    checkanswer = incheck.convertercheck(inputval, inputuni, to_text, desireduni, codeblock)
    if checkanswer == "NoInput":  # No Arguments
        embed = discord.Embed(title="Hello %s, here's an explanation of how the +convert command works" % (ctx.message.author.name), color=0xFF0000)
        embed.add_field(name="Command Format: ", value="Use \"+convert #Number# #Unit# #to# #Desired Unit#\"")
        embed.add_field(name="Current Conversion Pairs: ", value="kph <-> mph｜km <-> mi｜cm <-> inch｜km <- Wh -> mi")
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.send_message(ctx.message.author, embed=embed)
        embed2 = discord.Embed(title="Hello %s" % (ctx.message.author.name), color=0xFF0000)
        embed2.add_field(name="Help Messages: ", value="All help messages are sent to PM's to reduce clutter, please check your PM's.")
        embed2.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.say(embed=embed2)
    elif checkanswer == "TypeError":  # Type Error
        embed = discord.Embed(title="Electric SkateBot Battery Calculator", color=0xFF0000)
        embed.add_field(name="Arguments Error:", value="Please input numbers and letters where requested.", inline=True)
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.say(embed=embed)
    elif checkanswer == "Correct":  # Correct Input
        upcase1, upcase2, upcase4 = inputval.upper(), inputuni.upper(), desireduni.upper()
        answer = conv.executer(float(upcase1), upcase2, upcase4)
        embed = discord.Embed(title="Electric SkateBot Converter", color=0xFF0000)
        embed.add_field(name="Input Value:", value=inputval, inline=True)
        embed.add_field(name="Input Unit:", value=inputuni, inline=True)
        embed.add_field(name="Output Unit:", value=desireduni, inline=False)
        embed.add_field(name="Result", value=answer, inline=False)
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.say(embed=embed)
    elif checkanswer == "TooMany":  # Too Many Arguments
        embed = discord.Embed(title="Electric SkateBot Converter", color=0xFF0000)
        embed.add_field(name="Arguments Error:", value="Sorry but the bot only accepts 4 inputs which are: inputValue, inputUnit, \"to\" and DesiredUnit.", inline=True)
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.say(embed=embed)
    else:  # Just in case
        embed = discord.Embed(title="Hello %s, here's an explanation of how the +convert command works" % (ctx.message.author.name), color=0xFF0000)
        embed.add_field(name="Command Format: ", value="Use \"+convert #Number# #Unit# #to# #Desired Unit#\"")
        embed.add_field(name="Current Conversion Pairs: ", value="kph <-> mph｜km <-> mi｜cm <-> inch｜km <- Wh -> mi")
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.send_message(ctx.message.author, embed=embed)
        embed2 = discord.Embed(title="Hello %s" % (ctx.message.author.name), color=0xFF0000)
        embed2.add_field(name="Help Messages: ", value="All help messages are sent to PM's to reduce clutter, please check your PM's.")
        embed2.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.say(embed=embed2)


@bot.command(pass_context = True)  # +mute
async def mute(ctx, member: discord.Member, codeblock=None, *reason):
    checkanswer = mutec.checks(codeblock)  # Checks input
    time = datetime.datetime.now()
    import_time = time.strftime("%D, %H:%M:%S")
    if ctx.message.author.id in adminslist.admin_id and checkanswer == "Correct":  # If input matches requirements
        duration_in_min, reason_final = mutec.duration_and_reason(codeblock, reason)  # Gets the duration in minutes and the reason
        role = discord.utils.get(member.server.roles, name='Muted')  # Gets the role we're adding
        await bot.add_roles(member, role)  # Adds the mute role
        muted_Name, muted_By, muted_Duration, muted_Time, muted_Reason = mutel.mute_data_formatter(member.name, ctx.message.author.name, codeblock, import_time, reason_final)
        mutel.list_add(member. id, muted_Name, muted_By, muted_Duration, muted_Time, muted_Reason)
        embed = discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xFF0000)
        embed.add_field(name="Reason", value=reason_final)
        embed.add_field(name="Duration", value=str(codeblock) + " Minute(s)")
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.say(embed=embed)  # Sending to message where command was incited
        await bot.send_message(bot.get_channel(id='371587856042557440'), embed=embed)  # Sending to automod log channel
        await asyncio.sleep(duration_in_min)  # Waiting the duration until mute role is removed
        await bot.remove_roles(member, role)
        embed2 = discord.Embed(title="User Unmuted!", description="**{0}** was unmuted by Electric Skatebot!".format(member), color=0xFF0000)
        embed2.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.send_message(bot.get_channel(id='371587856042557440'), embed=embed2)
        del mutel.muted_users[member.id]
    elif checkanswer == "Missing Time":
        embed = discord.Embed(title="No Time.", description="Please include the mute duration (in minute(s))", color=0xFF0000)
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.say(embed=embed)
    else:
        embed = discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xFF0000)
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.say(embed=embed)


@bot.command(pass_context = True)  # +unmute
async def unmute(ctx, member: discord.Member):
    if ctx.message.author.id in adminslist.admin_id:
        role = discord.utils.get(member.server.roles, name='Muted')
        await bot.remove_roles(member, role)
        embed = discord.Embed(title="User Unmuted!", description="**{0}** was unmuted by **{1}**!".format(member, ctx.message.author), color=0xFF0000)
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.say(embed=embed)
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.send_message(bot.get_channel(id='371587856042557440'), embed=embed)
        del mutel.muted_users[member.id]
    else:
        embed = discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xFF0000)
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.say(embed=embed)


@bot.command(pass_context=True)  # +printmutes
async def printmute(ctx, member: discord.Member):
    embed = discord.Embed(name="Mute List", description="", color=0xFF0000)
    embed.add_field(name="Username: ", value=mutel.muted_users[member.id][0], inline=True)
    embed.add_field(name="Muted By: ", value=mutel.muted_users[member.id][1], inline=True)
    embed.add_field(name="Duration: ", value=mutel.muted_users[member.id][2], inline=True)
    embed.add_field(name="Time: ", value=mutel.muted_users[member.id][3], inline=True)
    embed.add_field(name="Reason: ", value=mutel.muted_users[member.id][4], inline=False)
    embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
    await bot.say(embed=embed)


@bot.command(pass_context=True)  # +mutelist
async def mutelist(ctx):
    embed = discord.Embed(name="Mute List", description="Current Muted Users", color=0xFF0000)
    embed.add_field(name="ID's", value=mutel.muted_list())
    embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
    await bot.say(embed=embed)


@bot.command(pass_context=True)  # +server
async def server(ctx):
    raw_creation_time = ctx.message.server.created_at
    formatted_time = raw_creation_time.strftime("%D, %H:%M:%S")
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="", color=0xFF0000)
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="Number of e-Boarders", value=(len(ctx.message.server.members) - 3))
    embed.add_field(name="Number of Channels", value=(len(ctx.message.server.channels)))
    embed.add_field(name="Owner", value=(ctx.message.server.owner))
    embed.add_field(name="Created: ", value=formatted_time)
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
    await bot.say(embed=embed)


bot.run("")
