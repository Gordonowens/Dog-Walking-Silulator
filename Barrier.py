from Node import *


class Barrier(Node):
    def __init__(self, row, col, width, total_rows, spriteSheet):


        Node.__init__(self, row, col, width, total_rows, spriteSheet)
        self._layer = 2
        self.image = self.createSprite(spriteSheet, 960, 448, width, width)
        self.color = BLACK
        self.state = 'barrier'



    def test(self):
        pass