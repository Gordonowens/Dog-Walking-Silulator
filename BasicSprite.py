from config import *
from pygame import *


class BasicSprite(pygame.sprite.Sprite):
    def __init__(self, row, col, width, total_rows, spriteSheet):

        pygame.sprite.Sprite.__init__(self)
        # variables for sprite
        self._layer = 0
        self.image = self.createSprite(spriteSheet, 178, 143, width, width)
        self.rect = self.image.get_rect()
        self.x = row * width
        self.y = col * width
        self.rect.x = self.x
        self.rect.y = self.y
        self.width = width

        # variables for game grid
        self.pos = vec((self.x, self.y))
        self.row = row
        self.col = col
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def createSprite(self, spriteSheet, x, y, width, height, background = BLACK):
        '''

        :param spriteSheet:
        :param x:
        :param y:
        :param width:
        :param height:
        :return:
        '''

        sprite = pygame.Surface([width, height])
        sprite.blit(spriteSheet, (0, 0), (x, y, width, height))
        # this is used to create transperancy in the sprite
        sprite.set_colorkey(background)
        return sprite

    def updatePosition(self, position):
        '''
        :tuple position: x, y
        :return:
        '''

        # update position on game grid
        self.row = position[0]
        self.col = position[1]
        # set position of upper left of sprites rectangle
        self.pos.x = position[0] * 30
        self.pos.y = position[1] * 30

        # update sprite rectangle
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

    def get_pos(self):
        return self.row, self.col
