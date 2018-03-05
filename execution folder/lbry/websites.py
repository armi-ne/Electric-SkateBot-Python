# Function for differentiating websites of eboard companies
from PIL import Image


def sitefinder(a):
    # Acton
    if a.upper() == "ACTON":
        website = "https://www.actonglobal.com/"
        contact_email = "info@actonglobal.com"
        facebook = "https://www.facebook.com/ACTONglobal/"
        reddit = "https://www.reddit.com/r/actonglobal/"
        logo = "https://i.imgur.com/7VZapFJ.png"
    # Arc
    elif a.upper() == "ARC":  # or a.upper() == "ARC BOARD":
        website = "https://www.arcboardsev.com/"
        contact_email = "hello@arcboardsev.com"
        facebook = "https://www.facebook.com/ArcBoardsEV"
        reddit = "https://www.reddit.com/user/ArcBoardsEV"
        logo = "https://i.imgur.com/bOuWa2L.jpg"
    # Backfire
    elif a.upper() == "BACKFIRE":
        website = "http://www.backfireboards.com/"
        contact_email = "Sales@helloskate.com"
        facebook = "https://www.facebook.com/backfireskateboards/"
        reddit = "Unavailable"
        logo = "https://i.imgur.com/CAaiqik.jpg"
    # Boosted
    elif a.upper() == "BOOSTED":  # or a.upper() == "BOOSTED BOARD" or a.upper() == "BOOSTED BOARDS":
        website = "https://boostedboards.com/"
        contact_email = "community@boostedboards.com"
        facebook = "https://www.facebook.com/BoostedBoards/"
        reddit = "https://www.reddit.com/r/boostedboards/"
        logo = "https://i.imgur.com/4H51uMi.jpg"
    # Carvon
    elif a.upper() == "CARVON":
        website = "https://www.carvonskates.com/"
        contact_email = "info@carvonskates.com"
        facebook = "https://www.facebook.com/Carvonskates/"
        reddit = "https://www.reddit.com/user/carvonskates/"
        logo = "https://i.imgur.com/QUdZMiU.jpg"
    # DiyEboard
    elif a.upper() == "DIYEBOARD":  # or a.upper() == "DIY EBOARD" or a.upper() == "DIY-EBOARD":
        website = "http://www.diyeboard.com/"
        contact_email = "Unavailable"
        facebook = "Unavailable"
        reddit = "Unavailable"
        logo = "https://i.imgur.com/xPw8WSv.jpg"
    # Enertion
    elif a.upper() == "ENERTION":
        website = "http://www.enertionboards.com/"
        contact_email = "support@enertionboards.com"
        facebook = "https://www.facebook.com/enertion.boards"
        reddit = "https://www.reddit.com/user/onloop/"
        logo = "https://i.imgur.com/fwgSDmW.png"
    # Evolve
    elif a.upper() == "EVOLVE":
        website = "https://www.evolveskateboards.com/"
        contact_email = "ask@evolveskateboards.com.au"
        facebook = "https://www.facebook.com/EvolveSkateboards/"
        reddit = "https://www.reddit.com/r/evolveskateboards/"
        logo = "https://i.imgur.com/XwDJ7vR.jpg"
    # Jed Board
    elif a.upper() == "JED":  # or a.upper() == "JED BOARD" or a.upper() == "JEDBOARD":
        website = "https://jedboards.com/"
        contact_email = "yo@jedboards.com"
        facebook = "https://www.facebook.com/jedboards/"
        reddit = "https://www.reddit.com/user/jedboards"
        logo = "https://i.imgur.com/YWdzKvv.png"
    # Max
    elif a.upper() == "MAX":
        website = "https://www.maxskate.com/"
        contact_email = "support@maxskate.com"
        facebook = "https://www.facebook.com/FPVskate"
        reddit = "Unavailable"
        logo = "https://i.imgur.com/Ci2cJAA.jpg"
    # Meepo
    elif a.upper() == "MEEPO":
        website = "https://meepoboard.com/"
        contact_email = "kieran@meepoboard.com"
        facebook = "https://www.facebook.com/MeepoBoard"
        reddit = "https://www.reddit.com/user/kieraneboard"
        logo = "https://i.imgur.com/prpdMO4.jpg"
    # Metroboard
    elif a.upper() == "METROBOARD":  # or a.upper() == "METRO BOARD":
        website = "https://metro-board.com/"
        contact_email = "info@metro-board.com"
        facebook = "https://www.facebook.com/Metroboard.Electric.Skateboard"
        reddit = "Unavailable"
        logo = "https://i.imgur.com/r00kfMe.jpg"
    # Onewheel
    elif a.upper() == "ONEWHEEL":  # or a.upper() == "ONE WHEEL":
        website = "https://onewheel.com/"
        contact_email = "support@onewheel.com"
        facebook = "https://www.facebook.com/OnewheelOfficial/"
        reddit = "https://www.reddit.com/r/onewheel/"
        logo = "https://i.imgur.com/hdKin4R.png"
    # Predator Board
    elif a.upper() == "PREDATOR":  # or a.upper() == "PREDATOR BOARD":
        website = "https://ridepredator.com/"
        contact_email = "contactpredatorelectric@gmail.com"
        facebook = "https://www.facebook.com/TheFreakingQ/"
        reddit = "https://www.reddit.com/user/PredatorBoards"
        logo = "https://i.imgur.com/BvgFwKe.jpg"
    # Pulseboards
    elif a.upper() == "PULSEBOARD":  # or a.upper() == "PULSE BOARD" or a.upper() == "PULSE BOARDS" or a.upper() == "PULSEBOARDS":
        website = "https://www.pulseboards.com/"
        contact_email = "Unavailable"
        facebook = "https://www.facebook.com/pulseboard"
        reddit = "https://www.reddit.com/user/pulseboards"
        logo = "https://i.imgur.com/Ww8cayr.png"
    # Riptide
    elif a.upper() == "RIPTIDE":
        website = "https://rideriptide.com/"
        contact_email = "info@rideriptide.com"
        facebook = "https://www.facebook.com/RideRiptide/"
        reddit = "https://www.reddit.com/user/RideRiptide"
        logo = "https://i.imgur.com/u0sO9BV.png"
    # Trampa
    elif a.upper() == "TRAMPA":
        website = "http://www.trampaboards.com/"
        contact_email = "info@trampaboards.com"
        facebook = "https://www.facebook.com/trampaboards"
        reddit = "Unavailable"
        logo = "https://i.imgur.com/amdrGsd.jpg"
    # Wowgo
    elif a.upper() == "WOWGO":
        website = "https://wowgoboard.com/"
        contact_email = "wowgoeboard@gmail.com"
        facebook = "https://www.facebook.com/WOWGOBOARD/?ref=br_rs"
        reddit = "Unavailable"
        logo = "https://i.imgur.com/qBpsiMX.jpg"
    return website, contact_email, facebook, reddit, logo
