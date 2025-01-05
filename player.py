import json
from items import Backpack
from clear_console import clear_terminal


class Player:
    def __init__(self, file_name: str) -> None:
        try:
            with open(file_name, 'r') as file:
                data = json.load(file)
                try:
                    if data["health"] <= 0:
                        raise ValueError('Health must be positive')
                    else:
                        self.health = data["health"]
                        self._max_health = data["health"]
                    if data["hit_strength"] < 0:
                        raise ValueError('Hit strength must be positive')
                    else:
                        self.hit_strength = data["hit_strength"]
                    self.backpack = Backpack(data['backpack']['coins'])
                    try:
                        self.location = (data["location"]["x"],
                                         data["location"]["y"])
                    except KeyError:
                        raise KeyError('Location should have keys: x and y')
                except KeyError:
                    raise KeyError('The dictionary should contain: health,'
                                   'hit_strength, backpack, location')
        except FileNotFoundError:
            raise FileNotFoundError('There is no such file')

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
        self.health = self._max_health

    def give_options(self, current_loc: object) -> list:
        moves_list = []
        if current_loc.is_monster():
            if current_loc.object.is_alive(0):
                moves_list = [move
                              for move in current_loc.moves['monster alive']]
            else:
                moves_list = [move
                              for move in current_loc.moves['monster dead']]
        else:
            moves_list = [move for move in current_loc.moves]
        return moves_list

    def decision(self, current_loc: object, world: object) -> None:
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

    def find_location(self, coords: list, location_list: list) -> object:
        loc = None
        for i in range(len(location_list)):
            if coords == location_list[i].coordinates:
                loc = location_list[i]
                return loc
        if loc is None:
            raise IndexError("Location with coordinates not found")

    def go_west(self, world: object) -> None:
        new_loc = self.location[0] - 1
        if new_loc < 0:
            self.location = (world.size - 1, self.location[1])
        else:
            self.location = (new_loc, self.location[1])
        curr_loc = self.find_location(self.location, world.location_list)
        print(curr_loc.description)

    def go_east(self, world: object) -> None:
        new_loc = self.location[0] + 1
        if new_loc > world.size - 1:
            self.location = (0, self.location[1])
        else:
            self.location = (new_loc, self.location[1])
        curr_loc = self.find_location(self.location, world.location_list)
        print(curr_loc.description)

    def go_north(self, world: object) -> None:
        new_loc = self.location[1] - 1
        if new_loc < 0:
            self.location = (self.location[0], world.size - 1)
        else:
            self.location = (self.location[0], new_loc)
        curr_loc = self.find_location(self.location, world.location_list)
        print(curr_loc.description)

    def go_south(self, world: object) -> None:
        new_loc = self.location[1] + 1
        if new_loc > world.size - 1:
            self.location = (self.location[0], 0)
        else:
            self.location = (self.location[0], new_loc)
        curr_loc = self.find_location(self.location, world.location_list)
        print(curr_loc.description)

    def curr_loc_description(curr_loc: object) -> None:
        clear_terminal()
        if curr_loc.is_monster():
            if curr_loc.object.is_alive(0):
                print(curr_loc.description['monster alive'])
            else:
                print(curr_loc.description['monster dead'])
        else:
            print(curr_loc.description)

    def fight_status(self, monster: object):
        print(f'Your hp is: {self.health}.'
              f'Monsters hp is: {monster.health}.')

    def fight_monster(self, monster: object) -> None:
        print(f'You are fighting monster level 1 named {monster.name}.')
        while monster.is_alive(0) and self.is_alive(0):
            self.fight_status(monster)
            monster.get_damage(self.attack())
        if self.is_alive(0):
            clear_terminal()
            print('You have defeated the monster. You are healed.')
            self.heal()

    def fight_monster_level_2(self, monster: object) -> None:
        print(f'You are fighting monster level 2 named {monster.name}.')
        while monster.is_alive(0) and self.is_alive(0):
            self.fight_status(monster)
            monster.get_damage(self.attack())
            self.get_damage(monster.attack_player())
        if self.is_alive(0):
            clear_terminal()
            print('You have defeated the monster. You are healed.')
            self.heal()

    def fight_monster_level_3(self, monster: object) -> None:
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

    def talk_to_trader(self, trader: object) -> None:
        trader.introduce()

    def receive_coins(self, coins: int) -> None:
        self.backpack.add_coins(coins)

    def help():
        pass
