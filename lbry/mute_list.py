import time
starttime = time.time()

muted_users = {
}


def write_to_file():
    file_ = open("C:/Users/Armi-ne/Desktop/Electric-SkateBot-Python-Master (1)/Electric-SkateBot-Python-Master/lbry/muted_users.txt", "w")
    file_.write(str(muted_users))
    file_.close()


def muted_list():
    raw_list = muted_users.keys()
    joined = ", ".join(raw_list)
    if len(raw_list) is 0:
        answer = "No Muted Users"
        return answer
    else:
        answer = joined
        return answer


def mute_data_formatter(muted_Name, muted_By, muted_Duration, muted_Time, muted_Reason):
    name = str(muted_Name)
    by = str(muted_By)
    duration = "Duration: " + muted_Duration + " minute(s)"
    time = "Time: " + muted_Time
    reason = muted_Reason = "Reason: " + muted_Reason
    return name, by, duration, time, reason

def list_add(member_ID, muted_Name, muted_By, muted_Duration, muted_Time, muted_Reason):
    muted_users[member_ID] = [muted_Name, muted_By, muted_Duration, muted_Time, muted_Reason]
