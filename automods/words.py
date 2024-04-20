import discord
from discord.ext import commands

# Banned words list; configure this as needed
BANNED_WORDS = {"nigga", "nigger", "NIGGA", "Nigga", "NIGGER", "Nigger"}

class words(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        # Do not process if the message is sent by the bot
        if message.author.bot:
            return

        # Check if any banned word is in the message
        if any(word in message.content.lower() for word in BANNED_WORDS):
            # Delete the offending message
            await message.delete()
            # Send a warning to the user
            warning = f"Nuh uh"
            await message.channel.send(f"{message.author.mention} {warning}")

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        # Recheck the message on edit
        await self.on_message(after)

async def setup(bot):
    await bot.add_cog(words(bot))
