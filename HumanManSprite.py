from config import *
import pygame


class HumanManSprite():
    def __init__(self, spriteSheet):



        self.humanSpriteSheet = self.createSpriteSheets(spriteSheet)


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

        animations = {}
        up = []
        up.append(pygame.transform.scale(self.createSprite(spriteSheet, 55, 40, 26, 35, (55,99,77)), (40, 50)))
        up.append(pygame.transform.scale(self.createSprite(spriteSheet, 123, 39, 26, 35, (55,99,77)), (40, 50)))

        right = []

        right.append(pygame.transform.scale(self.createSprite(spriteSheet, 42, 5, 26, 35, (55, 99, 77)), (40, 50)))
        right.append(pygame.transform.scale(self.createSprite(spriteSheet, 63, 2, 26, 35, (55, 99, 77)), (40, 50)))
        right.append(pygame.transform.scale(self.createSprite(spriteSheet, 100, 4, 26, 35, (55, 99, 77)), (40, 50)))
        right.append(pygame.transform.scale(self.createSprite(spriteSheet, 127, 5, 26, 35, (55, 99, 77)), (40, 50)))
        right.append(pygame.transform.scale(self.createSprite(spriteSheet, 150, 3, 26, 35, (55, 99, 77)), (40, 50)))
        right.append(pygame.transform.scale(self.createSprite(spriteSheet, 179, 5, 26, 35, (55, 99, 77)), (40, 50)))

        left = []

        left.append(pygame.transform.flip(pygame.transform.scale(self.createSprite(spriteSheet, 42, 5, 26, 35, (55, 99, 77)), (40, 50)), True, False))
        left.append(pygame.transform.flip(pygame.transform.scale(self.createSprite(spriteSheet, 63, 2, 26, 35, (55, 99, 77)), (40, 50)), True, False))
        left.append(pygame.transform.flip(pygame.transform.scale(self.createSprite(spriteSheet, 100, 4, 26, 35, (55, 99, 77)), (40, 50)), True, False))
        left.append(pygame.transform.flip(pygame.transform.scale(self.createSprite(spriteSheet, 127, 5, 26, 35, (55, 99, 77)), (40, 50)), True, False))
        left.append(pygame.transform.flip(pygame.transform.scale(self.createSprite(spriteSheet, 150, 3, 26, 35, (55, 99, 77)), (40, 50)), True, False))
        left.append(pygame.transform.flip(pygame.transform.scale(self.createSprite(spriteSheet, 179, 5, 26, 35, (55, 99, 77)), (40, 50)), True, False))

        down = []
        down.append(pygame.transform.scale(self.createSprite(spriteSheet, 55, 80, 26, 35, (55, 99, 77)), (40, 50)))
        down.append(pygame.transform.scale(self.createSprite(spriteSheet, 79, 84, 26, 35, (55, 99, 77)), (40, 50)))
        down.append(pygame.transform.scale(self.createSprite(spriteSheet, 102, 81, 26, 35, (55, 99, 77)), (40, 50)))
        down.append(pygame.transform.scale(self.createSprite(spriteSheet, 125, 80, 26, 35, (55, 99, 77)), (40, 50)))
        down.append(pygame.transform.scale(self.createSprite(spriteSheet, 148, 83, 26, 35, (55, 99, 77)), (40, 50)))
        down.append(pygame.transform.scale(self.createSprite(spriteSheet, 171, 81, 26, 35, (55, 99, 77)), (40, 50)))

        stayUp =[]
        stayUp.append(pygame.transform.scale(self.createSprite(spriteSheet, 3, 41, 26, 35, (55, 99, 77)), (40, 50)))

        stayDown = []
        stayDown.append(pygame.transform.scale(self.createSprite(spriteSheet, 2, 79, 26, 35, (55, 99, 77)), (40, 50)))

        stayRight = []
        stayRight.append(pygame.transform.scale(self.createSprite(spriteSheet, 3, 3, 26, 35, (55, 99, 77)), (40, 50)))

        stayLeft = []
        stayLeft.append(pygame.transform.scale(self.createSprite(spriteSheet, 3, 3, 26, 35, (55, 99, 77)), (40, 50)))

        throw = []
        throw.append(pygame.transform.scale(self.createSprite(spriteSheet, 89, 576, 26, 35, (55, 99, 77)), (40, 50)))
        throw.append(pygame.transform.scale(self.createSprite(spriteSheet, 125, 580, 26, 35, (55, 99, 77)), (40, 50)))
        throw.append(pygame.transform.scale(self.createSprite(spriteSheet, 169, 578, 26, 35, (55, 99, 77)), (40, 50)))
        throw.append(pygame.transform.scale(self.createSprite(spriteSheet, 201, 577, 26, 35, (55, 99, 77)), (40, 50)))

        animations.update({'Up': up})
        animations.update({'Right': right})
        animations.update({'Left': left})
        animations.update({'Down': down})
        animations.update({'Stay Up': stayUp})
        animations.update({'Stay Down': stayDown})
        animations.update({'Stay Right': stayRight})
        animations.update({'Stay Left': stayLeft})
        animations.update({'Throw': throw})

        return animations