from BasicSprite import *

class GoalTile(BasicSprite):

    def __init__(self, row, col, width, spriteSheet):
        BasicSprite.__init__(self, row, col, width)
        self._layer = 1
        self.image = self.createSprite(spriteSheet, 765, 493, 16, 16, WHITE)
        self.image = pygame.transform.scale(self.image, (GAP, GAP))
        self.weight = 1