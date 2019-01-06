import asyncio
import os
import logging
from discord.ext import commands

logging.basicConfig(
    level='DEBUG', format='%(asctime)s - %(name)s - %(levelname)s: %(message)s')
logger = logging.getLogger('janbot2')

bot = commands.Bot("!")

@bot.event
async def on_ready():
    logger.info("JanBot2 gotowy!")
    logger.info("Zalogowano jako: {}".format(bot.user.name))

@bot.command()
async def elo(ctx):
    await ctx.send("No elo.")

if __name__ == '__main__':
    TOKEN = os.environ['DISCORD_TOKEN']
    bot.run(TOKEN)
