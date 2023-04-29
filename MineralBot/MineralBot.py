from selenium import webdriver
import re

# Class containing all methods for MineralBot
class Bot():
    def __init__(self):
        options = webdriver.ChromeOptions() 
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(executable_path= r"C:\Users\dylan\Desktop\MineralBot\Drivers\chromedriver.exe", chrome_options=options)

    def getSite(self, linkAddress):
        self.driver.get(linkAddress)
        self.driver.implicitly_wait(5)
        
    def findAndClick(self, id, waitTime = 5, method = "id"):
        button = self.driver.find_element(method, id)
        button.click()
        self.driver.implicitly_wait(waitTime)

    def findAndSend(self, id, key, waitTime = 5):
        button = self.driver.find_element("id", id)
        button.send_keys(key)
        self.driver.implicitly_wait(waitTime)

    def readCoords(self, file= r"C:\Users\dylan\Desktop\MineralBot\targets.txt"):
        coordList = open(file)
        targets = []
        for i in coordList:
            if i[0] == "#" or i == "\n":
                pass
            else:
                newCoord = i.strip()
                targets.append(newCoord)
        coordList.close()
        return targets
                
    def extractCoords(self, coordString):
        nums = re.sub("[^0-9]", " ", coordString)
        nums = nums.strip()
        nums = nums.split()
        return nums
    

## Testing Zone ## 