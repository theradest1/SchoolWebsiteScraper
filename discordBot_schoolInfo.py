##!/usr/bin/python3

import discord
from discord.ext import commands
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.by import By
import time

#accessing hidden info that I don't want online
hiddenInfoFile = open("hiddenInfo.txt")
hiddenInfo = content = hiddenInfoFile.readlines()

#discord bot init
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="@", intents = intents)

#settings
timeToLoad = 120 #in seconds (higher is better but takes more time for testing)

schoolWebsite = hiddenInfo[3] + getCurrentDate() + "/day"

#print("Date: " + getCurrentDate())
#print("URL used: " + schoolWebsite)

elements = scrape(schoolWebsite, "wcm-calendar-event-title")

print("Today's info: ")
for element in elements:
    print(element.text)

@bot.command()
async def die(ctx):
	await ctx.send("Bye (:")
	exit()

def getCurrentDate():
    return datetime.today().strftime('%Y-%m-%d').replace("-", "")

def scrape(websiteURL, className):
    browser = webdriver.Firefox()
    browser.get(vahsURL)
    time.sleep(timeToLoad)
    try:
        return browser.find_elements(By.CLASS_NAME, classToFind)
    except:
        return []

bot.run(hiddenInfo[1])