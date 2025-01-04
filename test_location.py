from location import Location
from monsters import Monster_level_1
from items import Trader


def test_create_location_no_object():
    loc = Location(1, 1, "swamp", "this is swamp", ["go west"])
    assert loc.coordinates == (1, 1)
    assert loc.name == "swamp"
    assert loc.description == "this is swamp"
    assert loc.moves == ["go west"]
    if loc.object is None:
        assert True


def test_create_location_with_monster():
    object = {"monster": {
          "name": "Thor",
          "health": 200,
          "level": 1,
          "coins": 10,
          "description": "This is Thor",
          "hit_strength": 20
        }}
    loc = Location(1, 1, "swamp", "this is swamp", ["go west"], object)
    assert isinstance(loc.object, Monster_level_1)


def test_create_location_with_trader():
    object = {"trader": {
          "name": "Thor"
        }}
    loc = Location(1, 1, "swamp", "this is swamp", ["go west"], object)
    assert isinstance(loc.object, Trader)
