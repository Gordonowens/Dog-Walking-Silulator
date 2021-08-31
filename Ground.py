from BasicSprite import *

class Ground(BasicSprite):

    def __init__(self, row, col, width, total_rows, spriteSheet):
        BasicSprite.__init__(self, row, col, width, total_rows, spriteSheet)
        self._layer = 1
        self.image = self.createSprite(spriteSheet, 64, 352, width, width)
        self.color = WHITE
