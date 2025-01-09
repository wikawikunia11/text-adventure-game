from monsters import Monster_level_1, Monster_level_2, Monster_level_3
import pytest


def test_create_monster_level_1():
    monster_data = {
        'level': 1,
        'health': 200,
        "name": "Thor",
        'coins': 10
    }
    monster = Monster_level_1(monster_data)
    assert isinstance(monster, Monster_level_1)
    assert monster.type == "monster"
    assert monster.name == 'Thor'
    assert monster.health == 200
    assert monster.level == 1
    assert monster.coins == 10


def test_create_monster_level_1_invalid_health():
    monster_data = {
        'level': 1,
        'health': -10,
        "name": "Thor",
        'coins': 10
    }
    with pytest.raises(ValueError):
        Monster_level_1(monster_data)


def test_invalid_keys():
    monster_data = {
        'level': 1,
        "name": "Thor",
        'coins': 10
    }
    with pytest.raises(KeyError):
        Monster_level_1(monster_data)
    with pytest.raises(KeyError):
        Monster_level_2(monster_data)
    with pytest.raises(KeyError):
        Monster_level_3(monster_data)


def test_create_monster_level_2():
    monster_data = {
        'level': 2,
        'health': 200,
        "name": "Thor",
        'coins': 30,
        'hit strength': 20
    }
    monster = Monster_level_2(monster_data)
    assert isinstance(monster, Monster_level_2)
    assert monster.level == 2
    assert monster.hit_strength == 20


def test_create_monster_level_3():
    monster_data = {
        'level': 3,
        'health': 200,
        "name": "Thor",
        'coins': 50,
        'hit strength': 20
    }
    monster = Monster_level_3(monster_data)
    assert isinstance(monster, Monster_level_3)
    assert monster.level == 3


def test_monster_get_damage():
    monster_data = {
        'level': 1,
        'health': 200,
        "name": "Thor",
        'coins': 10
    }
    monster = Monster_level_1(monster_data)
    monster.get_damage(30)
    assert monster.health == 170
    assert monster.is_alive(30)
    monster.get_damage(300)
    assert monster.health == 0


def test_monster_get_damage_invalid_damage():
    monster_data = {
        'level': 1,
        'health': 200,
        "name": "Thor",
        'coins': 10
    }
    monster = Monster_level_1(monster_data)
    with pytest.raises(ValueError):
        monster.get_damage(-10)


def test_monster_attack_player(monkeypatch):
    def return_four(x, y):
        return 4
    monster_data = {
        'level': 2,
        'health': 200,
        "name": "Thor",
        'coins': 10,
        'hit strength': 20
    }
    monster = Monster_level_2(monster_data)
    monkeypatch.setattr('monsters.randint', return_four)
    hit = monster.attack_player()
    assert hit == 20


def test_monster_heal(monkeypatch):
    def return_four(x, y):
        return 4
    monster_data = {
        'level': 3,
        'health': 200,
        "name": "Thor",
        'coins': 50,
        'hit strength': 20
    }
    monster = Monster_level_3(monster_data)
    monkeypatch.setattr("monsters.randint", return_four)
    monster.get_damage(30)
    assert monster.health == 170
    monster.heal(10)
    assert monster.health == 180


def test_monster_heal_invalid_damage(monkeypatch):
    monster_data = {
        'level': 3,
        'health': 200,
        "name": "Thor",
        'coins': 10,
        'hit strength': 20
    }
    monster = Monster_level_3(monster_data)
    with pytest.raises(ValueError):
        monster.heal(-10)


def test_monster_attack_player_super_hit(monkeypatch):
    def return_four(x, y):
        return 4
    monster_data = {
        'level': 3,
        'health': 200,
        "name": "Thor",
        'coins': 50,
        'hit strength': 20
    }
    monster = Monster_level_3(monster_data)
    monkeypatch.setattr("monsters.randint", return_four)
    hit = monster.attack_player()
    assert hit == 40
