from src.models.world import World
from src.models.location import Location
import pytest

world_dir = "src/test/test_world.json"

def test_creating_world():
    world = World(world_dir)
    assert world.size == 3
    assert len(world.data_list) == 9
    assert world.data_list[0]['name'] == 'forest'
    assert world.data_list[0]['description'] == 'This is a forest'
    assert world.data_list[0]['moves'] == ['go east']


def test_file():
    World(world_dir)


def test_create_map():
    world = World(world_dir)
    assert world.size == 3
    assert len(world.location_list) == 9
    assert isinstance(world.location_list[0], Location)


def test_wrong_file_name():
    with pytest.raises(FileNotFoundError):
        World("xxx.json")
