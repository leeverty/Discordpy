import discord
import random
from discord.ext import commands

class Slots(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

class Slots(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def slots(self, ctx):
        # Your slots command implementation here
        await ctx.send("This is the slots command!")

    @commands.command(name='slots', help='Play the slots game')
    async def slots(self, ctx):
        symbols = ['🍒', '🍋', '🍊', '🍇', '🍉', '🍓', '🍍', '🥝', '🍎', '🍏']
        spins = [random.choice(symbols) for _ in range(3)]

        # Check for winning combinations
        if spins[0] == spins[1] == spins[2]:
            result = "Congratulations! You won!"
            color = 0x00ff00  # Green color for win
        else:
            result = "Sorry, you lost."
            color = 0xff0000  # Red color for loss

        # Create embed
        embed = discord.Embed(title="Slots", color=color)
        embed.add_field(name="Player ", value=ctx.author.mention, inline=False)
        embed.add_field(name="Fruits", value=' '.join(spins), inline=False)
        embed.add_field(name="Result", value=result, inline=False)

        message = await ctx.reply(embed=embed)

        # Add reaction for spinning again
        await message.add_reaction('🔄')  # Repeat emoji

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == '🔄' and reaction.message == message

        try:
            reaction, _ = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
        except:
            pass  # If the player doesn't react within 60 seconds, do nothing
        else:
            # Spin again if player reacts
            await self.slots(ctx)

async def setup(bot):
    await bot.add_cog(Slots(bot))
