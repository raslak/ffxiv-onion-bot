import json
import requests


def find_cheapest_onion(item_ids, world_dc_region="North-America"):
    """Find five lowest prices for provided item id. By default the
    results will be limited to all NA data centers. The optional "world_dc_region"
    parameter can be used to specify a data center or world. 

    Args:
        item_id (int): Unique id for item of interest.
        world_dc_region (str, optional): Region, data center, or world.

    Returns:
        str: ASCII table containing five lowest prices found for item id.
    """
    url = f'https://universalis.app/api/v2/{world_dc_region}/{item_ids}'
    response = requests.get(url)
    data = response.json()

    lowest_five = data['listings'][:5]
    
    item_id_map = json.load(open('items.json'))
    item_name = 'Unknown'
    if str(item_ids) in item_id_map.keys():
        item_name = item_id_map[str(item_ids)]['en']

    results_table = "```\n"
    results_table += f"Best prices for {item_name} on {world_dc_region.title()}\n"
    results_table += "+---------------+---------------+-----+\n"
    results_table += "| Server        | Price         | Qty |\n"
    results_table += "+---------------+---------------+-----+\n"

    for item in lowest_five:
        if 'worldName' in item.keys():
            world = item['worldName']
        else:
            world = world_dc_region.title()

        price = str(item['pricePerUnit'])
        qty = str(item['quantity'])

        results_table += f"| {world}" + " " * (14 - len(world))
        results_table += f"| {price}" + " " * (14 - len(price))
        results_table += f"| {qty}" + " " * (4 - len(qty)) + "|"
        results_table += "\n"

    results_table += "+---------------+---------------+-----+\n"
    results_table += "```"
    results_table += f"Source: https://universalis.app/market/{item_ids}"

    return results_table
