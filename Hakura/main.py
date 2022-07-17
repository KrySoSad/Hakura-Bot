from sqlite3 import Timestamp
import discord
from discord.ext import commands
import random
from datetime import timezone, datetime



TOKEN = 'OTU0OTQ5NDA1OTgxNzAwMTE4.GGEYVH.dfQcvpN8MuUxKfNQQbczPp5Hi5XU6ZdKtOlUoM'

client = commands.Bot(command_prefix='h.')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='Em là nhất'))
    print("we have logged in as {0.user}".format(client))

        
@client.command()
async def test(ctx):
    await ctx.send(f"done! {ctx.author.name}")

@client.command()
async def ping(ctx):
    ping = discord.Embed(title = f"Pong! Your latency is {round(client.latency*1000)}ms", color = discord.Colour.blue(), timestamp = datetime.now(timezone.utc))
    ping.set_author(name = f'{ctx.author.name}')
    ping.set_footer(text = 'Thank you so much')
    msg = await ctx.send(embed = ping )
    await msg.add_reaction('<:mimcuoi:950941408347439145>') 

@client.command()
async def h(ctx):
    embed = discord.Embed(title = f"❓ Can I help you ❓",description = "Some useful commands can help you!!",color = discord.Colour.blue()) 
    embed.set_footer(text = 'Thank you so much')
    embed.set_thumbnail(url = 'https://i.pinimg.com/564x/7e/6d/df/7e6ddf4bcc44c8b2686f3b54a84a8b34.jpg')
    embed.set_author(name = f'{ctx.author.name}')
    embed.add_field(name ='h.ping',value = 'Check the response speed',inline= False )
    embed.add_field(name ='h.lottery',value = 'Play lottery <:mimcuoi:950941408347439145>',inline= True )
    embed.add_field(name ='h.joined <name>',value = 'Check member when his/her joined',inline=False )   
    await ctx.send(embed=embed)
    


@client.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

@client.command()
async def joined(ctx, member: discord.Member):
    jnd = discord.Embed(title = '{0.name} đã tham gia vào {0.joined_at}'.format(member), color = discord.Colour.blue())
    await ctx.send(embed = jnd)

@client.command()
async def lottery(ctx):
    await ctx.send(f'Hi {ctx.author.mention}, choose your number 1-20!')
    x = random.randint(1,20)
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and int(msg.content) in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    msg = await client.wait_for("message", check=check)
    if int(msg.content) == x:
        await ctx.send(f'Congratulations {ctx.author.mention}, you won!!')
    else:
        await ctx.send(f'Nope {ctx.author.mention} :( , is was {x}')


def it_is_me(ctx):
    return ctx.author.id ==  874321270437728257

@client.command()
@commands.check(it_is_me)
async def clear(ctx, amount = 6):
    await ctx.channel.purge(limit = amount)
    await ctx.send('Đã clear 5 tin nhắn!')    




client.run(TOKEN)
