
class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.fields = [['.' for col in range(self.width)] for row in range(self.height)]

    def update(self, players, new_board):
        pass