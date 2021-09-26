from Node import *
from BasicSprite import *


class TreeBottom(BasicSprite):

    def __init__(self, row, col, width, sprite):
        BasicSprite.__init__(self, row, col, width)
        self._layer = 2
        self.image = sprite
        self.image = pygame.transform.scale(self.image, (width, width))
        self.state = ''

