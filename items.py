from clear_console import clear_terminal
from time import sleep


class Trader:
    def __init__(self, trader: dict) -> None:
        self.type = 'trader'
        try:
            self.item = trader['item']
            self._name = trader['name']
        except KeyError:
            raise KeyError('The dictionary should contain keys: name, item')
        try:
            self.item["price"] = int(self.item["price"])
        except Exception:
            raise ValueError('Price should be a number')

    @property
    def name(self) -> str:
        return self._name

    def sell_key(self, player: object) -> None:
        player.backpack.add_key()
        player.backpack.spend_coins(self.item['price'])
        self.item = {}

    def introduce(self, player: object) -> None:
        while True:
            clear_terminal()
            print(f"Hello my name is {self.name} and "
                  "I am a trader here in this city. "
                  "Let me introduce my offer.")
            self.introduce_offer()
            print('1.Check your sack\n2.Buy item\n3.Finish conversation')
            decision = int(input("Enter number of your decision: "))
            if decision not in (1, 2, 3):
                clear_terminal()
                print('Invalid decision. Please try again.')
                sleep(2)
            elif decision == 1:
                clear_terminal()
                print(f'You have {player.backpack.coins} '
                      'coins in your sack.')
                sleep(2)
            elif decision == 2:
                clear_terminal()
                if self.item == {}:
                    print("I dont have anything to offer")
                    sleep(2)
                elif player.backpack.coins < self.item['price']:
                    print('You do not have enough coins.')
                    sleep(2)
                else:
                    clear_terminal()
                    self.sell_key(player)
                    print('Done! Goodbye!')
                    sleep(2)
                    break
            elif decision == 3:
                clear_terminal()
                print("Goodbye!")
                sleep(2)
                break

    def introduce_offer(self) -> None:
        if self.item != {}:
            print(f'1. {self.item["name"]} : {self.item["description"]}\n'
                  f'\tThis item costs {self.item["price"]} coins.\n')
        else:
            print('I dont have anything to offer.\n')


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
        print('You have the key! The game is complete!')
        if input("Press enter to return to home screen:"):
            return
