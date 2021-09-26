from BasicSprite import *

class TreeTop(BasicSprite):

    def __init__(self, row, col, width, sprite):
        BasicSprite.__init__(self, row, col, width)
        self._layer = 5
        self.image = sprite