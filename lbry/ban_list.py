banned_users = {
}


def mute_data_formatter(banned_Name, banned_By, banned_Time, banned_Reason):
    name = str(banned_Name)
    by = str(banned_By)
    time = "Time: " + banned_Time
    reason = banned_Reason = "Reason: " + banned_Reason
    return name, by, time, reason
