import discord
from discord.ext import commands

class Utility(commands.Cog, name="utility"):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(
        name="ping",
        help="Shows the ping / latency of the bot in miliseconds.",
    )
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')

        if round(self.bot.latency * 1000) <= 50:
            color = 0x44ff44
        elif round(self.bot.latency * 1000) <= 100:
            color = 0xffd000
        elif round(self.bot.latency * 1000) <= 200:
            color = 0xff6600
        else:
            color = 0x990000
        embed=discord.Embed(title="PONG", description=f":ping_pong: Pong! {round(self.bot.latency * 1000)}ms", color=color)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Utility(bot))