import discord
from discord.ext import commands
from discord import Client
from discord import Server
import configparser
import os
config = configparser.ConfigParser()
config.read('config.ini')

bot = commands.Bot(command_prefix='!')
client = discord.Client()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await client.login(config['TOKEN']['TOKEN'])

@bot.command(pass_context=True)
async def kickall(ctx):
    if ctx.message.author.server_permissions.administrator and ctx.message.server.me.server_permissions.kick_members:
        for member in ctx.message.server.members:
            if member != ctx.message.author and member != ctx.message.server.me:
                await client.kick(member)
        await bot.say('All members kicked.')
    else:
        await bot.say('Error: Not administrator')
bot.run(config['TOKEN']['TOKEN'])
