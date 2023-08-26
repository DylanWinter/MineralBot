import sys
sys.path.append(r"C:\Users\dylan\Desktop\MineralBot")
import MineralBot.MineralBot as mBot
import MineralBot.logins as logins
import time

# opens the staking portal
def openSite():
    bot.getSite("https://licensing.gov.nl.ca/miriad/sfjsp?interviewID=MRlogin&lang=en")

    # login page
    bot.findAndSend("d_1553779889165", logins.userName)
    bot.findAndSend("d_1553779889166", logins.password)
    bot.findAndClick("h_1618409713756o1")
    bot.findAndClick("div_d_1642075435596")
    # reaching staking map
    bot.findAndClick("d_s1553779887997[1]")
    bot.findAndClick("d_1553779888004", method="name")
    bot.findAndClick("div_d_1550142656331")
    bot.findAndClick("d_1558981073505", method="name")
    bot.findAndClick("h_1531394652133o6")

def findPointCoords(target):
    bot.moveTo(canvas)
    currCoords = bot.extractCoords(coordDisplay.text)
    listToInt(currCoords)

    eastCoord = target[0]
    northCoord = target[1]
    offsetX = 0
    offsetY = 0
    moveX = 0
    moveY = 0
    while not (((eastCoord - 250) <= currCoords[0] <= (eastCoord + 250)) and ((northCoord) <= currCoords[1] <= (northCoord - 500))):

        if currCoords[0] < (eastCoord - 250):
            moveX = 2
        elif currCoords[0] > (eastCoord + 250):
            moveX = -2
        else:
            moveX = 0

        if currCoords[1] < (northCoord - 500):
            moveY = -2
        elif currCoords[1] > (northCoord):
            moveY = 2
        else:
            moveY = 0
        
        bot.moveBy(moveX, moveY)
        offsetX += moveX
        offsetY += moveY

        print(coordDisplay.text)
        currCoords = bot.extractCoords(coordDisplay.text)
        listToInt(currCoords)

        if ((eastCoord - 250) <= currCoords[0] <= (eastCoord + 250)) and ((northCoord - 500) <= currCoords[1] <= (northCoord)):
            break

    print("Offsets found:", offsetX, offsetY)
    return (offsetX, offsetY)

def listToInt(l):
    for i in range(len(l) - 1):
        l[i] = int(l[i])


## Startup ##
authorized = False
time_wait = True
print("MineralBot V1.1")
while True:
    resp = input("Type 'start' to start bot, 'test' to start in test mode:\n")
    if resp.lower() == "start":
        print("WARNING: THIS ALLOWS THE BOT TO MAKE PAYMENT")
        resp2 = input("Enter 'authorized' to begin: ")
        if resp2.lower() == "authorized":
            authorized = True
            print("Bot started, payment is authorized.")
            break
        else:
            print("Cancelled.")
            continue
    elif resp.lower() == "test":
        time_wait = False
        print("Running in test mode, the bot will not wait until 9:00 AM to run.")
        break
    else:
        continue
    

bot = mBot.Bot()
openSite()
# find the coords to start
targetList = bot.getTargetsList()
first = targetList[0]
avgEast = (int(first[0][0]) + int(first[1][0]))//2
avgNorth = (int(first[0][1]) + int(first[1][1]))//2
zone = first[0][2]
# opens the map at the starting coords
bot.findAndSend("d_1568912130644", avgEast)
bot.findAndSend("d_1568912130645", avgNorth)
bot.findAndSend("d_1568912130646", zone)
bot.findAndClick("d_1558981073510", method="name")
canvas = bot.find("/html/body/div[2]/div/form/div[3]/div[8]/div/div/div[1]/div[1]/canvas", method="xpath")
# grabs references to relevant elements 
clock = bot.find("d_1568912131385")
coordDisplay = bot.find("MouseCoords")
# finds the coords of the target claim
bot.moveTo(canvas)
coord1 = first[0]
coord2 = first[1]
listToInt(coord1)
listToInt(coord2)
offset1 = findPointCoords(coord1)
offset2 = findPointCoords(coord2)

bot.findAndClick("select-by-polygon")
# waits until the clock hits 9:00 am
if time_wait:
    print("Refreshing every 30 seconds...")
    while True:
        clock_val = clock.get_attribute("value")
        if "8:59" in clock_val and "AM" in clock_val:
            break
        else:
            time.sleep(30)
    print("Refreshing every 5 seconds...")
    while True:
        clock_val = clock.get_attribute("value")
        if "8:59:5" in clock_val:
            break
        else:
            time.sleep(5)
    print("Refreshing every second...")
    while True:
        clock_val = clock.get_attribute("value")
        if "8:59:58" in clock_val or "8:59:59" in clock_val:
            break
        else:
            time.sleep(1)
    print("Refreshing as fast as possible...")
    while True:
        clock_val = clock.get_attribute("value")
        if "9:00:00" in clock_val:
            break

start = time.time()

bot.findAndClick("/html/body/div[2]/div/form/div[3]/div[5]/div/div/div/a", method="xpath")
bot.selectArea(canvas, offset1[0], offset1[1], offset2[0], offset2[1])
while True:
    if bot.find("d_1531394652148").get_attribute("value") != "":
        bot.findAndClick("d_1558981073511", method="name")
        break

bot.findAndClick("d_1558981073515", method="name")
bot.findAndClick("h_1568912130520o1", method="id")
bot.findAndClick("d_1558981073517", method="name")
bot.enterIframe("monerisFrame")
bot.findAndSend("cardnumber", logins.card_number, method="name")
bot.findAndSend("exp-date", logins.expiry_date, method="name")
bot.findAndSend("cvc", logins.cvd, method="name")
bot.exitIframe()
bot.findAndClick("d_1565877925015", method="name")
bot.findAndClick("h_1559640796736o1")
if authorized:
    bot.findAndClick("d_1531394653880", method="name")


end = time.time()
print("Time elapsed:", str(end - start) + "s")

input()