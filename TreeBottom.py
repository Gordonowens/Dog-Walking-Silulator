from Node import *
from Barrier import *


class TreeBottom(Barrier):

    def __init__(self, row, col, width, sprite):
        Barrier.__init__(self, row, col, width, sprite)
        self._layer = 2
        #self.image = sprite
        #self.image = pygame.transform.scale(self.image, (width, width))
        self.state = ''


