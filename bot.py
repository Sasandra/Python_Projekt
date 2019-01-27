import random

__all__ = ['Bot']


class Bot:
    def __init__(self):
        self.game = None

    def set_up(self, game):
        self.game = game

    def do_turn(self):
        legal = self.game.fields.get_legal_moves(self.game.my_botid, self.game.players)
        if len(legal) == 0:
            self.game.pass_turn()
        else:
            (_, chosen) = random.choice(legal)
            self.game.order_turn(chosen)
