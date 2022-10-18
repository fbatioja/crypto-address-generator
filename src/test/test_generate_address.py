import unittest
from unittest import TestCase

from utils.generate_address import generate_address


class TestingGenerateAddress(TestCase):
    def test_address_generation(self):
        address = generate_address('BTC', '33353816f44447ede1a74fc278b9b4bda415218b86ffe8166b0cba65c1ee5510')
        
        self.assertIsNotNone(address)
        self.assertIsInstance(address, str)


if __name__ == '__main__':
    unittest.main()
