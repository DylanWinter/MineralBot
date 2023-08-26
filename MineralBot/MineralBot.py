from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import re
from webdriver_manager.chrome import ChromeDriverManager


# Class containing all methods for MineralBot
class Bot():
    def __init__(self):
        options = webdriver.ChromeOptions() 
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.action = ActionChains(self.driver)


    def getSite(self, linkAddress):
        self.driver.get(linkAddress)
        self.driver.implicitly_wait(5)

    def find(self, id, method="id"):
        return self.driver.find_element(method, id)
        
    def findAndClick(self, id, waitTime = 2, method = "id"):
        button = self.driver.find_element(method, id)
        button.click()
        self.driver.implicitly_wait(waitTime)

    def findAndSend(self, id, key, waitTime = 2, method = "id"):
        button = self.driver.find_element(method, id)
        button.send_keys(key)
        self.driver.implicitly_wait(waitTime)

    def readCoords(self, file= r"C:\Users\dylan\Desktop\MineralBot\targets.txt"):
        coordList = open(file)
        targets = []
        for i in coordList:
            if i[0] == "#" or i == "\n":
                pass
            else:
                coords = i.split("|")
                target = []
                for j in coords:
                    newCoord = j.strip()
                    target.append(newCoord)
                targets.append(target)
        coordList.close()
        return targets
                
    def extractCoords(self, coordString):
        nums = re.sub("[^0-9]", " ", coordString)
        nums = nums.strip()
        nums = nums.split()
        return nums
    
    def getTargetsList(self):
        tgts = self.readCoords()
        allTargets = []
        for line in tgts:
            tgt = []
            for val in line:
                coord = self.extractCoords(val)
                tgt.append(coord)
            allTargets.append(tgt)
        return allTargets
    
    def moveTo(self, element):
        self.action.move_to_element(element)
        self.action.perform()

    def moveBy(self, offsetH=0, offsetV=0):
        self.action.move_by_offset(offsetH, offsetV)
        self.action.perform()
    
    def selectArea(self, element, offsetX1, offsetY1, offsetX2, offsetY2):
        self.action.move_to_element(element)
        self.action.move_by_offset(offsetX1, offsetY1)
        self.action.click_and_hold()
        self.action.move_to_element(element)
        self.action.move_by_offset(offsetX2, offsetY2)
        self.action.release()
        self.action.perform()

    def enterIframe(self, frameID):
        self.driver.switch_to.frame(frameID)

    def exitIframe(self):
        self.driver.switch_to.default_content()

    
 
    

## Testing Zone ## 
# bot = Bot()
# tgts = bot.readCoords()
# allTargets = []
# for line in tgts:
#     tgt = []
#     for val in line:
#         coord = bot.extractCoords(val)
#         tgt.append(coord)
#     allTargets.append(tgt)
# print( allTargets)
    
        