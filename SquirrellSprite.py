
from config import *
import pygame

class SquirrellSprite():

    def __init__(self, spriteSheet):

        self.squirrelSpriteSheet = self.createSpriteSheets(spriteSheet)



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

    def createSpriteSheets(self, spriteSheet):

        #self.createSprite(spriteSheet, 0, 0, width, width)

        animations = {}
        up = []
        up.append(self.createSprite(spriteSheet, 6, 230, 30, 30, (0,0,0)))
        up.append(self.createSprite(spriteSheet, 39, 226, 30, 30, (0,0,0)))
        up.append(self.createSprite(spriteSheet, 72, 234, 30, 30, (0,0,0)))

        left = []

        left.append(self.createSprite(spriteSheet, 4, 38, 30, 30, (0,0,0)))
        left.append(self.createSprite(spriteSheet, 37, 38, 30, 30, (0,0,0)))
        left.append(self.createSprite(spriteSheet, 68, 38, 30, 30, (0,0,0)))
        left.append(self.createSprite(spriteSheet, 166, 37, 30, 30, (0,0,0)))

        right = []


        right.append(self.createSprite(spriteSheet, 4, 38, 26, 35, (0,0,0)))
        right.append(self.createSprite(spriteSheet, 37, 38, 26, 35, (0,0,0)))
        right.append(self.createSprite(spriteSheet, 68, 38, 26, 35, (0,0,0)))
        right.append(self.createSprite(spriteSheet, 166, 37, 26, 35, (0,0,0)))


        down = []
        down.append(self.createSprite(spriteSheet, 8, 196, 26, 35, (0,0,0)))
        down.append(self.createSprite(spriteSheet, 40, 191, 26, 35, (0,0,0)))
        down.append(self.createSprite(spriteSheet, 72, 194, 26, 35, (0,0,0)))

        stayRight = []
        stayRight.append(self.createSprite(spriteSheet, 196, 4, 26, 35, (0, 0, 0)))


        animations.update({'Up': up})
        animations.update({'Right': right})
        animations.update({'Left': left})
        animations.update({'Down': down})
        animations.update({'Stay Right': stayRight})


        return animations