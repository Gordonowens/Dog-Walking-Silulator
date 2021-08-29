from Node import *

class Ball(Node):

    def __init__(self, row, col, width, total_rows, spriteSheet):
        Node.__init__(self, row, col, width, total_rows, spriteSheet)
        self._layer = 1
        self.image = pygame.transform.scale(self.createSprite(spriteSheet, 74, 74, 73, 73), (10, 10))
