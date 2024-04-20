import discord
from discord.ext import commands

import google.generativeai as genai


class AIChat(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    genai.configure(api_key="AIzaSyBONHCMWVuB2E4iDiGv4n7qtTq5NIFZ8yk")
    self.model = genai.GenerativeModel('gemini-pro',
      safety_settings=[
        {
          "category": "HARM_CATEGORY_DANGEROUS",
          "threshold": "BLOCK_NONE",
        },
        {
          "category": "HARM_CATEGORY_HARASSMENT",
          "threshold": "BLOCK_NONE",
        },
        {
          "category": "HARM_CATEGORY_HATE_SPEECH",
          "threshold": "BLOCK_NONE",
        },
        {
          "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
          "threshold": "BLOCK_NONE",
        },
        {
          "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
          "threshold": "BLOCK_NONE",
        },
      ]
    )

  @commands.command(name="ai")
  async def ai(self, ctx: commands.Context, *, prompt: str):
    response = self.model.generate_content(prompt)
    await ctx.reply(response.text)

async def setup(bot):
    await bot.add_cog(AIChat(bot))



