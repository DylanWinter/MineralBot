import sys
sys.path.append(r"C:\Users\dylan\Desktop\MineralBot")
import MineralBot.MineralBot as bot
import MineralBot.logins as logins

bot = bot.Bot()
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

input()