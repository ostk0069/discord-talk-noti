import discord

TOKEN = 'NzMzNzA1NDkzNTQ5MTU0Mzc2.XxHCfQ.ECQZLtCD4rPwZo79fsyoN4TLHow'

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
