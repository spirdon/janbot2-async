import random
import requests
import discord

from bs4 import BeautifulSoup
from jb2.bot import bot

def random_ufnalism():
    last_page = 5
    page = random.randint(1, last_page)
    r = requests.get("https://steamcommunity.com/profiles/76561198014133816/allcomments?ctp={}".format(page))
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    random_ads = [a for a in soup.findAll("div", {"class": "commentthread_comment_text"}) if a.string is not None]
    return random.choice(random_ads).string.strip()


@bot.command()
async def ufnal(ctx):
    emoji = ':beer:'

    title = emoji + " Losowy ufnalizm"

    footer_text = "Losowy ufnalizm dla " + str(ctx.author)
    text = random_ufnalism()
    emb = discord.Embed(title=title, description=text, color=0xffff77)
    emb.set_footer(text=footer_text, icon_url=ctx.author.avatar_url)

    await ctx.send(embed=emb)