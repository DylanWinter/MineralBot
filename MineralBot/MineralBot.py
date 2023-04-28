from selenium import webdriver

# Class containing all methods for MineralBot
class Bot():
    def __init__(self):
        options = webdriver.ChromeOptions() 
        options.add_argument('--disable-blink-features=AutomationControlled')

        self.driver = webdriver.Chrome(executable_path= r"C:\Users\dylan\Desktop\MineralBot\Drivers\chromedriver.exe", chrome_options=options)

    def getSite(self, linkAddress):
        self.driver.get(linkAddress)
        self.driver.implicitly_wait(5)
        
    def findAndClick(self, id, waitTime = 5):
        button = self.driver.find_element("id", id)
        button.click()
        self.driver.implicitly_wait(waitTime)

    def findAndSend(self, id, key, waitTime = 5):
        button = self.driver.find_element("id", id)
        button.send_keys(key)
        self.driver.implicitly_wait(waitTime)