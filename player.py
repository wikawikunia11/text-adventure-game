import json


class Player:
    def __init__(self):
        with open("player.json", 'r') as file:
            data = json.loads(file)
            self.health = data["health"],
            self.hit_strength = data["hit_strength"],
            # backpack
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
        # tu zrobić


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

    def go_south(self, world: object) -> None:
        new_loc = self.location[1] + 1
        if new_loc > world.size - 1:
            self.location[1] = 0
        else:
            self.location[1] = new_loc
        curr_loc = self.find_location()
        print(curr_loc.description)

    def fight_monster(self, monster: object) -> None:
        while monster.is_alive() and self.is_alive():
            # automatyczna walka
            # wypisywać stan hp obu
            # kto zwycieżył -> dwa ify przypadki
            pass

    def fight_monster_level2(self, monster: object) -> None:
        pass

    def fight_monster_level3(self, monster: object) -> None:
        pass

    def talk_to_traider(self, traider: object) -> None:
        # if input() czy kupujemy klucz
        pass

    def help():
        pass
