#discord module
import discord
from discord.ext import commands
#module to access token
import os

#getting token
token=os.getenv('TOKEN')

#setting up connection/instance to server
bot=commands.Bot(command_prefix="/")

#On ready response/func
@bot.event
async def on_ready():
    print(f"Successfully connected to {bot.user.name}")
#list of banned words
bannedWords=["beach","bad"]

#On message responses/func
@bot.event
async def on_message(message):
    if message.author==bot.user:
        return
    if message.content.startswith("hello"):
        await message.channel.send("hi")
    #banned word(detect and delete)
    messageContent=message.content.strip().lower()
    for bannedword in bannedWords:
        if bannedword in messageContent:
            await message.channel.send("This is a banned word!")
            await message.delete()

    await bot.process_commands(message)
bot.run(token)
