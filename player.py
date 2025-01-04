import json
from monsters import Monster_level_1, Monster_level_2, Monster_level_3


class Player:
    def __init__(self, file_name):
        with open(file_name, 'r') as file:
            data = json.loads(file)
            self.health = data["health"],
            self.hit_strength = data["hit_strength"],
            # self.backpack = data['backpack']
            self.location = (data["location"]['x'], data["location"]['y'])

    def is_alive(self, damage) -> bool:
        return (self.health - damage > 0)

    def attack(self) -> None:
        return self.hit_strength

    def get_damage(self, damage) -> None:
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

    def decision(self, current_loc: object) -> None:
        decision = input()
        if decision == 'go east':
            pass
            # co??

    def find_location(self, coordinates: tuple, location_list: list) -> object:
        cnt = 0
        while coordinates != location_list[cnt].coordinates:
            loc = location_list[cnt]
            cnt += 1
        if coordinates != loc.coordinates:
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
        loc = self.find_location(coordinates, world.location_list)
        print(loc['description'])
        curr_loc = self.find_location()
        print(curr_loc.description)

    def go_north(self, world: object) -> None:
        new_loc = self.location[1] - 1
        if new_loc < 0:
            self.location[1] = world.size - 1
        else:
            self.location[1] = new_loc
        curr_loc = self.find_location()
        print(curr_loc.description)

    def curr_loc_description(curr_loc):
        if isinstance(curr_loc.object, (Monster_level_1,
                                        Monster_level_2,
                                        Monster_level_3)):
            print(curr_loc.description['monster alive'])
        else:
            pass
    # JAK spr czy monster żyje -> usuwnie z mapy?? bo są dwa descriptions

    def go_south(self, world: object) -> None:
        new_loc = self.location[1] + 1
        if new_loc > world.size - 1:
            self.location[1] = 0
        else:
            self.location[1] = new_loc
        curr_loc = self.find_location()
        self.curr_loc_description(curr_loc)

    def fight_monster(self, monster: object) -> None:
        print(f'You are fighting monster level {monster.level}.')
        while monster.is_alive(0) and self.is_alive(0):
            print(f'Your hp is: {self.health}. '
                  f'Monsters hp is: {monster.health}.')
            monster.get_damage(self.attack())
            pass
        if self.is_alive(0):
            print('You have defeated the monster')

    def fight_monster_level2(self, monster: object) -> None:
        pass

    def fight_monster_level3(self, monster: object) -> None:
        pass

    def talk_to_traider(self, traider: object) -> None:
        # if input() czy kupić klucz
        pass

    def help():
        pass
