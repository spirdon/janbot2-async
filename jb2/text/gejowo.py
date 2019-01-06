import random
import requests
import discord

from bs4 import BeautifulSoup
from jb2.bot import bot

def random_ad():
    category = 7
    full_link = "http://anonse.gejowo.pl/?m=list&pg={}&cat={}"
    req = requests.get(full_link.format(1, category))
    data = req.text
    soup = BeautifulSoup(data, "html.parser")
    pagination_div = soup.find("div", {"class": "pagination"})

    try:
        last_page = int(pagination_div.find_all("a")[-2].string)
    except IndexError or ValueError:
        last_page = 1
    
    page = random.randint(1, last_page)
    req = requests.get(full_link.format(page, category))
    data = req.text
    soup = BeautifulSoup(data, "html.parser")
    random_ads = soup.find_all("div", {"class": "adcontent"})
    return random.choice(random_ads).string


@bot.command()
async def gejowo(ctx):
    emoji = ':rainbow:'

    title = emoji + " Gejowski anons"

    footer_text = "Gejowski anons dla " + str(ctx.author)
    text = random_ad()
    emb = discord.Embed(title=title, description=text, color=0xff9999)
    emb.set_footer(text=footer_text, icon_url=ctx.author.avatar_url)

    await ctx.send(embed=emb)

    