from monsters import Monster_level_1, Monster_level_2, Monster_level_3
from items import Trader


class Location:
    def __init__(self, x, y, name, description, moves, object=None) -> None:
        self._coordinates = (x, y)
        self._name = name
        self._description = description
        self._object = object
        self._moves = moves
        if self._object is not None:
            self.def_object()

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description

    @property
    def coordinates(self) -> tuple:
        return self._coordinates

    @property
    def moves(self) -> list:
        return self._moves

    @property
    def object(self) -> object:
        return self._object

    def def_object(self) -> None:
        if "monster" in self._object.keys():
            level = self._object['monster']['level']
            if level == 1:
                monster = Monster_level_1(self._object['monster'])
            if level == 2:
                monster = Monster_level_2(self._object['monster'])
            if level == 3:
                monster = Monster_level_3(self._object['monster'])
            self._object = monster
        elif "trader" in self._object.keys():
            self._object = Trader(self._object['trader'])

    def is_monster(self) -> bool:
        return isinstance(self.object, (Monster_level_1,
                                        Monster_level_2,
                                        Monster_level_3))

    def is_trader(self) -> bool:
        return isinstance(self.object, Trader)
