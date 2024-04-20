import discord
from discord.ext import commands

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} has joined the server.')
        role = member.guild.get_role(1221768142112686111)
        if role:
            await member.add_roles(role)
            print(f'Assigned role {role.name} to {member.display_name}')

async def setup(bot):
    await bot.add_cog(Welcome(bot))

