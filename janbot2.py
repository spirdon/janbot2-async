import asyncio
import os
import logging

from jb2.bot import bot
from jb2.text.elo import elo
from jb2.text.gejowo import gejowo
from jb2.text.przondlo import przondlo
from jb2.text.ufnal import ufnal

logging.basicConfig(
    level='DEBUG', format='%(asctime)s - %(name)s - %(levelname)s: %(message)s')
logger = logging.getLogger('janbot2')

@bot.event
async def on_ready():
    logger.info("JanBot2 gotowy!")
    logger.info("Zalogowano jako: {}".format(bot.user.name))

if __name__ == '__main__':
    TOKEN = os.environ['DISCORD_TOKEN']
    bot.run(TOKEN)
