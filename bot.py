import discord
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

TOKEN = os.environ.get("DISCORD_TOKEN")

client = discord.Client()

#BOTが起動したとき
@client.event
async def on_ready():
    print('起動しました！(\'◇\')ゞ')

@client.event
async def on_message(message):
    # Botだったらは無視
    if message.author.bot:
        return
    if message.content == '/hello':
        await message.channel.send('hello')

client.run(TOKEN)
