from BasicSprite import *
from random import randrange

class RoughGround(BasicSprite):

    def __init__(self, row, col, width, spriteSheet):
        BasicSprite.__init__(self, row, col, width)
        self._layer = 1
        self.ground = self.getGround()
        self.image = self.createSprite(spriteSheet, self.ground[0], self.ground[1], 16, 16, WHITE)
        self.image = pygame.transform.scale(self.image, (GAP, GAP))
        self.weight = 1
        self.type = 'Rough'


    def getGround(self):

        grounds  = [[102, 0], [102, 17], [136, 170]]
        return grounds[randrange(3)]