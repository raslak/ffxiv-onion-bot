import os

from discord.ext import commands
from dotenv import load_dotenv

from market import find_cheapest_onion


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='commands')
async def commands(ctx):
    response = "```\n"
    response += "+------------------+---------------------------------------------------------+\n"
    response += "| Command          | Description                                             |\n"
    response += "+------------------+---------------------------------------------------------+\n"
    response += "| onion            | Five lowest thavnairian onion prices in NA data centers.|\n"
    response += "| prices <item_id> | Five lowest prices for <item_id> in NA data centers.    |\n"
    response += "+------------------+---------------------------------------------------------+\n"
    response += "```"

    await ctx.send(response)

@bot.command(name='onion')
async def onion(ctx):
    try:
        response = find_cheapest_onion()
    except Exception:
        response = 'Unable to find prices'
    
    await ctx.send(response)

@bot.command(name='prices')
async def prices(ctx, arg):
    item_id = arg
    try:
        response = find_cheapest_onion(item_id)
    except Exception:
        response = 'Unable to find prices'
    
    await ctx.send(response)

bot.run(TOKEN)