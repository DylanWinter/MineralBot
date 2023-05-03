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
    bot.findAndClick("d_s1553779887997[2]")
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
print("Checking every 30 seconds...")
while True:
    clock_val = clock.get_attribute("value")
    if "8:33" in clock_val and "PM" in clock_val:
        break
    else:
        time.sleep(30)
print("Checking every 5 seconds...")
while True:
    clock_val = clock.get_attribute("value")
    if "8:33:5" in clock_val:
        break
    else:
        time.sleep(5)
print("Checking every second...")
while True:
    clock_val = clock.get_attribute("value")
    if "8:33:58" in clock_val or "8:33:59" in clock_val:
        break
    else:
        time.sleep(1)
print("Checking as fast as possible...")
while True:
    clock_val = clock.get_attribute("value")
    if "8:34:00" in clock_val:
        break

start = time.time()

bot.findAndClick("/html/body/div[2]/div/form/div[3]/div[5]/div/div/div/a", method="xpath")
bot.selectArea(canvas, offset1[0], offset1[1], offset2[0], offset2[1])
while True:
    if bot.find("d_1531394652148").get_attribute("value") != "":
        bot.findAndClick("d_1558981073511", method="name")
        break
bot.findAndClick("d_1558981073515", method="name")

end = time.time()
print("Time elapsed:", str(end - start) + "s")







input()