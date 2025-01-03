from world import World
import pytest


def test_creating_world():
    world = World("test_world.json")
    assert world.size == 2
    assert len(world.data_list) == 4
    assert world.data_list[0]['name'] == 'forest'
    assert world.data_list[0]['description'] == 'This is a forest'
    assert world.data_list[0]['moves'] == ['go east']


def test_create_map():
    world = World("test_world.json")
    assert world.size == 2
    assert len(world.location_list) == 4
    loc = world.location_list[0]
    assert loc.name == 'forest'
    assert loc.description == 'This is a forest'


def test_wrong_file_name():
    with pytest.raises(FileNotFoundError):
        World("xxx.json")

