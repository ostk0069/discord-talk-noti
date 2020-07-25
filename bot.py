import discord
from datetime import datetime, timedelta
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

TOKEN = os.environ.get("DISCORD_TOKEN")
SERVER_ID = os.environ.get("SERVER_ID")
CHANNEL_ID = os.environ.get("CHANNEL_ID")

client = discord.Client()

#BOTが起動したとき
@client.event
async def on_ready():
    print('ログインしました')
    print(client.user.name)  # ボットの名前
    print(client.user.id)  # ボットのID
    print(discord.__version__)  # discord.pyのバージョン
    print('------')

@client.event
async def on_message(message):
    # Botだったらは無視
    if message.author.bot:
        return
    if message.content == "/version":
        await message.channel.send('1.0.1')
    if message.content == '/hello':
        await message.channel.send('hello')
    if message.content == '/server':
        await message.channel.send(f'{SERVER_ID} is your server id')
    if message.content == '/notification_channel':
        await message.channel.send(f'{CHANNEL_ID} is your notification channel id')

@client.event
async def on_voice_state_update(member, before, after):
    if member.guild.id == SERVER_ID and (before.channel != after.channel):
        now = datetime.utcnow() + timedelta(hours=9)
        alert_channel = client.get_channel(CHANNEL_ID)
        print(alert_channel)
        if before.channel is None: 
            msg = f'@everyone {now:%H:%M} に {member.name} が {after.channel.name} に参加したよ'
            await alert_channel.send(msg)
        elif after.channel is None: 
            msg = f'{now:%H:%M} に {member.name} が {before.channel.name} から退出したよ'
            await alert_channel.send(msg)

client.run(TOKEN)
