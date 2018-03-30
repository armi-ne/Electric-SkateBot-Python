import datetime
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ["https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("C:/Users/Administrator/Dropbox/Coding/Coding Projects/Python/Electric-SkateBot_Server_Test/client_secret.json", scope)
client = gspread.authorize(credentials)

def upload_to_drive_new(context, messages):
    time = datetime.datetime.now()  # Gets the time
    import_time = time.strftime("%D, %H:%M:%S")  # Formats the time
    sheet = client.open("ESK8 Server").sheet1
    deleted_on = ["Deleted on", import_time, "by", context.message.author.name]
    sheet.insert_row(deleted_on, 1)
    new_empty_row = ["  ", "  ", "  ", "  "]
    sheet.insert_row(new_empty_row, 1)
    timestamps = ""
    authors = ""
    contents = ""
    channels = ""
    for stuff in messages:
        timestamps = timestamps + "\n" + str(stuff.timestamp)
        authors = authors + "\n" + str(stuff.author)
        contents = contents + "\n" + str(stuff.content)
        channels = channels + "\n" + str(stuff.channel)        
    values_to_ins = [str(timestamps), str(authors), str(contents), str(channels)]
    sheet.insert_row(values_to_ins, 1)
    timestamps = ""
    authors = ""
    contents = ""
    channels = ""


def upload_to_drive(context, messages):
    time = datetime.datetime.now()  # Gets the time
    import_time = time.strftime("%D, %H:%M:%S")  # Formats the time
    sheet = client.open("ESK8 Server").sheet1
    delete_order = 0
    deleted_on = ["Deleted on", import_time, "by", context.message.author.name]
    sheet.insert_row(deleted_on, 1)
    new_empty_row = ["  ", "  ", "  ", "  "]
    sheet.insert_row(new_empty_row, 1)
    for inside in messages:
        delete_order += 1
        value_to_ins = [str(inside.timestamp), str(inside.author), str(inside.content), str(inside.channel)]
        sheet.insert_row(value_to_ins, 1)
    sheet.insert_row(new_empty_row, 1)

