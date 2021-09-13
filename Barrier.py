from BasicSprite import *


class Barrier(BasicSprite):

    def __init__(self, row, col, width, sprite):
        BasicSprite.__init__(self, row, col, width)
        self.image = sprite
        self._layer = 2
        #960, 448
        #


        self.color = BLACK
        self.state = 'barrier'
