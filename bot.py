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
    response += "+-----------------------------------------------+------------------------+\n"
    response += "| Command                                       | Example                |\n"
    response += "+-----------------------------------------------+------------------------+\n"
    response += "| onion <world_dc_region>                       | !onion primal          |\n"
    response += "| prices <item_ids> <world_dc_region, optional> | !prices 8166 ultros    |\n"
    response += "+------------------+-----------------------------------------------------+\n"
    response += "```"

    await ctx.send(response)

@bot.command(name='onion')
async def onion(ctx, world_dc_region="North-America"):
    try:
        response = find_cheapest_onion(item_ids=8166, world_dc_region=world_dc_region)
    except Exception:
        response = 'Unable to find prices'
    
    await ctx.send(response)

@bot.command(name='prices')
async def prices(ctx, item_ids, world_dc_region="North-America"):
    try:
        response = find_cheapest_onion(item_ids=item_ids, world_dc_region=world_dc_region)
    except Exception:
        response = 'Unable to find prices'
    
    await ctx.send(response)

bot.run(TOKEN)