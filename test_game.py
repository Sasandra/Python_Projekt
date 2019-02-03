"""Module for testing Game class"""
import unittest
from game import Game


class GameTest(unittest.TestCase):
    """Game Class Unit Test Class"""

    def setUp(self):
        self.game = Game()
