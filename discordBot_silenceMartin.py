import discord
from discord.ext import commands

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
        if message.author.id == 594245967738437639 and silencingMartin == True:
            await message.delete()
            return
        if message.content == "brug":
            await message.channel.send("in a rug")
            

    await bot.process_commands(message)

@bot.command()
async def silenceMartin(ctx):
    global silencingMartin
    if silencingMartin:
    	await ctx.channel.send('The silence has been toggled off')
    else:
        await ctx.channel.send("The silence has been toggled on... thank god")
    silencingMartin = not silencingMartin
    
bot.run(hiddenInfo[1])