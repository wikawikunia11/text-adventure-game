from player import Player
from location import Location
from world import World
import pytest


def test_file():
    Player("player.json")


def test_create_player():
    player = Player("test_player.json")
    assert player.health == 100
    assert player.backpack.coins == 10
    assert player.location == (0, 0)
    assert player.hit_strength == 20


def test_create_player_wrong_file():
    with pytest.raises(FileNotFoundError):
        Player("xxx.json")


def test_player_get_damage():
    player = Player("test_player.json")
    player.get_damage(10)
    assert player.health == 90
    assert player._max_health == 100


def test_player_heal():
    player = Player("test_player.json")
    player.get_damage(20)
    player.heal()
    assert player.health == 100


def test_player_give_options_monster_alive():
    player = Player("test_player.json")
    object = {"monster": {
          "name": "Thor",
          "health": 200,
          "level": 1,
          "coins": 10,
          "description": "This is Thor",
          "hit_strength": 20
        }}
    loc = Location(1, 1, "swamp", "this is swamp",
                   {'monster alive': ["go west", "go east"],
                    'Monster dead': ['go east']}, object)
    assert player.give_options(loc) == ["go west", "go east"]


def test_player_give_options_monster_dead():
    player = Player("test_player.json")
    object = {"monster": {
          "name": "Thor",
          "health": 1,
          "level": 1,
          "coins": 10,
          "description": "This is Thor",
          "hit_strength": 20
        }}
    loc = Location(1, 1, "swamp", "this is swamp",
                   {'monster alive': ["go west", "go east"],
                    'monster dead': ['go east']}, object)
    loc.object.get_damage(1)
    assert player.give_options(loc) == ["go east"]


def test_player_give_options_no_monster():
    player = Player("test_player.json")
    loc = Location(1, 1, "swamp", "this is swamp", ["go west", "go east"])
    assert player.give_options(loc) == ["go west", "go east"]


def test_player_decision():
    # jak??
    pass


def test_player_go_east():
    player = Player("test_player.json")
    world = World("test_world.json")
    player.go_east(world)
    assert player.location == (1, 0)
    player.go_east(world)
    assert player.location == (2, 0)
    player.go_east(world)
    assert player.location == (0, 0)


def test_player_go_west():
    player = Player("test_player.json")
    world = World("test_world.json")
    player.go_west(world)
    assert player.location == (2, 0)
    player.go_west(world)
    assert player.location == (1, 0)
    player.go_west(world)
    assert player.location == (0, 0)


def test_player_go_north():
    player = Player("test_player.json")
    world = World("test_world.json")
    player.go_north(world)
    assert player.location == (0, 2)
    player.go_north(world)
    assert player.location == (0, 1)
    player.go_north(world)
    assert player.location == (0, 0)


def test_player_go_south():
    player = Player("test_player.json")
    world = World("test_world.json")
    player.go_south(world)
    assert player.location == (0, 1)
    player.go_south(world)
    assert player.location == (0, 2)
    player.go_south(world)
    assert player.location == (0, 0)
