from BasicSprite import *

class Bread(BasicSprite):

    def __init__(self, row, col, width, spriteSurface):
        BasicSprite.__init__(self, row, col, width)
        self.image = spriteSurface

        self._layer = 1