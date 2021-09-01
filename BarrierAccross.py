from Barrier import *

class BarrierAccross(Barrier):

    def __init__(self, row, col, width, total_rows, spriteSheet):
        Barrier.__init__(self, row, col, width, total_rows, spriteSheet)

        self.image = self.createSprite(spriteSheet, 799, 391, 16, 16, WHITE)
        self.image = pygame.transform.scale(self.image, (30, 30))
        #self.color = BLACK