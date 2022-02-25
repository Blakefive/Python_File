import discord
import asyncio
import re

client = discord.Client()
token = "NzE2NjI2NDUxMTc2MDk1ODQz.XwwYUw.RN6jKWFJCAN6LApgIzGd6ie7l40"
check = 0

def main():
    print("귀찮아")
@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("Hello World")
    await client.change_presence(status=discord.Status.online, activity=game)
a = 0
@client.event
async def on_message(message):
    if message.channel.send("귀찮아"):
        await message.channel.send("```diff\n-ㅗ\n```")
    elif message.channel.send("일해"):
        await message.channel.send("```diff\n-귀찮아\n```")
    
    main()
client.run(token)
