from player import Player
from location import Location
from world import World
from monsters import Monster_level_1, Monster_level_2, Monster_level_3
import pytest
import unittest
import unittest.mock


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


def test_player_decision(monkeypatch):
    player = Player("test_player.json")
    world = World("test_world.json")
    monkeypatch.setattr("builtins.input", lambda _: "go east")
    player.decision(world.location_list[0], world)
    assert player.location == (1, 0)


def test_player_decision_not_in_list(monkeypatch):
    player = Player("test_player.json")
    world = World("test_world.json")
    monkeypatch.setattr("builtins.input", lambda _: "go west")
    player.decision(world.location_list[0], world)


class TestPlayer_go(unittest.TestCase):
    def setUp(self):
        self.world = World("test_world.json")
        self.player = Player("test_player.json")

    def test_go_west(self):
        with unittest.mock.patch('player.Player.decision', return_value=None):
            self.player.go_west(self.world)
            self.assertEqual(self.player.location, (2, 0))
            self.player.go_west(self.world)
            self.assertEqual(self.player.location, (1, 0))
            self.player.go_west(self.world)
            self.assertEqual(self.player.location, (0, 0))

    def test_go_east(self):
        with unittest.mock.patch('player.Player.decision', return_value=None):
            self.player.go_east(self.world)
            self.assertEqual(self.player.location, (1, 0))
            self.player.go_east(self.world)
            self.assertEqual(self.player.location, (2, 0))
            self.player.go_east(self.world)
            self.assertEqual(self.player.location, (0, 0))

    def test_go_north(self):
        with unittest.mock.patch('player.Player.decision', return_value=None):
            self.player.go_north(self.world)
            self.assertEqual(self.player.location, (0, 2))
            self.player.go_north(self.world)
            self.assertEqual(self.player.location, (0, 1))
            self.player.go_north(self.world)
            self.assertEqual(self.player.location, (0, 0))

    def test_go_south(self):
        with unittest.mock.patch('player.Player.decision', return_value=None):
            self.player.go_south(self.world)
            self.assertEqual(self.player.location, (0, 1))
            self.player.go_south(self.world)
            self.assertEqual(self.player.location, (0, 2))
            self.player.go_south(self.world)
            self.assertEqual(self.player.location, (0, 0))


def test_player_fight_monster_level_3():
    player = Player("test_player.json")
    monster_data = {
        'level': 3,
        'health': 2,
        "name": "Thor",
        'description': 'This is Thor',
        'coins': 50,
        'hit strength': 10
    }
    monster = Monster_level_3(monster_data)
    player.fight_monster_level_3(monster)
    assert monster.health == 0
    assert player.backpack.coins == 60


def test_player_fight_monster_level_2():
    player = Player("test_player.json")
    monster_data = {
        'level': 2,
        'health': 2,
        "name": "Thor",
        'description': 'This is Thor',
        'coins': 50,
        'hit strength': 10
    }
    monster = Monster_level_2(monster_data)
    player.fight_monster_level_2(monster)
    assert monster.health == 0
    assert player.backpack.coins == 60


def test_player_fight_monster():
    player = Player("test_player.json")
    monster_data = {
        'level': 1,
        'health': 2,
        "name": "Thor",
        'description': 'This is Thor',
        'coins': 50,
        'hit strength': 10
    }
    monster = Monster_level_1(monster_data)
    player.fight_monster(monster)
    assert monster.health == 0
    assert player.backpack.coins == 60


def test_curr_loc_description():
    world = World("test_world.json")
    player = Player("test_player.json")
    player.curr_loc_description(world.location_list[0])
