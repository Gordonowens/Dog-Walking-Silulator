from config import *
import pygame

class DuckSprite():

    def __init__(self, spriteSheet):

        self.duckSpriteSheet = self.createSpriteSheets(spriteSheet)



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

        #pygame.transform.scale( (20, 20))
        up.append(pygame.transform.scale(self.createSprite(spriteSheet, 12, 158, 20, 33, (0,0,0)), (17, 23)))
        up.append(pygame.transform.scale(self.createSprite(spriteSheet, 61, 158, 20, 33, (0,0,0)), (17, 23)))
        up.append(pygame.transform.scale(self.createSprite(spriteSheet, 108, 158, 20, 33, (0,0,0)), (17, 23)))

        left = []

        left.append(pygame.transform.scale(self.createSprite(spriteSheet, 6, 64, 33, 31, (0,0,0)), (17, 23)))
        left.append(pygame.transform.scale(self.createSprite(spriteSheet, 56, 64, 33, 31, (0,0,0)), (17, 23)))
        left.append(pygame.transform.scale(self.createSprite(spriteSheet, 101, 64, 33, 31, (0,0,0)), (17, 23)))

        right = []



        right.append(pygame.transform.scale(pygame.transform.flip(
            self.createSprite(spriteSheet, 6, 64, 33, 31, (0, 0, 0)), True, False), (17, 23)))
        right.append(pygame.transform.scale(pygame.transform.flip(
            self.createSprite(spriteSheet, 56, 64, 33, 31, (0, 0, 0)), True, False), (17, 23)))
        right.append(pygame.transform.scale(pygame.transform.flip(
            self.createSprite(spriteSheet, 101, 64, 33, 31, (0, 0, 0)), True, False), (17, 23)))



        down = []
        down.append(pygame.transform.scale(self.createSprite(spriteSheet, 12, 19, 22, 28, (0,0,0)), (17, 23)))
        down.append(pygame.transform.scale(self.createSprite(spriteSheet, 61, 19, 22, 28, (0,0,0)), (17, 23)))
        down.append(pygame.transform.scale(self.createSprite(spriteSheet, 108, 19, 22, 28, (0,0,0)), (17, 23)))

        stayRight = []
        stayRight.append(pygame.transform.scale(pygame.transform.flip(
            self.createSprite(spriteSheet, 6, 64, 33, 31, (0, 0, 0)), True, False), (17, 23)))


        animations.update({'Up': up})
        animations.update({'Right': right})
        animations.update({'Left': left})
        animations.update({'Down': down})
        animations.update({'Stay Right': stayRight})


        return animations