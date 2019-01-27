DIRS = [
    ((-1, 0), "up"),
    ((0, 1), "right"),
    ((1, 0), "down"),
    ((0, -1), "left")
]


class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.fields = [['.' for col in range(self.width)] for row in range(self.height)]

    def update(self, players, new_board):
        # range co 16?
        new_fields = new_board.split(',')
        row = 0
        col = 0
        for filed in new_fields:
            if col >= self.width:
                col = 0
                row += 1
            self.fields[row][col] = filed
            self.update_players(players, row, col, filed)
            col += 1

    def update_players(self, players, row, col, filed):
        if filed == '0':
            players[0].row = row
            players[0].col = col

        elif filed == '1':
            players[1].row = row
            players[1].col = col

    def get_legal_moves(self, my_id, players):
        my_player = players[my_id]
        moves = []

        for (tmp_row, tmp_col), order in DIRS:
            row = my_player.row + tmp_row
            col = my_player.col + tmp_col

            if self.is_legal_move(row, col, my_id):
                moves.append(((row, col), order))

        return moves

    def is_legal_move(self, row, col, id):
        second_id = 1 - id
        boundary_cond = self.boundary_condition(row, col)
        free_field_cond = self.check_if_filed_free(row, col, second_id)

        return boundary_cond and free_field_cond

    def boundary_condition(self, row, col):
        return 0 <= row < self.height and 0 <= col < self.width

    def check_if_filed_free(self, row, col, second_id):
        wall_condition = self.fields[row][col] != 'x'
        enemy_cond = self.fields[row][col] != str(second_id)
        return wall_condition and enemy_cond
