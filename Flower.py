from BasicSprite import *
from random import randrange

class Flower(BasicSprite):

    def __init__(self, row, col, width, spriteSheet):
        BasicSprite.__init__(self, row, col, width)
        self._layer = 1
        self.image = self.createSprite(spriteSheet, 51, self.selectRandomFlower(), 16, 16, WHITE)
        self.image = pygame.transform.scale(self.image, (GAP, GAP))
        self.weight = 1
        self.type = 'Flower'


    def selectRandomFlower(self):

        flowerY  = [170, 221, 119]
        return flowerY[randrange(3)]