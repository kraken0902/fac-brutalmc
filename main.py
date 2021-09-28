import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

PREFIX = ("$")
bot = commands.Bot(command_prefix=PREFIX, description='Hi')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="le faction"))
    print("Pret !")

bot.run('ODkyNDkyNTk2NzgwMzQ3NDIy.YVNsgA.nFdodGGyL8vEGyYFL3KMVqX04Yw')