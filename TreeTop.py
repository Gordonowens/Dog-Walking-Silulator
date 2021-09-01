from BasicSprite import *

class TreeTop(BasicSprite):

    def __init__(self, row, col, width, total_rows, spriteSheet):
        BasicSprite.__init__(self, row, col, width, total_rows, spriteSheet)
        self._layer = 5
        self.image = self.createSprite(spriteSheet, 221, 170, 16, 16, WHITE)
        self.image = pygame.transform.scale(self.image, (30, 30))