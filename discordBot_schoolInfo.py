import discord
from discord.ext import commands
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.by import By
import time
import threading
import asyncio

#discord bot init
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="@", intents = intents)

async def dayChecker():
    
    print("hola")
    elements, browser = scrape(schoolWebsite, "wcm-calendar-event-title")
    print(schoolWebsite)
    await bot.get_channel(1065857282040152114).send("Events for today:")
    for element in elements:
        await bot.get_channel(1065857282040152114).send(element.text)
    browser.close()

def getCurrentDate():
    return datetime.today().strftime('%Y-%m-%d').replace("-", "")

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

#@bot.event
#async def on_message(message):
#    global schoolWebsite
#    if message.content == "events":
#        elements, browser = await scrape(schoolWebsite, "wcm-calendar-event-title")
#        #await message.channel.send("Events for today:")
#        print("send: Events for today:")
#        for element in elements:
#            #await message.channel.send(element.text)
#            print("send: " + element.text)
#        browser.close()
        
@bot.command()
async def die(ctx):
    await ctx.send("Bye (:")
    botThread._stop()
    exit()

#accessing hidden info that I don't want online
hiddenInfoFile = open("hiddenInfo.txt")
hiddenInfo = content = hiddenInfoFile.readlines()

#settings
schoolWebsite = hiddenInfo[3] + getCurrentDate() + "/day"
print(schoolWebsite)
timeBetweenChecks = 1000
timeToLoad = 5 #in seconds (higher is better but takes more time for testing)

print("starting discord bot")
botThread = threading.Thread(target=bot.run, args=(hiddenInfo[1],))
botThread.start()

print("starting main loop")
date = ""   
while True:
    print("testing day")
    if date != getCurrentDate():
        asyncio.run(nextDay())
        date = getCurrentDate()
    else:
        date = getCurrentDate()
