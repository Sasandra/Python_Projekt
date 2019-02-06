""" Module with class to represent game's board."""
import numpy as np

DIRS = [
    ((-1, 0), "up"),
    ((0, 1), "right"),
    ((1, 0), "down"),
    ((0, -1), "left")
]


class Board:
    """ Class to represent board and operations on it."""

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.fields = ''

    def update(self, new_board):
        """
        Update board and players' positions.
        :param new_board: new board's representation from game API
        """

        self.fields = np.array(new_board.split(',')).reshape((self.width, self.height))

    def get_legal_moves(self, my_id):
        """
        Find all possible moves from my bot current position.
        :param my_id: my bot's id (int)
        :return: list of possible moves: ((new_row, new_col), order)
        """

        moves = []
        my_player_row, my_player_col = np.where(self.fields == str(my_id))

        for (tmp_row, tmp_col), order in DIRS:
            row = my_player_row[0] + tmp_row
            col = my_player_col[0] + tmp_col

            if self.is_legal_move(row, col, my_id):
                moves.append(((row, col), order))

        return moves

    def is_legal_move(self, row, col, my_bot_id):
        """
        Check if move on given position is legal
        :param row: y coordinate of board
        :param col: x coordinate of board
        :param my_bot_id: my bot's id (int)
        :return: True if move is allowed, False otherwise
        """

        second_id = 1 - my_bot_id
        boundary_cond = self.boundary_condition(row, col)

        if boundary_cond:
            return self.check_if_filed_free(row, col, second_id)

        return False

    def boundary_condition(self, row, col):
        """
        Check if given indexes are on in board's range.
        :param row: y coordinate of board
        :param col: x coordinate of board
        :return: True if pair [col, row] is in board's range, False otherwise
        """

        return 0 <= row < self.height and 0 <= col < self.width

    def check_if_filed_free(self, row, col, second_id):
        """
        Check if given filed on board is empty
        :param row: y coordinate of board
        :param col: x coordinate of board
        :param second_id: enemy bot's id
        :return: True if filed if free, False otherwise
        """

        wall_condition = self.fields[row][col] != 'x'
        enemy_cond = self.fields[row][col] != str(second_id)
        return wall_condition and enemy_cond
