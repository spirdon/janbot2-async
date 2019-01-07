import asyncio
import os
import logging
import datetime
import discord

from jb2.bot import bot
from jb2.text.elo import elo
from jb2.text.gejowo import gejowo
from jb2.text.przondlo import przondlo
from jb2.text.szkaluj import szkaluj
from jb2.text.ufnal import ufnal

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s: %(message)s')
logger = logging.getLogger('janbot2')

@bot.event
async def on_ready():
    logger.info("JanBot2 gotowy!")
    logger.info("Zalogowano jako: {}".format(bot.user.name))

discordchan_id = 411952528499015691
log_channel_id = 531586622026678293
infiltration_id = 531783516296577024

@bot.event
async def on_message(message):
    if message.guild.id == discordchan_id:
        return
    if message.channel.id == log_channel_id:
        return
    if message.author.bot:
        return

    channel = bot.get_channel(infiltration_id)

    emb = discord.Embed(title="{} zapostował wiadomość".format(message.author),
                        timestamp=datetime.datetime.now())
    emb.description = "[{}#{}] {}".format(message.guild.name, 
                                          message.channel.name, 
                                          message.content)

    await channel.send(embed=emb)
@bot.event
async def on_message_delete(message):
    if message.guild.id != discordchan_id:
        return
    if message.channel.id == log_channel_id:
        return
    if message.author.bot:
        return

    channel = bot.get_channel(log_channel_id)

    emb = discord.Embed(title="{} usunięto wiadomość".format(message.author),
                        timestamp=datetime.datetime.now())
    emb.description = "[{}#{}] {}".format(message.guild.name, 
                                          message.channel.name, 
                                          message.content)

    await channel.send(embed=emb)

@bot.event
async def on_message_edit(before, after):
    if before.guild.id != discordchan_id:
        return
    if before.channel.id == log_channel_id:
        return
    if before.author.bot:
        return
    if before.content == after.content:
        return

    channel = bot.get_channel(log_channel_id)

    emb = discord.Embed(title="{} zedytował wiadomość".format(before.author),
                        timestamp=datetime.datetime.now())
    emb.description = "[{}#{}]\n**Przed**:\n{}\n\n**Po**:\n{}".format(
        before.guild.name,
        before.channel.name, 
        before.content,
        after.content)

    await channel.send(embed=emb)

if __name__ == '__main__':
    TOKEN = os.environ['DISCORD_TOKEN']
    bot.run(TOKEN)
