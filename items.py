from clear_console import clear_terminal
from player import Player


class Item:
    def __init__(self, item: dict) -> None:
        try:
            self.name = item['name']
            self.description = item['description']
            self.price = item['price']
        except KeyError:
            raise KeyError('The dictionary should contain keys:'
                           'name, description, price')

    def get_description(self) -> str:
        return f'{self.description}. This item costs {self.price} coins'


class Trader:
    def __init__(self, trader: dict) -> None:
        self.type = 'trader'
        self.item = {
            "name": "key",
            "description": "",
            "price": 100
        }
        try:
            self._name = trader['name']
        except KeyError:
            raise KeyError('The dictionary should contain keys: name')

    @property
    def name(self) -> str:
        return self._name

    def sell_key(self, player: Player) -> None:
        player.backpack.add_key()
        player.backpack.spend_coins(self.item['price'])
        self.item = {}

    def def_objects(self, trader: dict) -> None:
        list_of_objects = []
        for object in trader['backpack']:
            list_of_objects.append(Item(object))
        self._backpack = list_of_objects

    def introduce(self, player: Player) -> None:
        clear_terminal()
        print("Hello my name is {self.name} and"
              "I am a trader here in this city. Let me introduce my offer.")
        if self.item != {}:
            self.introduce_offer()
            while True:
                print('1. Buy item\n2.Finish conversation')
                decision = input("Enter number of your decision: ")
                if decision not in (1, 2):
                    raise ValueError("The decision can be 1 or 2")
                elif decision == 1:
                    if player.backpack.coins >= self.item['price']:
                        print('You dont have enough coins.')
                    else:
                        self.sell_key(player)
                elif decision == 2:
                    print("Goodbye!")
                    break
        else:
            print("I dont have anything to offer")

    def introduce_offer(self) -> None:
        print(f'1. {self.item["name"]} : {self.item["description"]}\n'
              f'This item costs {self.item["price"]}')


class Backpack:
    def __init__(self, coins: int) -> None:
        self.coins = coins
        self.is_key = False

    def add_coins(self, coins: int) -> None:
        self.coins += coins

    def spend_coins(self, amount: int) -> None:
        self.coins -= amount

    def add_key(self) -> None:
        self.is_key = True
