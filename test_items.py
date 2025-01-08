from items import Trader, Backpack
from player import Player
import io
import unittest
import unittest.mock
import pytest


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


def test_create_trader_keyerror_item():
    trader_data = {
        'name': 'Andreas',
        }
    with pytest.raises(KeyError):
        Trader(trader_data)


def test_create_trader_keyerror_name():
    trader_data = {
        'item': {}
        }
    with pytest.raises(KeyError):
        Trader(trader_data)


def test_sell_key(monkeypatch):
    player = Player('test_player.json')
    trader_data = {
        'name': 'Andreas',
        'item': {
            "name": "key",
            "description": "This is a key.",
            "price": 10
        }
    }
    trader = Trader(trader_data)
    assert not player.backpack.is_key
    monkeypatch.setattr('builtins.input', lambda _: None)
    trader.sell_key(player)
    assert player.backpack.is_key
    assert player.backpack.coins == 0
    assert trader.item == {}


class TestTrader(unittest.TestCase):
    def test_trader_introduce_offer(self):
        player = Player('test_player.json')
        trader_data = {
            'name': 'Andreas',
            'item': {
                "name": "key",
                "description": "This is a key.",
                "price": 10
            }
        }
        trader = Trader(trader_data)
        with unittest.mock.patch(
            'sys.stdout', new_callable=io.StringIO
        ) as mock_stdout:
            trader.introduce_offer()
            self.assertEqual(
                mock_stdout.getvalue(), ('1. key : This is a key.\n'
                                         '\tThis item costs 10 coins.\n\n')
            )
        with (
            unittest.mock.patch('sys.stdout',
                                new_callable=io.StringIO)
            as mock_stdout,
            unittest.mock.patch('builtins.input',
                                return_value='ok')
            as mock_input
        ):
            trader.sell_key(player)
            self.assertEqual(
                mock_stdout.getvalue(),
                "You have the key! The game is complete!\n"
            )
            self.assertTrue(player.backpack.is_key)
            mock_input.assert_called_once()
        with unittest.mock.patch(
            'sys.stdout', new_callable=io.StringIO
        ) as mock_stdout:
            trader.introduce_offer()
            self.assertEqual(
                mock_stdout.getvalue(), ('I dont have anything to offer.\n\n')
            )


def test_create_backpack():
    backpack = Backpack(10)
    assert not backpack.is_key
    assert backpack.coins == 10


def test_backpack_add_coins():
    backpack = Backpack(10)
    assert backpack.coins == 10
    backpack.add_coins(10)
    assert backpack.coins == 20


def test_backpack_spend_coins():
    backpack = Backpack(10)
    assert backpack.coins == 10
    backpack.spend_coins(10)
    assert backpack.coins == 0


class TestBackpack(unittest.TestCase):
    def test_backpack_add_key(self):
        backpack = Backpack(10)
        assert not backpack.is_key
        with (
            unittest.mock.patch('sys.stdout',
                                new_callable=io.StringIO)
            as mock_stdout,
            unittest.mock.patch('builtins.input',
                                return_value='ok')
            as mock_input
        ):
            backpack.add_key()
            self.assertEqual(
                mock_stdout.getvalue(),
                "You have the key! The game is complete!\n"
            )
            self.assertTrue(backpack.is_key)
            mock_input.assert_called_once()
