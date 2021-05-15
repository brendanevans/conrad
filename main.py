import discord
import json
import os

from discord.ext.commands import Bot

#Load the config file
with open('config.json' ,'r') as r:
    config = json.load(r)

botPrefix=('!')
bot = Bot(command_prefix=botPrefix, case_insensitive=True)

@bot.event
async def on_ready():
    print(f"Connected and ready")

if __name__ == '__main__':
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            bot.load_extension(f'cogs.{file[:-3]}')
    bot.run(config['secret'])