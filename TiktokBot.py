import discord
import requests

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send(f'Hello {message.author.name}!')

# Replace 'your_discord_token_here' with your actual Discord bot token
client.run('your_discord_token_here')