import discord
from discord.ext import commands
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.by import By
import time
import asyncio

#discord bot init
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="@", intents = intents)
        
async def nextDay():
    print("hola")
    elements, browser = scrape(schoolWebsite, "wcm-calendar-event-title")
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

#accessing hidden info that I don't want online
hiddenInfoFile = open("hiddenInfo.txt")
hiddenInfo = content = hiddenInfoFile.readlines()

#settings
schoolWebsite = hiddenInfo[3] + getCurrentDate() + "/day"
print(schoolWebsite)
timeBetweenChecks = 1000
timeToLoad = 10 #in seconds (higher is better but takes more time for testing)

@bot.event
async def on_message(message):
    global schoolWebsite
    if message.content == "events":
        elements, browser = scrape(schoolWebsite, "wcm-calendar-event-title")
        await message.channel.send("Events for today:")
        for element in elements:
            await message.channel.send(element.text)
        browser.close()
    if message.content == "startEvents":
        await message.channel.send("aight")
        date = ""   
        while True:
            print("testing day")
            if date != getCurrentDate():
                await nextDay()
            else:
                date = getCurrentDate()
            time.sleep(timeBetweenChecks)
        
@bot.command()
async def die(ctx):
	await ctx.send("Bye (:")
	exit()

bot.run(hiddenInfo[1])