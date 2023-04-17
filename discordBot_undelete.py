import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=">", intents = intents)

hiddenInfoFile = open("hiddenInfo.txt")
hiddenInfo = content = hiddenInfoFile.readlines()

@bot.event
async def on_ready():
    print('client ready')

@bot.event
async def on_message_delete(message):
    if bot.user.id != message.author.id:
        if message.author.id == 718795668801585203:
            await message.channel.send("Riley deleted this message: \"" + message.content + "\"")

print(hiddenInfo[1])
bot.run(hiddenInfo[1])