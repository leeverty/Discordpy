import discord
from discord.ext import commands

class Spam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='spam', help='Spam a message')
    async def spam_message(self, ctx, *, message_and_count: str):
        # Split the message_and_count string into the message and the count
        message, count = message_and_count.rsplit(' ', 1)
        count = int(count)

        # Check if the count is valid
        if count <= 0 or count > 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999:  # Limit the count to avoid abuse
            await ctx.send("Please specify a valid number of messages to spam (1 to ).999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999")
            return

        # Send the message multiple times
        for _ in range(count):
            await ctx.send(message)

async def setup(bot):
    await bot.add_cog(Spam(bot))
