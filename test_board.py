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

        self.board.update(self.players, new_board)

    def test_convert_coordinates_to_index(self):
        """ Return True if (1,1) elem in 4x4 matrix is 5 in 16x1 vector"""
        index = self.board.convert_coordinates_to_index(1, 1)
        self.assertEqual(index, 5)

    def test_convert_index_to_coordinates(self):
        """ Return True if 10 elem in 16x1 vector is (2,2) elem in 4x4 matrix"""
        row, col = self.board.convert_index_to_coordinates(10)
        self.assertEqual((row, col), (2, 2))

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
        moves = set(self.board.get_legal_moves(1, self.players))
        test_moves = {[((0, 1), "up"), ((1, 2), "right"), ((2, 1), "down"), ((1, 0), "left")]}
        self.assertEqual(moves, test_moves)
