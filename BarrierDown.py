from BasicSprite import *

class BarrierDown(BasicSprite):

    def __init__(self, row, col, width, sprite):
        BasicSprite.__init__(self, row, col, width)
        self.image = sprite
        self._layer = 2


