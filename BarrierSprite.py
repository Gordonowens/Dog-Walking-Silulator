from BasicSprite import *

class BarrierSprite(BasicSprite):

    def __init__(self, row, col, width, spriteSheet):
        BasicSprite.__init__(self, row, col, width)
        self.image = self.createSprite(spriteSheet, 960, 448, 30, 30)
        self._layer = 1