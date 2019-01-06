import random
import discord

from jb2.bot import bot
from jb2.embed import error_embed

with open('res/text/szkalunki.txt', encoding="utf8") as file:
    global slanders
    slanders = file.readlines()

@bot.command()
async def szkaluj(ctx, *args):
    global slanders

    if len(args) < 1:
        emb = error_embed(ctx.author.mention, "Podaj kogo szkalujesz.")
    else:       
        text = random.choice(slanders).format(' '.join(args))
        footer_text = "Szkalunek dla " + str(ctx.author)
        emb = discord.Embed(description=text, color=0x777777)
        emb.set_footer(text=footer_text, icon_url=ctx.author.avatar_url)
    
    await ctx.send(embed=emb)