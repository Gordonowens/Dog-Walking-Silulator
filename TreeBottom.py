from Node import *
from Barrier import *


class TreeBottom(Barrier):

    def __init__(self, row, col, width, total_rows, spriteSheet):
        Barrier.__init__(self, row, col, width, total_rows, spriteSheet)
        self._layer = 2
        self.image = self.createSprite(spriteSheet, 780, 335, width, width)
        self.color = BLACK
        self.state = ''