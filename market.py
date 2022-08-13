import requests


def find_cheapest_onion(item_id=8166):
    """Find five lowest prices for provided item id. If no item id is provided, defaults to 8166 ("Thavnairian Onion").

    Args:
        item_id (int, optional): Unique id for item of interest. Defaults to 8166.

    Returns:
        str: ASCII table containing five lowest prices found for item id.
    """
    url = f'https://universalis.app/api/v2/North-America/{item_id}'
    response = requests.get(url)

    data = response.json()

    top_five = data['listings'][:5]

    results_table = "```\n"
    results_table += f"Top five prices for https://universalis.app/market/{item_id}\n"
    results_table += "+---------------+---------------+-----+\n"
    results_table += "| Server        | Price         | Qty |\n"
    results_table += "+---------------+---------------+-----+\n"

    for item in top_five:
        world = item['worldName']
        price = str(item['pricePerUnit'])
        qty = str(item['quantity'])

        results_table += f"| {world}" + " " * (14 - len(world))
        results_table += f"| {price}" + " " * (14 - len(price))
        results_table += f"| {qty}" + " " * (4 - len(qty)) + "|"
        results_table += "\n"

    results_table += "+---------------+---------------+-----+\n"
    results_table += "```"

    return results_table
