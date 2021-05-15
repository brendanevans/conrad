import os
from discord import Embed, TextChannel, User
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(hidden=True)
    @commands.has_permissions(administrator=True)
    async def reload(self, ctx):
        for file in os.listdir('./cogs'):
            if file.endswith('.py'):
                self.bot.reload_extension(f'cogs.{file[:-3]}')
        await ctx.send(f"Reloaded all Cogs")

def setup(bot):
    bot.add_cog(Admin(bot))