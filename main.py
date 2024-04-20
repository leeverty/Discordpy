import discord
from discord.ext import commands
import os
import asyncio
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

def read_activities(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]
    
activities_file = 'activities.txt'
activities = read_activities(activities_file)

async def update_activity():
    activity = discord.Activity(type=discord.ActivityType.playing, name=random.choice(activities))
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=activity)
    print(f"Status set to {activity.type.name}: {activity.name}")
    await asyncio.sleep(10)

@bot.command()
async def reload_activities(ctx):
    global activities
    activities = read_activities(activities_file)
    await ctx.send('Activities reloaded!')

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    await update_activity()
    print("Loaded cogs:")
    for cog in bot.cogs:
        print(cog)

async def setup():
    for folder in ['./cogs', './automods']:
        for filename in os.listdir(folder):
            if filename.endswith('.py') and not filename.startswith('_'):
                cog_name = os.path.splitext(filename)[0]
                await bot.load_extension(f'{folder[2:].replace("/", ".")}.{cog_name}')

if __name__ == '__main__':
    bot.setup_hook = setup  # Set up hook to load cogs before running the bot
    bot.run('Your bot token')

