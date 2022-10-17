import unittest
from unittest import TestCase

from utils.generate_address import generate_address


class TestingGenerateAddress(TestCase):
    def test_address_generation(self):
        address = generate_address('BTC')
        
        self.assertIsNotNone(address)
        self.assertIsInstance(address, str)


if __name__ == '__main__':
    unittest.main()
