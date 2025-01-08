from location import Location
import json


class World:
    def __init__(self, file_name: str) -> None:
        self.location_list = []
        self.data_list = []
        self._size = 0
        try:
            with open(file_name, "r") as file:
                data = json.load(file)
            locations_data = data['locations']
            self._size = int(data['world size'])
            for location in locations_data:
                self.data_list.append(
                    {
                        'name': location['name'],
                        'description': location['description'],
                        'object': location['object'],
                        'moves': location['moves']
                    }
                )
            self.create_map()
        except FileNotFoundError:
            raise FileNotFoundError("This file does not exist")

    @property
    def size(self) -> int:
        return self._size

    def create_map(self) -> None:
        cnt = 0
        for c in range(self.size):
            for r in range(self.size):
                name = self.data_list[cnt]['name']
                description = self.data_list[cnt]['description']
                moves = self.data_list[cnt]['moves']
                if self.data_list[cnt]['object'] != "None":
                    object = self.data_list[cnt]['object']
                    loc = Location(r, c, name, description,  moves, object)
                else:
                    loc = Location(r, c, name, description, moves)
                self.location_list.append(loc)
                cnt += 1

    def save_world(self):
        cnt = 0
        for location in self.location_list:
            if location.is_monster() and location.object.health == 0:
                self.data_list[cnt]['object']['monster']['health'] = 0
            cnt += 1
        with open('saved_game.json', 'w') as file:
            data_to_save = {}
            data_to_save['world size'] = self.size
            data_to_save['locations'] = self.data_list
            json.dump(data_to_save, file, indent=4)
