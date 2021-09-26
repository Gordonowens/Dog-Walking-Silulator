from BasicSprite import *

class BarrierAccrossSprite(BasicSprite):

    def __init__(self, row, col, width, spriteSheet):
        BasicSprite.__init__(self, row, col, width)
        self.image = self.createSprite(spriteSheet, 799, 391, 16, 16, WHITE)
        self.image = pygame.transform.scale(self.image, (30, 30))
        self._layer = 2