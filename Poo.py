from BasicSprite import *

class Poo(BasicSprite):

    def __init__(self):
        BasicSprite.__init__(self, 0, 0, 30, 60, pygame.image.load('img/terrain2.png').convert())
        self._layer = 1

        self.image = pygame.transform.scale(self.createSprite(pygame.image.load('img/terrain2.png').convert(), 919, 325, 18, 18, (255,255,255)), (10, 10))
        self.image = pygame.transform.scale(self.image, (10, 10))

