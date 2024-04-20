import discord
from discord.ext import commands

class lockunlock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx):
        """Lock the current channel."""
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        embed = discord.Embed(
            title="Channel Locked",
            description="This channel has been locked.",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx):
        """Unlock the current channel."""
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        embed = discord.Embed(
            title="Channel Unlocked",
            description="This channel has been unlocked.",
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

async def setup(bot):
    await bot.add_cog(lockunlock(bot))
