import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print ("Bot is ready!")
    print ("I am running on: " + client.user.name)
    print ("With the ID: " + client.user.id)

#General Response Commands
@client.event
async def on_message(message):
    if message.content.upper().startswith('!PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))
    if message.content.upper().startswith('!SAY'):
        args = message.content.split(" ")
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))


client.run("NDM3MzQ2Nzk0MTkyNzY0OTM4.Db0ueA.LFVZ06WzphUsYrhZkS4R_e92DMI")
