import codecs
import aiohttp
import discord
from bs4 import BeautifulSoup
from discord.ext import commands

class Translate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()  # Create a session to use for HTTP requests

    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())  # Close the session when the cog is unloaded

    @commands.command()
    async def translate(self, ctx, to_language, *, msg):
        """Translates words from one language to another."""
        await ctx.message.delete()
        if to_language == "rot13":
            embed = discord.Embed(color=discord.Color.blue())
            embed.add_field(name="Original", value=msg, inline=False)
            embed.add_field(name="ROT13", value=codecs.encode(msg, "rot_13"), inline=False)
            return await ctx.send(embed=embed)
        
        async with self.session.get("https://gist.githubusercontent.com/astronautlevel2/93a19379bd52b351dbc6eef269efa0bc/raw/18d55123bc85e2ef8f54e09007489ceff9b3ba51/langs.json") as resp:
            lang_codes = await resp.json(content_type='text/plain')
        
        real_language = False
        to_language = to_language.lower()
        for entry in lang_codes:
            if to_language in lang_codes[entry]["name"].replace(";", "").replace(",", "").lower().split():
                language = lang_codes[entry]["name"].replace(";", "").replace(",", "").split()[0]
                to_language = entry
                real_language = True
        
        if real_language:
            async with self.session.get("https://translate.google.com/m",
                                         params={"hl": to_language, "sl": "auto", "q": msg}) as resp:
                translate = await resp.text()
            result = str(translate).split('class="t0">')[1].split("</div>")[0]
            result = BeautifulSoup(result, "lxml").text
            
            embed = discord.Embed(color=discord.Color.blue())
            embed.add_field(name="Original", value=msg, inline=False)
            embed.add_field(name=language, value=result.replace("&amp;", "&"), inline=False)
            
            if result == msg:
                embed.add_field(name="Warning", value="This language may not be supported by Google Translate.")
            
            await ctx.send(embed=embed)
        else:
            await ctx.send("That's not a real language.")

async def setup(bot):
    await bot.add_cog(Translate(bot))
