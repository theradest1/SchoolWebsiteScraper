import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=">", intents = intents)

hiddenInfoFile = open("hiddenInfo.txt")
hiddenInfo = content = hiddenInfoFile.readlines()

rileyID = 718795668801585203
channelID = 1097510587208048793
person = "Riley"

#rileyID = 571446451771801600
#channelID = 970098568197201932
#person = "Landon"

@bot.event
async def on_ready():
    print('client ready')


@bot.event
async def on_message_delete(message):
    if bot.user.id != message.author.id:
        if message.author.id == rileyID:
            await bot.get_channel(channelID).send(person + " deleted the message: \"" + message.content + "\"")


@bot.event
async def on_message_edit(before, after):
    if bot.user.id != before.author.id:
        if before.author.id == rileyID:
            await bot.get_channel(channelID).send(person + " edited the message: \"" + before.content + "\"")


bot.run(hiddenInfo[1])