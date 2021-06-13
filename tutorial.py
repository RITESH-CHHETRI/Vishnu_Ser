#discord module
import discord
from discord.ext import commands
#modules to access token
import os
from dotenv import load_dotenv

#getting token
load_dotenv('.env')
token=os.getenv('token')

#setting up connection to server
client=commands.Bot(command_prefix="/")

#On ready response
@client.event
async def on_ready():
    print(f"Successfully connected to {client.user.name}")
#list of banned words
bannedWords=["beach","bad"]

#On message responses
@client.event
async def on_message(message):
    if message.author==client.user:
        return
    if message.content.startswith("hello"):
        await message.channel.send("hi")
    #banned word(detect and delete)
    messageContent=message.content.strip().lower()
    for bannedword in bannedWords:
        if bannedword in messageContent:
            await message.channel.send("This is a banned word!")
            await message.delete()

    await client.process_commands(message)
client.run(token)