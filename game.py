"""Module with class to maintain game's system."""

import sys
import random
import time
import player
import board

__all__ = ['Game']


class Game:
    """ Class to maintain game's system."""

    def __init__(self):
        self.last_timebank = 0
        self.timebank = 0
        self.last_update = 0
        self.time_per_move = 0
        self.field_width = 0
        self.field_height = 0
        self.fields = None
        self.my_bot_id = 0
        self.other_bot_id = 0

        self.players = [player.Player(), player.Player()]

    def my_player(self):
        """Return my Player object."""
        return self.players[self.my_bot_id]

    def other_player(self):
        """ Return opponent Player object."""
        return self.players[self.other_bot_id]

    @staticmethod
    def order_turn(order):
        """Method to make move."""
        sys.stdout.write('%s\n' % order)
        sys.stdout.flush()

    @staticmethod
    def pass_turn():
        """Method to pass round."""
        sys.stdout.write('pass\n')
        sys.stdout.flush()

    def update(self, data):
        """
        Update game's parameters
        :param data: Data from game's API.
        """

        self.last_update = time.time()
        for line in data.split('\n'):
            line = line.rstrip()
            if line:
                line_elements = line.split(' ')
                if line_elements[0] == 'settings':
                    if line_elements[1] == 'timebank':
                        self.timebank = int(line_elements[2])
                    elif line_elements[1] == 'time_per_move':
                        self.time_per_move = int(line_elements[2])
                    elif line_elements[1] == 'your_botid':
                        self.my_bot_id = int(line_elements[2])
                        self.other_bot_id = 1 - self.my_bot_id
                    elif line_elements[1] == 'field_width':
                        self.field_width = int(line_elements[2])
                    elif line_elements[1] == 'field_height':
                        self.field_height = int(line_elements[2])

                elif line_elements[0] == 'update':
                    if line_elements[2] == 'field':
                        if not self.fields:
                            self.fields = board.Board(self.field_width, self.field_height)
                        self.fields.update(self.players, line_elements[3])

                elif line_elements[0] == 'action' and line_elements[1] == 'move':
                    self.last_timebank = int(line_elements[2])
                elif line_elements[0] == 'quit':
                    pass

    def run(self):
        """ Main loop of the game."""
        keep_playing = True
        setting_update_data = ''

        while keep_playing:
            current_line = sys.stdin.readline().rstrip('\r\n')
            setting_update_data += current_line + '\n'

            if current_line.lower().startswith('action move'):
                self.update(setting_update_data)
                self.do_turn()
                setting_update_data = ''

            elif current_line.lower().startswith('quit'):
                keep_playing = False

    def do_turn(self):
        """ Method to calculate side to which bot should go. """
        legal = self.fields.get_legal_moves(self.my_bot_id, self.players)
        if not legal:
            self.pass_turn()
        else:
            (_, chosen) = random.choice(legal)
            self.order_turn(chosen)
