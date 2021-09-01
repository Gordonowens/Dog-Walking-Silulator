from Node import *
from Barrier import *


class TreeBottom(Barrier):

    def __init__(self, row, col, width, total_rows, spriteSheet):
        Barrier.__init__(self, row, col, width, total_rows, spriteSheet)
        self._layer = 2
        self.image = self.createSprite(spriteSheet, 221, 187, 16, 16, WHITE)
        #self.image = pygame.transform.scale(self.image, (width, width))
        self.state = ''
        self.image = pygame.transform.scale(self.image, (30, 30))

