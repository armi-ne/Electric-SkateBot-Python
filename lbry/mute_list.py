import time
starttime = time.time()

muted_users = {

}


def write_to_file():
    file_ = open("/home/armi-ne/Desktop/Coding/Coding Projects/Python/esk8 bot/Bot Spring Cleaning/Spring Cleaning Bot Folder/muted_users.txt", "w")
    file_.write(str(muted_users))
    file_.close()
