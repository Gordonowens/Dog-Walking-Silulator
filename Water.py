from BasicSprite import *

class Water(BasicSprite):

    def __init__(self, row, col, width, sprite):
        BasicSprite.__init__(self, row, col, width)
        self._layer = 2
        self.image = sprite
        pygame.transform.scale(self.image, (GAP, GAP))



