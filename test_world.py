from world import World


def test_creating_world():
    world = World("test_world.json")
    assert world.size == 2
    assert len(world.data_list) == 4
    assert world.data_list[0]['name'] == 'forest'
    assert world.data_list[0]['description'] == 'This is a forest'
    assert world.data_list[0]['moves'] == ['go east']