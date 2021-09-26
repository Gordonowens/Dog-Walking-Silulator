from BasicSprite import *

class WaterSprite(BasicSprite):

    def __init__(self, row, col, width, spriteSheet):
        BasicSprite.__init__(self, row, col, width)

        self.image = self.createSprite(spriteSheet, 51, 17, 16, 16, WHITE)
        self._layer = 2