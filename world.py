from location import Location
import json


class World:
    def __init__(self, file_name):
        self.location_list = []
        self.data_list = []
        self._size = 0
        with open(f'{file_name}.json', "r") as file:
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

    @property
    def size(self) -> int:
        return self._size

    def create_map(self) -> None:
        cnt = 0
        for r in range(self.size):
            for c in range(self.size):
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
