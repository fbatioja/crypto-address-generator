import unittest
from unittest import TestCase

from utils.generate_address import generate_address


class TestingGenerateAddress(TestCase):
    def test_address_generation(self):
        address_btc = generate_address('BTC', '33353816f44447ede1a74fc278b9b4bda415218b86ffe8166b0cba65c1ee5510')
        address_etc = generate_address('ETC', '33353816f44447ede1a74fc278b9b4bda415218b86ffe8166b0cba65c1ee5510')
        address_none = generate_address('DOLLAR', '33353816f44447ede1a74fc278b9b4bda415218b86ffe8166b0cba65c1ee5510')
        
        self.assertIsNotNone(address_btc)
        self.assertIsNotNone(address_etc)
        self.assertIsNone(address_none)
        self.assertIsInstance(address_btc, str)
        self.assertIsInstance(address_etc, str)


if __name__ == '__main__':
    unittest.main()
