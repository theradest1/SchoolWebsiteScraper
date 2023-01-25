import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=">", intents = intents)

hiddenInfoFile = open("hiddenInfo.txt")
hiddenInfo = content = hiddenInfoFile.readlines()

silencingMartin = False

@bot.event
async def on_ready():
    print('client ready')


@bot.event
async def on_message(message):
    global silencingMartin
    if bot.user.id != message.author.id:
        if message.author.id == 594245967738437639:
            if silencingMartin == True:
                await message.delete()
                return
            elif random.randint(0, 70) == 69:
                await message.delete()
                await message.channel.send("Martin said something but I deleted it lol")
                await message.channel.send("Skill issue :shrug:")
    await bot.process_commands(message)

@bot.command()
async def silenceMartin(ctx):
    global silencingMartin
    if silencingMartin:
    	await ctx.channel.send('The silence has been toggled off')
    else:
        await ctx.channel.send("The silence has been toggled on... thank god")
    silencingMartin = not silencingMartin
async def test(ctx):
    await ctx.channel.send("Skill issue :shrug:")
    
bot.run(hiddenInfo[1])