import discord
from discord.ext import commands
import random

class Flip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='coinflip', help='Flip a coin')
    async def coinflip(self, ctx):
        # Flip the coin (0 for heads, 1 for tails)
        result = random.choice(['Heads', 'Tails'])

        # Create an embed to display the result
        embed = discord.Embed(title="Coin Flip", color=discord.Color.blurple())
        embed.add_field(name="Result", value=result, inline=False)
        embed.set_footer(text=f"Requested by {ctx.author.display_name}", icon_url=ctx.author.avatar_url)

        # Send the embed
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Flip(bot))
