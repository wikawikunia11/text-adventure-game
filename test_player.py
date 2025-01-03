import json
from items import Backpack


with open("locations.json", 'r') as file:
    data = json.load(file)
    loc = data['locations']
    print(loc[6]['description']['monster dead'])

    items = [{"name": "milk"}, {"name": "cheese"}]
    backpack = Backpack(items, 10)
    backpack.check_items()
