from src.models.location import Location
from src.models.monsters import Monster_level_1
from src.models.items import Trader


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
    assert loc.is_monster()
    assert not loc.is_trader()


def test_create_location_with_trader():
    object = {"trader": {
          "name": "Thor",
          "item": {
            "name": "key",
            "description": "this is key",
            "price": 20
          }
        }}
    loc = Location(1, 1, "swamp", "this is swamp", ["go west"], object)
    assert isinstance(loc.object, Trader)
    assert not loc.is_monster()
    assert loc.is_trader()
