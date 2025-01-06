from items import Trader


def test_create_trader():
    trader_data = {
        'name': 'Andreas',
        'item': {
            "name": "key",
            "description": "This is a key.",
            "price": 20
        }
        }
    trader = Trader(trader_data)
    assert trader.type == 'trader'
    assert trader.name == 'Andreas'
    assert trader.item['name'] == 'key'
