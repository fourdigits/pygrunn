import unittest
from utils import add


class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(4, 2), 6)
