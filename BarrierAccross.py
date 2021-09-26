from BasicSprite import *

class BarrierAccross(BasicSprite):

    def __init__(self, row, col, width, sprite):
        BasicSprite.__init__(self, row, col, width)

        self.image = sprite
        self.layer = 2