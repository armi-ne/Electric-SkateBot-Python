# Update 3.6, 15/03/2018
_____________________________________________________________________________
Modified Commands:
1) +battery

 a) Modified and implemented optional variables and a help "error" message, please read under "more info" tab.

2) +convert

 a) Modified and implemented optional variables and a help "error" message, please read under "more info" tab.

3) +help
 
 a) Adjusted the message to reflect changes in the +battery and +convert functions
_____________________________________________________________________________
More Info:
In regards to the +battery and +convert command, through the use of optional variables and evaluating multiple variables using one if statement (https://stackoverflow.com/questions/9504638/evaluate-multiple-variables-in-one-if-statement) now when users don't provide the required number of arguments the bot will instead send the user a PM detailing how to properly use the command.

Example:

@client.command(pass_context=True)

async def test(ctx, var1=None, var2=None):

    if all((var1, var2)):
    
        var3 = str(var1) + str(var2)
        
        await client.say(var3)
        
    else:
    
        await client.say("Please can you input 2 values")
        
_____________________________________________________________________________
Date 05/03/2018

Total hours spent learning python: 98

Total days spend learning python: 18

# Update 3.5, 09/03/2018
_____________________________________________________________________________
Other Changes:
 1) Rewritten files
  - Brand
  - Battery
  - Converter
  - Bot.py
 2) Details
  - Brand has been shortened and values have all been moved into a list within a dictionary.
  - Battery had had it's variables changed and some calculations reworded.
  - Converter has had all of its code re-written and now uses all the variables.
  - Bot.py had been re-written to make more use of client.command instead of client.event, although both are still used.
_____________________________________________________________________________
Date 09/03/2018

Total hours spent learning python: 74

Total days spend learning python: 12

# News Announcement, 07/03/2018
_____________________________________________________________________________
After receiving feedback on the bot and code, I've decided it would be for the best to stop adding any new features for the time being and instead create a new branch with all the good changes that have been advised.

# Update 3.4.2, 06/03/2018
_____________________________________________________________________________
Other Changes:
 - Added a wiki page showing each command accompanied by an image of the bots response

# Update 3.4.1, 06/03/2018
_____________________________________________________________________________
Other Changes:
- Modified "+battery" command to take inputs in the order of (S, P, Ah, Volt) instead of (P, S, Ah, Volt)

- Modified the +batteryhelp command to show this change in input

# Update 3.4, 06/03/2018
_____________________________________________________________________________
Added Commands:
1) +battery
2) +batteryhelp

"+battery" takes 4 inputs and returns an "embed" formatted message with 8 total values.

"+batteryhelp" pm's user a messsage detailing how to use the "+battery" command
_____________________________________________________________________________
Modified Commands:
1) +about
 
 a) Added a "mentions" field crediting Jinra, Weinbee, Neozeon and Howser for their help

2) +help, +easter eggs

 a) Alphabetically sorted
_____________________________________________________________________________
Other Changes:
- Added new "battery.py" library in the "lbry" folder

- Removed colons at the end of every title for commands.
_____________________________________________________________________________
Date 05/03/2018

Total hours spent learning python: 64

Total days spend learning python: 11

# Update 3.3.1, 06/03/2018
_____________________________________________________________________________
Other Changes:
- Fixed the converter, added parentheses for each conversion pair in order to return an overall True or False answer, instead of a chain of "or"'s which resulted in pairs which shouldn't be matched being input as correct pairs, therefore returning an incorrect answer.

- Fixed some variables being mis-labelled (some were labelled as C instead of B and vice versa)

# Update 3.3, 05/03/2018
_____________________________________________________________________________
Added Commands:
1) +about

Displays information about the bot, including a link to the github repo
_____________________________________________________________________________
Modified Commands:
1) +brand
 
 a) Now the +brand embed output will include brand logo as "thumbnail"

2) +help, +brandhelp 1, +brandhelp 2, +brandhelp 3, +easter eggs

 a) Now when any of the help commands are used, the bot will send the response as a private message to reduce clutter.
_____________________________________________________________________________
Other Changes:
- Added logo's for all companies in the "websites.py" file in order to return their respective logoes when "+brand" command is used

- In "converter.py, fixed the #wh converter (used to return an error)

- Modified the converter to accept "miles", "mile", "kilometers", "kilometres", "kilometer", "kilometre", "centimeters", "centimetre", "centimeter" and "centimetres"
_____________________________________________________________________________
Date 05/03/2018

Total hours spent learning python: 61

Total days spend learning python: 10

# Update 3.2, 05/03/2018
_____________________________________________________________________________
Added Commands:
1) +brand
2) +brandhelp 1
3) +brandhelp 2
4) +brandhelp 3

Returns Brand information formatted via embed, includes "Website", "eMail", "Facebook" and "Reddit"
_____________________________________________________________________________
Modified Commands:
1) +help
 
 a) Added the +brandhelp commands.
_____________________________________________________________________________
Other Changes:
- Created new library called websites, includes information on each brand which has it's own channel on the server.
_____________________________________________________________________________
Date 05/03/2018

Total hours spent learning python: 57

Total days spend learning python: 10

# Update 3.1, 04/03/2018
_____________________________________________________________________________
Added Commands:
1) +server

Returns Server Info
_____________________________________________________________________________
Modified Commands:
1) +convert
 
 a) Modified data entry method, now allows decimals to be enterred.
 
 b) Moved the conversion functions to a seperate file stored in a /lbry/ folder, which is imported into the main bot.py.
_____________________________________________________________________________
Other Changes:
- Main Project moved to new folder, "/execution folder"
- All old project files moved to new folder called "/Old Files"
_____________________________________________________________________________
Date 04/03/2018

Total hours spent learning python: 54

Total days spend learning python: 9

# Update 3, 03/03/2018, Version 2 Released!
Version two released.
_____________________________________________________________________________
Current Commands:
1) +convert
 
Use "+convert #Number#... ..."｜kph <-> mph｜km <-> mi｜cm <-> inch｜km <- Wh -> mi

2) +reddit
 
Get link to the official esk8 Reddit

3) +forum
 
Get link to electric-skateboard.builders

4) +easter eggs

Easter Eggs
_____________________________________________________________________________
Easter Eggs:

1) Moshi Moshi
 
UserName Desu

2) Ben Pls
 
Everyone knows this one

3) Who's your daddy?
 
Want to know who was responsible for the bots birth?
_____________________________________________________________________________
Other changes:
- Added "embed" to main commands for formatting.
- Changed how floats are printed to limit them to 2 decimal places.
- Added logging.
- Prints Bot name and ID to console.
- Added "playing" info with "+help for more info" text.
_____________________________________________________________________________
Date 03/03/2018

Total hours spent learning python: 50

Total days spend learning python: 8

# Update 2, 01/03/2018
First version of the bot uploaded.
_____________________________________________________________________________
Current commands:
1) ++Convert # Converts 2 given values
2) ++Conversion Help # Returns list of commands for "++Convert"
3) Who's your daddy # Returns "Armin Senpai"
4) Ben pls # Returns :benpls: emoji
_____________________________________________________________________________
Date: 01/03/2018

Total hours spent learning python: 38

Total days spent learning python: 6

# Update 1, 01/03/2018
This new version of the converter has been re-written, only retaining around 5 lines of code from the previous version.
_____________________________________________________________________________
*Main file is "Main Converter Version 4"*
_____________________________________________________________________________
#1: Makes better use of Functions, as well as parameters and arguments
#2: Made after 48% completion of CodeCademy Course, total hours spent learning python: 33
_____________________________________________________________________________
Inspired by: Test V2 and Jinra's Version. Both of which will be uploaded for reference.
