import json
from world import World
from location import Location
from monsters import Monster_level_1, Monster_level_2, Monster_level_3
from items import Trader, Backpack
from clear_console import clear_terminal


class Player:
    def __init__(self, file_name: str) -> None:
        with open(file_name, 'r') as file:
            data = json.loads(file)
            self.health = data["health"],
            self.hit_strength = data["hit_strength"],
            self.backpack = Backpack(data['backpack']['coins'])
            self.location = (data["location"]['x'], data["location"]['y'])

    def is_alive(self, damage: int) -> bool:
        return (self.health - damage > 0)

    def attack(self) -> None:
        return self.hit_strength

    def get_damage(self, damage: int) -> None:
        if self.is_alive(damage):
            self.health -= damage
        else:
            self.die()

    def die(self) -> bool:
        print('Game over!')
        # od poczatku

    def heal(self) -> None:
        with open("player.json", 'r') as file:
            data = json.loads(file)
            self.health = data["health"]

    def give_options(self, current_loc: Location) -> list:
        moves_list = []
        if current_loc.is_monster:
            if current_loc.object.is_alive(0):
                moves_list = [move
                              for move in current_loc.moves['monster alive']]
            else:
                moves_list = [move
                              for move in current_loc.moves['monster dead']]
        else:
            moves_list = [move for move in current_loc.moves]
        return moves_list

    def decision(self, current_loc: Location, world: World) -> None:
        list_of_moves = self.give_options(current_loc)
        print(list_of_moves)
        decision = input("Please write your choice: ").lower()
        if decision not in list_of_moves:
            raise ValueError(f'You cannot make that move.'
                             f'Try one of these: {list_of_moves}.')
        else:
            if decision == 'go east':
                self.go_east(world)
            if decision == ' go west':
                self.go_west(world)
            if decision == 'go south':
                self.go_south(world)
            if decision == 'go north':
                self.go_north(world)
            if decision == 'fight monster':
                self.fight_monster(current_loc.object)
            if decision == 'talk to trader':
                self.talk_to_trader(current_loc.object)

    def find_location(self, coords: tuple, location_list: list) -> Location:
        cnt = 0
        while coords != location_list[cnt].coordinates:
            loc = location_list[cnt]
            cnt += 1
        if coords != loc.coordinates:
            raise IndexError("Location with coordinates not found")
        else:
            return loc

    def go_east(self, world: object) -> None:
        new_loc = self.location[0] - 1
        if new_loc < 0:
            self.location[0] = world.size - 1
        else:
            self.location[0] = new_loc
        curr_loc = self.find_location()
        print(curr_loc.description)

    def go_west(self, world: object) -> None:
        new_loc = self.location[0] + 1
        if new_loc > world.size - 1:
            self.location[0] = 0
        else:
            self.location[0] = new_loc
        coordinates = (self.location[0], self.location[1])
        curr_loc = self.find_location(coordinates, world.location_list)
        print(curr_loc.description)

    def go_north(self, world: object) -> None:
        new_loc = self.location[1] - 1
        if new_loc < 0:
            self.location[1] = world.size - 1
        else:
            self.location[1] = new_loc
        curr_loc = self.find_location()
        print(curr_loc.description)

    def curr_loc_description(curr_loc: Location) -> None:
        clear_terminal()
        if curr_loc.is_monster():
            if curr_loc.object.is_alive(0):
                print(curr_loc.description['monster alive'])
            else:
                print(curr_loc.description['monster dead'])
        else:
            print(curr_loc.description)

    def go_south(self, world: object) -> None:
        new_loc = self.location[1] + 1
        if new_loc > world.size - 1:
            self.location[1] = 0
        else:
            self.location[1] = new_loc
        curr_loc = self.find_location()
        self.curr_loc_description(curr_loc)

    def fight_status(self, monster: object):
        print(f'Your hp is: {self.health}.'
              f'Monsters hp is: {monster.health}.')

    def fight_monster(self, monster: Monster_level_1) -> None:
        print(f'You are fighting monster level 1 named {monster.name}.')
        while monster.is_alive(0) and self.is_alive(0):
            self.fight_status(monster)
            monster.get_damage(self.attack())
        if self.is_alive(0):
            clear_terminal()
            print('You have defeated the monster. You are healed.')
            self.heal()

    def fight_monster_level_2(self, monster: Monster_level_2) -> None:
        print(f'You are fighting monster level 2 named {monster.name}.')
        while monster.is_alive(0) and self.is_alive(0):
            self.fight_status(monster)
            monster.get_damage(self.attack())
            self.get_damage(monster.attack_player())
        if self.is_alive(0):
            clear_terminal()
            print('You have defeated the monster. You are healed.')
            self.heal()

    def fight_monster_level_3(self, monster: Monster_level_3) -> None:
        print(f'You are fighting monster level 3 named {monster.name}.')
        while monster.is_alive(0) and self.is_alive(0):
            self.fight_status(monster)
            monster.get_damage(self.attack())
            self.get_damage(monster.attack_player())
            monster.heal()
        if self.is_alive(0):
            clear_terminal()
            print('You have defeated the monster. You are healed.')
            self.heal()

    def talk_to_trader(self, trader: Trader) -> None:
        trader.introduce()

    def receive_coins(self, coins: int) -> None:
        self.backpack.add_coins(coins)

    def help():
        pass
