import sys
import time
import player
import board

__all__ = ['Game']

class Game:
    def __init__(self):
        self.last_timebank = 0
        self.last_update = 0
        self.fields = None
        self.players = [player.Player(), player.Player()]

    def my_player(self):
        return self.players[self.my_botid]

    def other_player(self):
        return self.players[self.other_botid]

    def time_remaining(self):
        return self.last_timebank - int(1000 * (time.clock() - self.last_update))

    def order_turn(self, order):
        """issue an order, noting that (col, row) is the expected output
        however internally, (row, col) is used."""
        sys.stdout.write('%s\n' % order)
        sys.stdout.flush()

    def pass_turn(self):
        sys.stdout.write('pass\n')
        sys.stdout.flush()

    def update(self, data):
        self.last_update = time.time()
        for line in data.split('\n'):
            line = line.rstrip()
            if len(line) > 0:
                line_elements = line.split(' ')
                if line_elements[0] == 'settings':
                    if line_elements[1] == 'timebank':
                        self.timebank = int(line_elements[2])
                    elif line_elements[1] == 'time_per_move':
                        self.time_per_move = int(line_elements[2])
                    elif line_elements[1] == 'player_names':
                        self.player_names = line_elements[2].split(',')
                    elif line_elements[1] == 'your_bot':
                        self.my_bot = line_elements[2]
                    elif line_elements[1] == 'your_botid':
                        self.my_botid = int(line_elements[2])
                        self.other_botid = 1 - self.my_botid
                    elif line_elements[1] == 'field_width':
                        self.field_width = int(line_elements[2])
                    elif line_elements[1] == 'field_height':
                        self.field_height = int(line_elements[2])

                elif line_elements[0] == 'update':
                    if line_elements[2] == 'round':
                        self.round = int(line_elements[3])
                    elif line_elements[2] == 'field':
                        if not self.fields:
                            self.fields = board.Board(self.field_width, self.field_height)
                        self.fields.update(self.players, line_elements[3])
                elif line_elements[0] == 'action' and line_elements[1] == 'move':
                    self.last_timebank = int(line_elements[2])
                elif line_elements[0] == 'quit':
                    pass

    def run(self, bot):
        keep_playing = True
        setting_update_data = ''

        while keep_playing:
            current_line = sys.stdin.readline().rstrip('\r\n')
            setting_update_data += current_line + '\n'

            if current_line.lower().startswith('action move'):
                self.update(setting_update_data)
                if not bot.game:
                    bot.set_up(self)
                bot.do_turn()
                setting_update_data = ''

            elif current_line.lower().startswith('quit'):
                keep_playing = False
