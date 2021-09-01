from BasicSprite import *


class Barrier(BasicSprite):

    def __init__(self, row, col, width, total_rows, spriteSheet):
        BasicSprite.__init__(self, row, col, width, total_rows, spriteSheet)
        self._layer = 2
        #960, 448
        #
        self.image = self.createSprite(spriteSheet, 960, 448, 30, 30)
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.color = BLACK
        self.state = 'barrier'
