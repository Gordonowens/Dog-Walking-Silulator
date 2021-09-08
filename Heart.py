from BasicSprite import *

class Heart(BasicSprite):

    def __init__(self, row, col, width, total_rows, spriteSheet):

        self.spriteSet =  self.createSpriteSet(spriteSheet)
        self.image =  self.spriteSet[0]
        BasicSprite.__init__(self, row, col, width, total_rows, self.image)
        self._layer = 6
        self.coolDown = 7


    def createSpriteSet(self, spriteSheet):

        spriteSet = []
        spriteSet.append(pygame.transform.scale(self.createSprite(spriteSheet, 20, 70, 480, 368, (0, 0, 0)),
                               (5, 10)))
        spriteSet.append(pygame.transform.scale(self.createSprite(spriteSheet, 20, 70, 480, 368, (0, 0, 0)),
                                                (10, 15)))
        spriteSet.append(pygame.transform.scale(self.createSprite(spriteSheet, 20, 70, 480, 368, (0, 0, 0)),
                                                (20, 25)))
        spriteSet.append(pygame.transform.scale(self.createSprite(spriteSheet, 20, 70, 480, 368, (0, 0, 0)),
                                                (10, 15)))

        return spriteSet

    def update(self):

        self.coolDown = self.coolDown - 1
        if len(self.spriteSet) == 0:
            self.kill()



        elif self.coolDown == 0:

            self.image = self.spriteSet.pop()
            self.coolDown = 7



