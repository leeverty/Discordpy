import discord
import random
from discord.ext import commands

class Joke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='joke', help='Tells a random joke')
    async def joke(self, ctx):
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Parallel lines have so much in common. It’s a shame they’ll never meet.",
            "I told my wife she was drawing her eyebrows too high. She looked surprised.",
            "I'm reading a book on anti-gravity. It's impossible to put down!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why did the bicycle fall over? Because it was two-tired!"
        ]
        response = random.choice(jokes)
        await ctx.send(response)

async def setup(bot):
    await bot.add_cog(Joke(bot))
