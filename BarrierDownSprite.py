from BasicSprite import *

class BarrierDownSprite(BasicSprite):

    def __init__(self, row, col, width, spriteSheet):
        BasicSprite.__init__(self, row, col, width)
        self.image = self.createSprite(spriteSheet, 860, 391, 16, 16, WHITE)
        self.image = pygame.transform.scale(self.image, (GAP, GAP))
        self._layer = 2