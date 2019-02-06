"""Module for testing Board Class"""
import unittest
from board import Board
from player import Player


class BoardTest(unittest.TestCase):
    """Board Class Unit Test Class"""

    def setUp(self):
        self.board = Board(4, 4)
        new_board = '.,.,.,.,' \
                    '.,1,.,.,' \
                    '.,.,.,.,' \
                    '.,.,0,.'

        self.players = [Player(), Player()]

        self.board.update(new_board)

    def test_boundary_condition(self):
        """Return True if filed (2,2) is in board's range and filed (5,5) isn't"""
        self.assertEqual(self.board.boundary_condition(5, 5), False)
        self.assertEqual(self.board.boundary_condition(2, 2), True)

    def test_check_if_filed_free(self):
        """Return True if field (2,2) is empty and field (5,5) isn't."""
        self.assertEqual(self.board.check_if_filed_free(2, 2, 0), True)
        self.assertEqual(self.board.check_if_filed_free(3, 2, 0), False)

    def test_is_legal_move(self):
        """Return True if move to (2,2) is a legal move and to (3,2) isn't."""
        self.assertEqual(self.board.is_legal_move(2, 2, 1), True)
        self.assertEqual(self.board.is_legal_move(3, 2, 1), False)

    def test_get_legal_moves(self):
        """Return True when legal moves are calculated correctly."""
        moves = set(self.board.get_legal_moves(1))
        test_moves = set([((0, 1), "up"), ((1, 2), "right"), ((2, 1), "down"), ((1, 0), "left")])
        self.assertEqual(moves, test_moves)
