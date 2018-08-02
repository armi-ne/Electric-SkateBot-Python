import datetime
import math

mutesdic = {}

def checks(codeblock=None):
    if codeblock is None:
        answer = "Missing Time"
    elif codeblock is not None and codeblock.isnumeric():
        answer = "Correct"
    elif codeblock is not None and not codeblock.isnumeric():
        answer = "Time given not number"
    else:
        answer = "Missing Time"
    return answer


def reason(reasonin = None):
    if len(reasonin) > 0:
        sentence = ' '.join(reasonin)
    else:
        sentence = "No reason given."
    return sentence


def seconds_to_time_and_date(time):
    final = []
    print(time)
    if int(time) >= 86401:
        days = math.floor(time/86400)
        remainder = time%86400
        hours = math.floor(remainder/3600)
        remainder2 = remainder%3600
        minutes = math.floor(remainder2/60)
        seconds = remainder2%60
        print(days + hours + minutes + seconds)
        final = [days, hours, minutes, seconds]
    elif int(time) <= 86400 and int(time) >= 3600:
        hours = math.floor(time/3600)
        remainder = time%3600
        minutes = math.floor(remainder/60)
        seconds = remainder%60
        print(hours + minutes + seconds)
        final = [hours, minutes, seconds]
    elif int(time) <=3599 and int(time) >= 60:
        minutes = math.floor(time/60)
        seconds = time%60
        print(minutes + seconds)
        final = [minutes, seconds]
    return final


def time_stripper(muted_Time):
    hour = muted_Time[0]
    minute = muted_Time[1]
    second = muted_Time[2]
    day = muted_Time[3]
    month = muted_Time[4]
    year = muted_Time[5]
    return hour, minute, second, day, month, year


def text_formatter_and_writer(user_ID, banned_on, unbanned_on):
    to_write = (str(user_ID) + "/" + str(banned_on) + "/" + str(unbanned_on))
    print(to_write)
    f=open("muted_users.txt", "a")
    f.write("{0}/ \n".format(to_write))
    f.close()


def mutes_check():
    with open("C:/Users/Administrator/Dropbox/Coding/Coding Projects/Python/Electric-SkateBot/muted_users.txt") as f:
        for line in f:
            (ID, muted_on, unmuted_on, new_line) = line.split("/")
            key = ID
            val = [str(muted_on), str(unmuted_on)]
            mutesdic[key] = val
    print("Mutes Dictionary:")
    print("")
    print(mutesdic)
    print("")


def mute_main_function(muted_ID, muted_Name, muted_By, muted_Duration, muted_Time, muted_Reason):
    key_to_write = str(muted_ID)
    time_answer = seconds_to_time_and_date(muted_Duration)
    ohour, ominute, osecond, oday, omonth, oyear = time_stripper(muted_Time)
    original_datetime = datetime.datetime(int(oyear), int(omonth), int(oday), int(ohour), int(ominute), int(osecond))
    if len(time_answer) == 4:
        days_to_add = time_answer[0]
        hours_to_add = time_answer[1]
        minutes_to_add = time_answer[2]
        seconds_to_add = time_answer[3]
        full_time_of_unban = (original_datetime + datetime.timedelta(days = days_to_add, hours = hours_to_add, minutes = minutes_to_add, seconds = seconds_to_add))
    elif len(time_answer) == 3:
        hours_to_add = time_answer[0]
        minutes_to_add = time_answer[1]
        seconds_to_add = time_answer[2]
        full_time_of_unban = (original_datetime + datetime.timedelta(hours = hours_to_add, minutes = minutes_to_add, seconds = seconds_to_add))
    else:
        minutes_to_add = time_answer[0]
        seconds_to_add = time_answer[1]
        full_time_of_unban = (original_datetime + datetime.timedelta(minutes = minutes_to_add, seconds = seconds_to_add))
    text_formatter_and_writer(muted_ID, original_datetime, full_time_of_unban)
