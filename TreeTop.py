from Node import *

class TreeTop(Node):

    def __init__(self, row, col, width, total_rows, spriteSheet):
        Node.__init__(self, row, col, width, total_rows, spriteSheet)
        self._layer = 5
        self.image = self.createSprite(spriteSheet, 780, 335, width, width)