"""Module with class to maintain Players positions on board."""


class Player:
    """Class to represent players position"""

    def __init__(self):
        self.col = 0
        self.row = 0

    def set_row(self, new_row):
        """
        Set new row's value
        :param new_row: new value for row attribute
        """

        self.row = new_row

    def set_col(self, new_col):
        """
        Set new col's value.
        :param new_col: new value for col attribute
        """

        self.col = new_col
