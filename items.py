class Item:
    def __init__(self, item: dict):
        self.name = item['name']
        self.description = item['description']
        self.price = item['price']

    def get_description(self):
        pass


class Trader:
    def __init__(self, trader: dict):
        self.type = 'trader'
        pass

    def trade_item():
        pass

    def introduce():
        pass

    def introduce_offer():
        pass


class Backpack:
    def __init__(self, coins: int):
        self.coins = coins
        self.is_key = False

    def add_coins(self, coins: int) -> None:
        self.coins += coins

    def spend_coins(self, amount):
        self.coins -= amount

    def add_key(self):
        self.is_key = True
