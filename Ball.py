from BasicSprite import *

class Ball(BasicSprite):

    def __init__(self, row, col, width, total_rows, spriteSheet):
        BasicSprite.__init__(self, row, col, width, total_rows, spriteSheet)
        self._layer = 1
        self.image = pygame.transform.scale(self.createSprite(spriteSheet, 69, 71, 18, 18), (10, 10))
        self.image = pygame.transform.scale(self.image, (10, 10))

