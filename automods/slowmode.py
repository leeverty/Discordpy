import discord
from discord.ext import commands

class slowmode(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def slowmode(self, ctx, seconds: int):
        """Set slowmode in the current channel."""
        await ctx.channel.edit(slowmode_delay=seconds)
        embed = discord.Embed(
            title="Slowmode Enabled",
            description=f"Slowmode set to {seconds} seconds in this channel.",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def remove_slowmode(self, ctx):
        """Remove slowmode in the current channel."""
        await ctx.channel.edit(slowmode_delay=0)
        embed = discord.Embed(
            title="Slowmode Disabled",
            description="Slowmode has been disabled in this channel.",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title="Permission Error",
                description="You don't have permission to use this command.",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                title="Invalid Argument",
                description="Please provide a valid number of seconds.",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(slowmode(bot))
