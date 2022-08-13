import requests


def find_cheapest_onion() -> str:
    url = 'https://universalis.app/api/v2/North-America/8166'
    response = requests.get(url)

    data = response.json()

    top_five = data['listings'][:5]

    results_table = "```\n"
    results_table += "Top five prices\n"
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
