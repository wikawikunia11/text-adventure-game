from world import World


def test_creating_world():
    world = World('test_world')
    assert len(world.data_list) == 9
    assert world.data_list[0]['name'] == 'forest'
    assert world.size == 3


def test_create_map():
    world = World('test_world')
    assert len(world.location_list) == 9