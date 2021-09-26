from config import *
import pygame

class DogSprite2():
    def __init__(self, spriteSheet):



        self.dogSpriteSheet = self.createSpriteSheets(spriteSheet)


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
        up.append(pygame.transform.scale(self.createSprite(spriteSheet, 15, 116, 26, 35, (0, 0, 0)), (50, 60)))
        up.append(pygame.transform.scale(self.createSprite(spriteSheet, 44, 116, 26, 35, (0, 0, 0)), (50, 60)))
        up.append(pygame.transform.scale(self.createSprite(spriteSheet, 70, 116, 26, 35, (0, 0, 0)), (50, 60)))
        up.append(pygame.transform.scale(self.createSprite(spriteSheet, 92, 116, 26, 35, (0, 0, 0)), (50, 60)))

        right = []

        right.append(pygame.transform.scale(self.createSprite(spriteSheet, 9, 54, 30,25, (0, 0, 0)), (40, 50)))
        right.append(pygame.transform.scale(self.createSprite(spriteSheet, 41, 54, 30, 25, (0, 0, 0)), (40, 50)))
        right.append(pygame.transform.scale(self.createSprite(spriteSheet, 74, 54, 30, 25, (0, 0, 0)), (40, 50)))
        right.append(pygame.transform.scale(self.createSprite(spriteSheet, 108, 54, 30, 25, (0, 0, 0)), (40, 50)))

        left = []

        left.append(pygame.transform.flip(
            pygame.transform.scale(self.createSprite(spriteSheet, 9, 54, 30, 25, (0, 0, 0)), (40, 50)), True, False))
        left.append(pygame.transform.flip(
            pygame.transform.scale(self.createSprite(spriteSheet, 41, 54, 30, 25, (0, 0, 0)), (40, 50)), True, False))
        left.append(pygame.transform.flip(
            pygame.transform.scale(self.createSprite(spriteSheet, 74, 54, 30, 25, (0, 0, 0)), (40, 50)), True, False))
        left.append(pygame.transform.flip(
            pygame.transform.scale(self.createSprite(spriteSheet, 108, 54, 30, 25, (0, 0, 0)), (40, 50)), True, False))

        down = []
        down.append(pygame.transform.scale(self.createSprite(spriteSheet, 16, 24, 26, 30, (0, 0, 0)), (50, 60)))
        down.append(pygame.transform.scale(self.createSprite(spriteSheet, 47, 24, 26, 30, (0, 0, 0)), (50, 60)))
        down.append(pygame.transform.scale(self.createSprite(spriteSheet, 79, 24, 26, 30, (0, 0, 0)), (50, 60)))
        down.append(pygame.transform.scale(self.createSprite(spriteSheet, 111, 24, 26, 30, (0, 0, 0)), (50, 60)))

        sleep = []
        sleep.append(pygame.transform.scale(self.createSprite(spriteSheet, 44, 209, 30, 29, (0, 0, 0)), (40, 50)))
        sleep.append(pygame.transform.scale(self.createSprite(spriteSheet, 91, 209, 30, 29, (0, 0, 0)), (40, 50)))

        stay = []
        stay.append(pygame.transform.scale(self.createSprite(spriteSheet, 106, 164, 30, 30, (0, 0, 0)), (40, 50)))


        love = []

        #love.append(pygame.transform.scale(self.createSprite(spriteSheet, 4, 168, 26, 35, (0, 0, 0)), (40, 50)))
        #love.append(pygame.transform.scale(self.createSprite(spriteSheet, 35, 168, 26, 35, (0, 0, 0)), (40, 50)))
        #love.append(pygame.transform.scale(self.createSprite(spriteSheet, 65, 168, 26, 35, (0, 0, 0)), (40, 50)))
        #love.append(pygame.transform.scale(self.createSprite(spriteSheet, 99, 168, 26, 35, (0, 0, 0)), (40, 50)))
        love.append(pygame.transform.scale(self.createSprite(spriteSheet, 107, 165, 26, 35, (0, 0, 0)), (40, 50)))
        love.append(pygame.transform.scale(self.createSprite(spriteSheet, 138, 165, 26, 35, (0, 0, 0)), (40, 50)))

        love.append(pygame.transform.scale(self.createSprite(spriteSheet, 107, 165, 26, 35, (0, 0, 0)), (40, 50)))
        love.append(pygame.transform.scale(self.createSprite(spriteSheet, 138, 165, 26, 35, (0, 0, 0)), (40, 50)))

        love.append(pygame.transform.scale(self.createSprite(spriteSheet, 107, 165, 26, 35, (0, 0, 0)), (40, 50)))
        love.append(pygame.transform.scale(self.createSprite(spriteSheet, 138, 165, 26, 35, (0, 0, 0)), (40, 50)))
        love.append(pygame.transform.scale(self.createSprite(spriteSheet, 6, 204, 26, 35, (0, 0, 0)), (40, 50)))

        love.append(pygame.transform.scale(self.createSprite(spriteSheet, 6, 204, 26, 35, (0, 0, 0)), (40, 50)))
        love.append(pygame.transform.scale(self.createSprite(spriteSheet, 6, 204, 26, 35, (0, 0, 0)), (40, 50)))
        love.append(pygame.transform.scale(self.createSprite(spriteSheet, 6, 204, 26, 35, (0, 0, 0)), (40, 50)))
        love.append(pygame.transform.scale(self.createSprite(spriteSheet, 6, 204, 26, 35, (0, 0, 0)), (40, 50)))
        love.append(pygame.transform.scale(self.createSprite(spriteSheet, 6, 204, 26, 35, (0, 0, 0)), (40, 50)))
        love.append(pygame.transform.scale(self.createSprite(spriteSheet, 6, 204, 26, 35, (0, 0, 0)), (40, 50)))
        love.append(pygame.transform.scale(self.createSprite(spriteSheet, 6, 204, 26, 35, (0, 0, 0)), (40, 50)))
        love.append(pygame.transform.scale(self.createSprite(spriteSheet, 6, 204, 26, 35, (0, 0, 0)), (40, 50)))


















        animations.update({'Up': up})
        animations.update({'Right': right})
        animations.update({'Left': left})
        animations.update({'Down': down})
        animations.update({'Sleep': sleep})
        animations.update({'Stay': stay})
        animations.update({'Stay Right': stay})
        animations.update({'Love': love})

        return animations