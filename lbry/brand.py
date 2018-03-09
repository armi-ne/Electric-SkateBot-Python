acton = [
    "https://www.actonglobal.com/",
    "info@actonglobal.com",
    "https://www.facebook.com/ACTONglobal/",
    "https://www.reddit.com/r/actonglobal/",
    "https://i.imgur.com/7VZapFJ.png"
]

arc = [
    "https://www.arcboardsev.com/",
    "hello@arcboardsev.com",
    "https://www.facebook.com/ArcBoardsEV",
    "https://www.reddit.com/user/ArcBoardsEV",
    "https://i.imgur.com/bOuWa2L.jpg",
]

backfire = [
    "http://www.backfireboards.com/",
    "Sales@helloskate.com",
    "https://www.facebook.com/backfireskateboards/",
    "Unavailable",
    "https://i.imgur.com/CAaiqik.jpg"
]

boosted = [
    "https://boostedboards.com/",
    "community@boostedboards.com",
    "https://www.facebook.com/BoostedBoards/",
    "https://www.reddit.com/r/boostedboards/",
    "https://i.imgur.com/4H51uMi.jpg"
]

carvon = [
    "https://www.carvonskates.com/",
    "info@carvonskates.com",
    "https://www.facebook.com/Carvonskates/",
    "https://www.reddit.com/user/carvonskates/",
    "https://i.imgur.com/QUdZMiU.jpg"
]

diyeboard = [
    "http://www.diyeboard.com/",
    "Unavailable",
    "Unavailable",
    "Unavailable",
    "https://i.imgur.com/xPw8WSv.jpg"
]

enertion = [
    "http://www.enertionboards.com/",
    "support@enertionboards.com",
    "https://www.facebook.com/enertion.boards",
    "https://www.reddit.com/user/onloop/",
    "https://i.imgur.com/fwgSDmW.png"
]

evolve = [
    "https://www.evolveskateboards.com/",
    "ask@evolveskateboards.com.au",
    "https://www.facebook.com/EvolveSkateboards/",
    "https://www.reddit.com/r/evolveskateboards/",
    "https://i.imgur.com/XwDJ7vR.jpg"
]

jed = [
    "https://jedboards.com/",
    "yo@jedboards.com",
    "https://www.facebook.com/jedboards/",
    "https://www.reddit.com/user/jedboards",
    "https://i.imgur.com/YWdzKvv.png"
]

max = [
    "https://www.maxskate.com/",
    "support@maxskate.com",
    "https://www.facebook.com/FPVskate",
    "Unavailable",
    "https://i.imgur.com/Ci2cJAA.jpg"
]

meepo = [
    "https://meepoboard.com/",
    "kieran@meepoboard.com",
    "https://www.facebook.com/MeepoBoard",
    "https://www.reddit.com/user/kieraneboard",
    "https://i.imgur.com/prpdMO4.jpg"
]

metro = [
    "https://metro-board.com/",
    "info@metro-board.com",
    "https://www.facebook.com/Metroboard.Electric.Skateboard",
    "Unavailable",
    "https://i.imgur.com/r00kfMe.jpg"
]

onewheel = [
    "https://onewheel.com/",
    "support@onewheel.com",
    "https://www.facebook.com/OnewheelOfficial/",
    "https://www.reddit.com/r/onewheel/",
    "https://i.imgur.com/hdKin4R.png"
]

predator = [
    "https://ridepredator.com/",
    "contactpredatorelectric@gmail.com",
    "https://www.facebook.com/TheFreakingQ/",
    "https://www.reddit.com/user/PredatorBoards",
    "https://i.imgur.com/BvgFwKe.jpg"
]

pulse = [
    "https://www.pulseboards.com/",
    "Unavailable",
    "https://www.facebook.com/pulseboard",
    "https://www.reddit.com/user/pulseboards",
    "https://i.imgur.com/Ww8cayr.png"
]

riptide = [
    "https://rideriptide.com/",
    "info@rideriptide.com",
    "https://www.facebook.com/RideRiptide/",
    "https://www.reddit.com/user/RideRiptide",
    "https://i.imgur.com/u0sO9BV.png"
]

trampa = [
    "http://www.trampaboards.com/",
    "info@trampaboards.com",
    "https://www.facebook.com/trampaboards",
    "Unavailable",
    "https://i.imgur.com/amdrGsd.jpg"
]

wowgo = [
    "https://wowgoboard.com/",
    "wowgoeboard@gmail.com",
    "https://www.facebook.com/WOWGOBOARD/?ref=br_rs",
    "Unavailable",
    "https://i.imgur.com/qBpsiMX.jpg"
]

maindict = {
    "ACTON": acton, "ARC": arc, "BACKFIRE": backfire, "BOOSTED": boosted,
    "CARVON": carvon, "DIYEBOARD": diyeboard, "ENERTION": enertion, "EVOLVE": evolve,
    "JED": jed, "MAX": max, "MEEPO": meepo, "METRO": metro, "ONEWHEEL": onewheel, "PREDATOR": predator,
    "PULSE": pulse, "RIPTIDE": riptide, "TRAMPA": trampa, "WOWGO": wowgo
}


def brandfinder(a):
    website = maindict[a()][0]
    email = maindict[a()][1]
    facebook = maindict[a()][2]
    reddit = maindict[a()][3]
    thumbnail = maindict[a()][4]
    return website, email, facebook, reddit, thumbnail

# Testing to ensure it works for now below

userinput = input("Please input the brand's information that you'd like ").upper

reqWeb, reqEm, reqFb, reqRed, reqThu = brandfinder(userinput)

print(reqWeb)
print(reqEm)
print(reqFb)
print(reqRed)
print(reqThu)
