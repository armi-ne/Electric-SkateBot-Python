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
import lbry.ban_formatter as banf
import lbry.battery as batt
import lbry.brand as brand_
import lbry.converter as conv
import lbry.easter_eggs as eastereggs
import lbry.input_check as incheck
import lbry.mute as mutem
import lbry.regions as regions
import lbry.roles as roles_list
import lbry.store_in_drive as dstore

# Google Sheets
scope = ["https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("C:/Users/Administrator/Dropbox/Coding/Coding Projects/Python/Electric-SkateBot/client_secret.json", scope)
client = gspread.authorize(credentials)
bot = commands.Bot(command_prefix="+") # Setting the prefix for the bot
bot.remove_command("help") # Removing the default help command


@bot.event
async def on_member_join(member): # When a member joins, run mute checks
    channel = bot.get_channel("342965746948636672") # Getting channel info, so we can get server info later
    server_ = channel.server # Getting server info using channel
    role_to_assign = discord.utils.get(server_.roles, name="Muted") # Getting the role to assign
    if member.id in mutem.mutesdic: # If the users ID is in the mutes dictionary
        unmuted_on = mutem.mutesdic[member.id][1] # Getting the time they're supposed to be unmuted at
        parsed = datetime.datetime.strptime(unmuted_on, "%Y-%m-%d %H:%M:%S") # Changing from string to a datetime object
        if (datetime.datetime.now()) < parsed: # If the time now is before when they're supposed to be unmuted
            await bot.add_roles(member, role_to_assign) # Add mute role


@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='+help for more info')) # Changes bots presence information to display "+help for more info"
    print("Hi, my name is " + bot.user.name)
    print("My ID is: " + bot.user.id)
    mutem.mutes_check() # Run the mutes check function in the mute_main file
    time_when_launched = str(datetime.datetime.now())
    await mutes_checker() #Check and unmute any users who should not be muted, or await however long it'll take and unmute them on time
    while True:
        time = str(datetime.datetime.now())
        await react_messages() # Role auto assigner
        await react_messages_regions() # Regions auto assigner
        print("Dictionaries Cleared")
        print("Launched on: " + time_when_launched)
        print("Time is: " + time)
        print("Going to sleep for 40 Minutes")
        print(" ")
        await asyncio.sleep(2400) # Sleep for 40 minutes then run again


async def mutes_checker():
    channel = bot.get_channel("425714572981436436") # Get Channel
    server = channel.server # Get Server
    for key, value in mutem.mutesdic.items(): # For each member and information provided in mutes dictionary.
        time_now = datetime.datetime.now() # Get time right now
        unmuted_on = value[1] # When they'll be unmuted, loaded as a string from same list in dictionary as muted_on.
        unmuted_on_parsed = datetime.datetime.strptime(unmuted_on, "%Y-%m-%d %H:%M:%S") # Turn unmuted_on from a string into a datetime object.
        member = server.get_member(key) # Get the member object using the server get_member function using the User ID provided from they Key of each dictionary entry.
        role = discord.utils.get(member.server.roles, name='Muted') # Get the role to  
        if (unmuted_on_parsed < time_now) and role in member.roles: # If the time now has passed the unmute time and the user has the muted role, remove the role.
            await bot.remove_roles(member, role)
        elif (unmuted_on_parsed < time_now) and role not in member.roles: # If the time now has passed the unmute time but the user doesn't have the muted role, continue.
            continue
        elif (unmuted_on_parsed > time_now) and role in member.roles: # If the time now hasn't passed the unmute time and the user still has the muted role.
            time_left = unmuted_on_parsed - time_now # Time left calculated by subtracting time now from unmute_time
            time_left_seconds = time_left.total_seconds() # Time left turned into seconds for use with asyncio.sleep() function
            if key is not None: # If the key is not a nonetype (user ID exists)
                time_left_seconds2 = str(time_left_seconds).split('.')[0] # Time left in seconds is now stripped of anything passed the decimal point, turning it into a whole number for ease of use.
                await bot.send_message(bot.get_channel(id='371587856042557440'), "+unmutebot " + str(key) + " " + str(time_left_seconds2)) # Bot invokes the +unmutebot on_message command
        elif role not in member.roles: # If the bot/admins had previously removed the role, continue.
            continue
        await asyncio.sleep(10) # Sleep for 10 seconds before going to next user, this is so the on_message part of the bot has enough time to cycle through it's process.


async def react_messages():
    channel = bot.get_channel("425714572981436436") #Get Channel ID and assign to Channel variable.
    server_ = channel.server #Get the server via channel which was defined before.
    tick = {} # Create two empty dictionaries for users who will have reacted with a cross or a tick.
    cross = {} # Create two empty dictionaries for users who will have reacted with a cross or a tick.
    async for x in bot.logs_from(channel, limit=100): # Get the last 100 messages in the channel.
        role_name = x.content # Assign the role_name that we'll use as the content of the message.
        role_to_assign = discord.utils.get(server_.roles, name=role_name) # Using the role_name we will now get the role object to assign.
        for reaction in x.reactions: # For each reaction in each message's reactions.
            reacts = reaction.emoji # Assign the reaction emoji (either the tick or cross) to reacts.
            reactors = await bot.get_reaction_users(reaction) # Get user objects for each reactor and assign them to the reactors variable.
            for reactor in reactors: # For each reactor in reactors.
                if reaction.emoji == "✅": # If the reaction emoji is a tick.
                    joined = str(reactor.id) + str(x.content)
                    tick.update({str(joined):str(joined)}) # Format the data to input and add the relevant information (user_ID and role) to the ticks dictionary.
                elif reaction.emoji == "❌": # If the reaction emoji is a cross.
                    joined = str(reactor.id) + str(x.content)
                    cross.update({str(joined):str(joined)}) # Format the data to input and add the relevant information (user_ID and role) to the cross dictionary.
                else:
                    continue
                # Now the bot will cycle through multiple if statements in order to decide whether or not to skip a user or assign/remove the role in question
                reactor_name_id = reactor.id
                reactees = server_.get_member(reactor_name_id)
                if reactees == None:
                    continue
                if reactor.id == "417386039691182080":
                    continue
                joined = str(reactor.id) + str(x.content)
                check_in_cross = not(str(joined) in tick)
                check_in_tick = not(str(joined) in cross)
                if check_in_tick is False and check_in_cross is False:
                    continue
                elif check_in_tick is True and check_in_cross is True:
                    continue
                elif (role_to_assign in reactees.roles) and reacts == "❌":
                    await bot.remove_roles(reactees, role_to_assign)
                elif (len(reactees.roles) < 11) and (role_to_assign not in reactees.roles) and reacts == "✅":
                    await bot.add_roles(reactees, role_to_assign)
                else:
                    continue
                tick.clear()
                cross.clear() 


async def react_messages_regions(): # Same concept as reaction roles assigner but with a different channel
    channel = bot.get_channel("470635791110897674")
    server_ = channel.server
    tick = {}
    cross = {}
    async for x in bot.logs_from(channel, limit=100):
        role_name = x.content
        role_to_assign = discord.utils.get(server_.roles, name=role_name)
        for reaction in x.reactions:
            reacts = reaction.emoji
            reactors = await bot.get_reaction_users(reaction)
            for reactor in reactors:
                if reaction.emoji == "✅":
                    joined = str(reactor.id) + str(x.content)
                    tick.update({str(joined):str(joined)})
                elif reaction.emoji == "❌":
                    joined = str(reactor.id) + str(x.content)
                    cross.update({str(joined):str(joined)})
                else:
                    continue
                reactor_name_id = reactor.id
                reactees = server_.get_member(reactor_name_id)
                if reactees == None:
                    continue
                if reactor.id == "425732605342908426" or reactor.id == "224311966058020875" or reactor.id == "417386039691182080":
                    continue
                joined = str(reactor.id) + str(x.content)
                check_in_cross = not(str(joined) in tick)
                check_in_tick = not(str(joined) in cross)
                if check_in_tick is False and check_in_cross is False:
                    continue
                elif check_in_tick is True and check_in_cross is True:
                    continue
                elif (role_to_assign in reactees.roles) and reacts == "❌":
                    await bot.remove_roles(reactees, role_to_assign)
                elif (len(reactees.roles) < 11) and (role_to_assign not in reactees.roles) and reacts == "✅":
                    await bot.add_roles(reactees, role_to_assign)
                else:
                    continue
                tick.clear()
                cross.clear()


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
    # Unmutebot
    if message.content.startswith("+unmutebot") and message.author.id == "417386039691182080":
        prefix_and_command, ID, time_to_wait = message.content.split(" ")
        channel = bot.get_channel("425714572981436436")
        server = channel.server
        member = server.get_member(ID)
        role = discord.utils.get(member.server.roles, name='Muted')
        embed = discord.Embed(title="User Will Be Unmuted!", description="**{0}** will be unmuted by **{1}** in **{2}** minutes!".format(member.name, message.author.name, str(int(int(time_to_wait)/60))), color=0xFF0000)
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.send_message(bot.get_channel(id='371587856042557440'), embed=embed)
        mgs = []  # Creates an empty list to place all the message objects
        number = (2)  # Converts the number string into an int
        async for x in bot.logs_from(message.channel, limit = number):  # For each message sent, with a limit defined by the number
            mgs.append(x)  # Adds the message to be deleted to the mgs list
        await asyncio.sleep(2)
        await bot.delete_messages(mgs)
        await asyncio.sleep(2)
        await bot.send_message(bot.get_channel(id='371587856042557440'), embed=embed)
        await asyncio.sleep(int(time_to_wait))
        await bot.remove_roles(member, role)
        embed = discord.Embed(title="User Unmuted!", description="**{0}** was unmuted by **{1}**!".format(member.name, message.author.name), color=0xFF0000)
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.say(embed=embed)
        await bot.send_message(bot.get_channel(id='371587856042557440'), embed=embed)
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
        embed.add_field(name="+ban #user# #number of days worth of messages to delete# #reason#", value="The ban function will ban the user in question.")
        embed.add_field(name="+unban #userid#", value="The unban function will unban the user in question.")
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.say(embed=embed)
    elif help == "clear":
        embed = discord.Embed(title="Hello %s, here's more information on +clear" % (ctx.message.author.name), color=0xFF0000)
        embed.add_field(name="+clear #number of messages#", value="The clear function will delete 1-100 messages, specified by the admin")
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.say(embed=embed)
    elif help == "mute" and ctx.message.author.id in adminslist.admin_id:
        embed = discord.Embed(title="Hello %s, here's more information on +mute" % (ctx.message.author.name), color=0xFF0000)
        embed.add_field(name="+mute #user# #duration# #reason#", value="The mute function allows you to mute a certain user for a specific period of time. Make sure you include the duration and reason.", inline=False)
        embed.add_field(name="+unmute #user#", value="The unmute function allows you to remove the \"Muted\" role from a certain user", inline=False)
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.say(embed=embed)


@bot.command(pass_context = True)  # +ban
async def ban(ctx, member: discord.Member, codeblock=None, *reason):
    checkanswer = banc.checks(codeblock)  # Checks input
    time = datetime.datetime.now()
    import_time = time.strftime("%D, %H:%M:%S")
    if ctx.message.author.id in adminslist.admin_id and codeblock.isnumeric() and int(codeblock)<=7 and checkanswer == "Correct":
        await bot.ban(member, delete_message_days=int(codeblock))
        reason = banc.reason(reason)
        banned_Name, banned_By, banned_Time, banned_Reason = banf.ban_data_formatter(member.name, ctx.message.author.name,  import_time, reason)
        banned_ID = str(member.id)
        embed = discord.Embed(title="User Banned!", description="**{0}** was banned by **{1}**!".format(banned_Name, banned_By), color=0xFF0000)
        embed.add_field(name="Reason", value=banned_Reason)
        embed.add_field(name="User ID: ", value=banned_ID)
        embed.add_field(name="Time of Banning", value=banned_Time)
        embed.add_field(name="Deleted Message Days", value=str(codeblock))
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.say(embed=embed)  # Sending to message where command was incited
        await bot.send_message(bot.get_channel(id='371587856042557440'), embed=embed)  # Sending to automod log channel
    elif ctx.message.author.id not in adminslist.admin_id:
        embed = discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xFF0000)
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.say(embed=embed)
    elif not codeblock.isnumeric():
        embed = discord.Embed(title="Please input # of days worth of messages you'd like to delete.", description="+ban @user #days worth of messages to delete# reason", color=0xFF0000)
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.say(embed=embed)
    elif int(codeblock)>=8:
        embed = discord.Embed(title="Deleted Message Days value too high", description="You can only delete up to 7 days worth of messages. Please ammend.", color=0xFF0000)
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.say(embed=embed)
    elif checkanswer == "Missing Reason":
        embed = discord.Embed(title="No Reason or Message Deletion Date.", description="Please include the ban reason / # of days worth of messages you'd like to delete.", color=0xFF0000)
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
        number = (int(number) + 1)  # Converts the number string into an int
        async for x in bot.logs_from(ctx.message.channel, limit = number):  # For each message sent, with a limit defined by the number
            mgs.append(x)  # Adds the message to be deleted to the mgs list
        await bot.delete_messages(mgs)  # Deletes the messages in the mgs list
        dstore.upload_to_drive_new(ctx, mgs)  # Runs the function to store the deleted messages and their information on google drive
    elif int(number) >= 101:
        embed = discord.Embed(title="Clear", color=0xFF0000)
        embed.add_field(name= "Too Many Messages", value="Sorry but the bot can only delete 1-100 messages at a time")
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
    checkanswer = mutem.checks(codeblock)
    #Get all time data
    day = time.strftime("%D")
    month, day, year_not_final = day.split("/")
    year = "20" + str(year_not_final)
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    time_and_date = [hour, minute, second, day, month, year]
    duration_seconds = int(codeblock)*60
    if ctx.message.author.id in adminslist.admin_id and checkanswer == "Correct":  # If input matches requirements
        reason_final = mutem.reason(reason)
        role = discord.utils.get(member.server.roles, name='Muted')  # Gets the role we're adding
        await bot.add_roles(member, role)  # Adds the mute role
        mutem.mute_main_function(member.id, member.name, ctx.message.author.name, duration_seconds, time_and_date, reason_final)
        embed = discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xFF0000)
        embed.add_field(name="Reason", value=reason_final)
        embed.add_field(name="Duration", value=str(codeblock) + " Minute(s)")
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.say(embed=embed)  # Sending message to where command was incited
        await bot.send_message(bot.get_channel(id='371587856042557440'), embed=embed)  # Sending to automod log channel
        await asyncio.sleep(duration_seconds)  # Waiting the duration until mute role is removed
        await bot.remove_roles(member, role)
        embed2 = discord.Embed(title="User Unmuted!", description="**{0}** was unmuted by Electric Skatebot!".format(member), color=0xFF0000)
        embed2.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.send_message(bot.get_channel(id='371587856042557440'), embed=embed2)
    elif checkanswer == "Time given not number":
        embed = discord.Embed(title="No Time.", description="Time given not number", color=0xFF0000)
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.say(embed=embed)
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
        await bot.send_message(bot.get_channel(id='371587856042557440'), embed=embed)
    else:
        embed = discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xFF0000)
        embed.set_footer(text="Electric SkateBot", icon_url="https://i.imgur.com/L38PKZR.png")
        await bot.say(embed=embed)


@bot.command(pass_context = True)  # +roleupdate
async def roles(ctx):
    channel = bot.get_channel("425714572981436436")
    server_ = channel.server
    if ctx.message.author.id in adminslist.admin_id:    #Check if user is Admin
        number = 200    #Limit of messages to be deleted
        counter = 0     #Counter of how many messages have been deleted 1-by-1 so far
        role_counter = 0        #Can't put it into words but this makes sure the second for loops (role duplicate checker) work, so don't delete it.
        async for x in bot.logs_from(ctx.message.channel, limit = number):  # For each message sent, with a limit defined by the number
            if counter<number:  #If counter of deleted messages is lower than limit, carry on deleting
                await bot.delete_message(x) 
                counter += 1
                await asyncio.sleep(1.5)
        for role in roles_list.roles:   #For each role in role list, if the role doesn't exist already, create a new one, else, add to the counter
            role_to_check = discord.utils.get(server_.roles, name=role)
            if role_to_check in server_.roles:
                 role_counter += 1
            else:
                await bot.create_role(server_, name = str(role))
            react_message = await bot.say(str(role)) #Assigning the message to post of role name to a variable, and posting the role name message
            await bot.add_reaction(react_message, "✅")  #Adding tick react to message
            await bot.add_reaction(react_message, "❌")  #Adding cross react to message
            await asyncio.sleep(2)  #Sleep for 2 seconds so no rate limiting
    else:
        print("error")


@bot.command(pass_context = True)  # +regions update
async def regionsup(ctx):
    channel = bot.get_channel("470635791110897674")
    server_ = channel.server
    if ctx.message.author.id in adminslist.admin_id:    #Check if user is Admin
        number = 200    #Limit of messages to be deleted
        counter = 0     #Counter of how many messages have been deleted 1-by-1 so far
        role_counter = 0        #Can't put it into words but this makes sure the second for loops (role duplicate checker) work, so don't delete it.
        async for x in bot.logs_from(ctx.message.channel, limit = number):  # For each message sent, with a limit defined by the number
            if counter<number:  #If counter of deleted messages is lower than limit, carry on deleting
                await bot.delete_message(x) 
                counter += 1
                await asyncio.sleep(1.5)
        for role in regions.regions_list:   #For each role in role list, if the role doesn't exist already, create a new one, else, add to the counter
            role_to_check = discord.utils.get(server_.roles, name=role)
            if role_to_check in server_.roles:
                 role_counter += 1
            else:
                await bot.create_role(server_, name = str(role))
            react_message = await bot.say(str(role)) #Assigning the message to post of role name to a variable, and posting the role name message
            await bot.add_reaction(react_message, "✅")  #Adding tick react to message
            await bot.add_reaction(react_message, "❌")  #Adding cross react to message
            await asyncio.sleep(2)  #Sleep for 2 seconds so no rate limiting
    else:
        print("error")


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
