import random
import discord

from jb2.bot import bot

with open('res/text/elo.txt') as file:
    global greetings
    greetings = file.readlines()

@bot.command()
async def elo(ctx):
    global greetings
    
    emoji = ':wave:'
    answer = random.choice(greetings)

    text = '{} {}: {}'.format(emoji, ctx.author.mention, answer)
    emb = discord.Embed(description=text, color=0xffffaa)
    
    await ctx.send(embed=emb)