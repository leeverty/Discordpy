import discord
from discord.ext import commands

class purge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def purge(self, ctx, num: int):
        await ctx.channel.purge(limit=num)

# This function needs to be asynchronous
async def setup(bot):
    await bot.add_cog(purge(bot))
