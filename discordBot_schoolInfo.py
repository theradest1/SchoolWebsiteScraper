import discord
from discord.ext import commands
from discord.ext import tasks
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.by import By
import time
import asyncio

#discord bot init
#intents = discord.Intents.default()
#intents.message_content = True
#bot = commands.Bot(command_prefix="@", intents = intents)
    
def getCurrentDate():
    return datetime.today().strftime('%Y-%m-%d').replace("-", "")

def getEvents():
    textList = []
    elements, browser = scrape(schoolWebsite, "wcm-calendar-event-title")
    for element in elements:
        textList.append(element.text)
    browser.close()
    return textList

async def sendEventsToChannel(channelID, events):
    await client.get_channel(channelID).send("Today's events:")
    for event in events:
        await client.get_channel(channelID).send(event)

def scrape(websiteURL, className):
    browser = webdriver.Firefox()
    browser.get(websiteURL)
    time.sleep(timeToLoad)
    try:
        elements = browser.find_elements(By.CLASS_NAME, className)
    except:
        print("browser failed to get any events from webpage")
        elements = []
    return elements, browser

#accessing hidden info that I don't want online
hiddenInfoFile = open("hiddenInfo.txt")
hiddenInfo = content = hiddenInfoFile.readlines()

#settings
schoolWebsite = hiddenInfo[3] + getCurrentDate() + "/day"
print(schoolWebsite)
timeBetweenChecks = 600
timeToLoad = 5 #in seconds (higher is better but takes more time for testing)
date = ""

class MyClient(discord.Client):
    async def setup_hook(self) -> None:
        # start the task to run in the background
        self.my_background_task.start()

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    @tasks.loop(seconds=timeBetweenChecks)  # task runs every 60 seconds
    async def my_background_task(self):
        global date
        if(date != getCurrentDate()):
            print("Next day")
            await sendEventsToChannel(1065857282040152114, getEvents())
            date = getCurrentDate()
        else:
            print("Same day")
            
    @my_background_task.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()  # wait until the bot logs in
    

client = MyClient(intents=discord.Intents.default())
client.run(hiddenInfo[1])