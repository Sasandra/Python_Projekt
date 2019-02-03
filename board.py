""" Module with class to represent game's board."""
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

    def update(self, players, new_board):
        """
        Update board and players' positions.
        :param players: list of Players objects
        :param new_board: new board's representation from game API
        """

        new_fields = new_board.split(',')
        row1, col1 = self.convert_index_to_coordinates(new_fields.index('1'))
        row0, col0 = self.convert_index_to_coordinates(new_fields.index('0'))

        players[0].row = row0
        players[0].col = col0

        players[1].row = row1
        players[1].col = col1

        self.fields = new_fields

    def get_legal_moves(self, my_id, players):
        """
        Find all possible moves from my bot current position.
        :param my_id: my bot's id (int)
        :param players: list of Players objects
        :return: list of possible moves: ((new_row, new_col), order)
        """

        my_player = players[my_id]
        moves = []

        for (tmp_row, tmp_col), order in DIRS:
            row = my_player.row + tmp_row
            col = my_player.col + tmp_col

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
        free_field_cond = self.check_if_filed_free(row, col, second_id)

        return boundary_cond and free_field_cond

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

        index = self.convert_coordinates_to_index(row, col)
        wall_condition = self.fields[index] != 'x'
        enemy_cond = self.fields[index] != str(second_id)
        return wall_condition and enemy_cond

    def convert_index_to_coordinates(self, index):
        """
        Convert index in vector to pair of indexes in 2D matrix
        :param index: index in vector
        :return: pair (row, col) -> coordinates in 2D matrix
        """

        row = index // self.width
        col = index % self.width

        return row, col

    def convert_coordinates_to_index(self, row, col):
        """
        Convert indexes in 2D matrix into index in vector.
        :param row: y coordinate of board
        :param col: x coordinate of board
        :return: index of vector
        """

        index = row * self.width + col

        return index
