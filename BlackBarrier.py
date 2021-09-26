from BasicSprite import *


class BlackBarrier(BasicSprite):

    def __init__(self, row, col, width):
        BasicSprite.__init__(self, row, col, width)
        self._layer = 2
        self.color = BLACK
        self.state = 'barrier'
