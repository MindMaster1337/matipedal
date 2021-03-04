import discord
import os
import random

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$essa'):
        x=random.randint(0, 100)
        await message.channel.send("Twoja essa to: "+str(x))

    if message.content.startswith('$rigcz'):
        x=random.randint(0, 100)
        await message.channel.send("Twój rigcz to: "+str(x)+" opie")

    if message.content.startswith('$bajer'):
        x=random.randint(0, 100)
        await message.channel.send("Detektor bajeru wykazał, że masz: "+str(x)+" współczynniku bajery")

    if message.content.startswith('$rzydy'):
        x=random.randint(0, 100)
        await message.channel.send(":fire:")

    if message.content.startswith('$mati'):
        x=random.randint(0, 100)
        await message.channel.send("Mati pedał psa jebał")

client.run(os.getenv('TOKEN'))