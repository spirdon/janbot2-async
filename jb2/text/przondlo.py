import random
import discord

from jb2.bot import bot

def przondling(text):
    przondling_factor = 0.3
    letter_dict = {
        'q': 'qwas',
        'w': 'qweasd',
        'e': 'wresfd',
        'r': 'rtefdg',
        't': 'yrtghf',
        'y': 'uythg',
        'u': 'iuyjkh',
        'i': 'ioukjl',
        'o': 'ipokl',
        'p': 'pol',
        'a': 'qasz',
        's': 'wsadx',
        'd': 'erdfsxc',
        'f': 'rtdfgcv',
        'g': 'tygfhbv',
        'h': 'uyjghnb',
        'j': 'uikjhmn',
        'k': 'iojklm,',
        'l': 'pokl',
        'z': 'aszx',
        'x': 'sdxzc',
        'c': 'xcv',
        'v': 'bvc',
        'b': 'vbn',
        'n': 'bmn',
        'm': 'mnjkl'
    }
    out = ""
    for l in list(text):
        if l not in letter_dict:
            out += l
            continue
        r = random.uniform(0.0, 1.0)

        if r > 0.05:
            new_text = l
        else:
            new_text = ""

        while True:
            r = random.uniform(0.0, 1.0)
            if r < przondling_factor:
                r2 = random.choice([1, 2])
                char = random.choice(list(letter_dict[l]))
                if r2 == 1:
                    new_text += char
                else:
                    new_text = char + new_text
            else:
                break
        out += new_text

    return out


@bot.command()
async def przondlo(ctx, *args):
    emoji = ':bee:'
    answer = przondling(' '.join(args))

    text = '{} {}: {}'.format(emoji, ctx.author.mention, answer)
    emb = discord.Embed(description=text, color=0xff7777)
    
    await ctx.send(embed=emb)