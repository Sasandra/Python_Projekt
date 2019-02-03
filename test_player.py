"""Module for testing Player class"""
import unittest
from player import Player


class PlayerTest(unittest.TestCase):
    """Player Class Unit Test Class"""

    def setUp(self):
        self.player = Player()

    def test_increase_row(self):
        """Return True if Player'y coordinate is 2"""
        self.player.row += 2
        self.assertEqual(self.player.row, 2)

    def test_increase_col(self):
        """Return True if Player'x coordinate is 3"""
        self.player.col += 3
        self.assertEqual(self.player.col, 3)

    def test_increase_both(self):
        """Return True if Player's coordinates is (6, 4)"""
        self.player.col += 3
        self.player.row += 2

        self.assertEqual(self.player.col, 3)
        self.assertEqual(self.player.row, 2)

    def test_decrease_row(self):
        """Return True if Player'y coordinate is -2"""
        self.player.row -= 2
        self.assertEqual(self.player.row, -2)

    def test_decrease_col(self):
        """Return True if Player'x coordinate is -3"""
        self.player.col -= 3
        self.assertEqual(self.player.col, -3)

    def test_decrease_both(self):
        """Return True if Player's coordinates is (-2, -3)"""
        self.player.col -= 3
        self.player.row -= 2

        self.assertEqual(self.player.col, -3)
        self.assertEqual(self.player.row, -2)
