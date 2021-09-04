# from sprites import *
import pygame
from config import *
from algorithms import *
from Node import *
from random import randrange
import sys
from Ball import *
from Animal import *
import random

'''
this class runs player controls
all inputs from user are handled by this class
'''
class Player(Animal):
    def __init__(self, grid, row, col, width, total_rows, spriteSheet, spriteGroup, characters):

        Animal.__init__(self, row, col, width, total_rows, grid, spriteSheet, spriteGroup, characters)
        #sprite layer
        self._layer = 2
        self.grid = grid
        self.items = []
        self.spriteGroup = spriteGroup
        self.characters = characters
        self.playerCommand = ''



    def throw(self, node):

        #check player has ball
        for i, item in enumerate(self.items):
            if isinstance(item, Ball):

                if not self.checkNodes(node.get_pos()) and node.get_pos() != self.get_pos():
                    self.dropItem(node, item)
                    self.items.pop(i)
                    self.playerCommand = 'throw'
                    self.animationCells = self.spriteSets.get('Throw').copy()
                    self.movementSprite = 'Throw'
                    return item

        return 0

    def update(self):
        '''
        this class deals with user inputs for moving player character and interacting
        with the world
        '''

        self.coolDownTimer = self.coolDownTimer - 1


        if self.coolDownTimer < - 1:
            #up
            if self.playerCommand == 'up':
                nextNode = [self.row, self.col - 1]

                if not self.checkNodes((self.row, self.col - 1)):
                    self.movementSprite = 'Up'
                    self.updatePosition(nextNode)

                #self.nextMovement = ''

            #down
            elif self.playerCommand == 'down':
                nextNode = [self.row, self.col + 1]

                if not self.checkNodes((self.row, self.col + 1)):
                    self.movementSprite = 'Down'
                    self.updatePosition(nextNode)

                #self.nextMovement = ''

            #left
            elif self.playerCommand == 'left':
                nextNode = [self.row - 1, self.col]

                if not self.checkNodes((self.row -1, self.col)):
                    self.movementSprite = 'Left'
                    self.updatePosition(nextNode)

                #self.nextMovement = ''

            #right
            elif self.playerCommand == 'right':
                nextNode = [self.row + 1, self.col]

                if not self.checkNodes((self.row + 1, self.col)):
                    self.movementSprite = 'Right'
                    self.updatePosition(nextNode)

                #self.nextMovement = ''

            #space come here
            elif self.playerCommand == 'here boy':
                for dog in self.characters.get('Dogs'):
                    dog.playerCommand = 'follow'

                #self.nextMovement = ''

            elif self.playerCommand == 'go away':
                for dog in self.characters.get('Dogs'):
                    dog.playerCommand = 'flee'

                #self.nextMovement = ''

            elif self.playerCommand == 'stay':
                for dog in self.characters.get('Dogs'):
                    dog.playerCommand = 'stay'

                #self.nextMovement = ''

            elif self.playerCommand == 'throw':

                ball = self.throw()
                if ball != 0:
                    for dog in self.characters.get('Dogs'):
                        dog.goal = ball
                        dog.animalState = "fetch"
                #self.nextMovement = ''

            elif self.playerCommand == 'pick up':
                self.pickUp()

                #self.nextMovement = ''

            elif self.playerCommand == '':

                if self.movementSprite == 'Right':
                    self.movementSprite = 'Stay Right'
                    self.updateSprite()

                elif self.movementSprite == 'Left':
                    self.movementSprite = 'Stay Left'
                    self.updateSprite()

                elif self.movementSprite == 'Up':
                    self.movementSprite = 'Stay Up'
                    self.updateSprite()

                elif self.movementSprite == 'Down':
                    self.movementSprite = 'Stay Down'
                    self.updateSprite()

                elif self.movementSprite == 'Throw' and len(self.animationCells) == 0:
                    self.movementSprite = 'Stay Down'
                    self.updateSprite()

                elif self.movementSprite == 'Throw':
                    self.animateAnimals()

            self.coolDownTimer = 0
            if random.randint(0, 100) < 36:
                print('poo')


        #if self.coolDownTimer < 0:

            #self.coolDownTimer = self.coolDown

        def testfunc(self, spriteSheet):

            animations = {}
            up = []
            up.append(pygame.transform.scale(self.createSprite(spriteSheet, 55, 40, 26, 35, (55, 99, 77)), (40, 50)))
            up.append(pygame.transform.scale(self.createSprite(spriteSheet, 123, 39, 26, 35, (55, 99, 77)), (40, 50)))

            right = []

            right.append(pygame.transform.scale(self.createSprite(spriteSheet, 42, 5, 26, 35, (55, 99, 77)), (40, 50)))
            right.append(pygame.transform.scale(self.createSprite(spriteSheet, 63, 2, 26, 35, (55, 99, 77)), (40, 50)))
            right.append(pygame.transform.scale(self.createSprite(spriteSheet, 100, 4, 26, 35, (55, 99, 77)), (40, 50)))
            right.append(pygame.transform.scale(self.createSprite(spriteSheet, 127, 5, 26, 35, (55, 99, 77)), (40, 50)))
            right.append(pygame.transform.scale(self.createSprite(spriteSheet, 150, 3, 26, 35, (55, 99, 77)), (40, 50)))
            right.append(pygame.transform.scale(self.createSprite(spriteSheet, 179, 5, 26, 35, (55, 99, 77)), (40, 50)))

            left = []

            left.append(pygame.transform.flip(
                pygame.transform.scale(self.createSprite(spriteSheet, 42, 5, 26, 35, (55, 99, 77)), (40, 50)), True,
                False))
            left.append(pygame.transform.flip(
                pygame.transform.scale(self.createSprite(spriteSheet, 63, 2, 26, 35, (55, 99, 77)), (40, 50)), True,
                False))
            left.append(pygame.transform.flip(
                pygame.transform.scale(self.createSprite(spriteSheet, 100, 4, 26, 35, (55, 99, 77)), (40, 50)), True,
                False))
            left.append(pygame.transform.flip(
                pygame.transform.scale(self.createSprite(spriteSheet, 127, 5, 26, 35, (55, 99, 77)), (40, 50)), True,
                False))
            left.append(pygame.transform.flip(
                pygame.transform.scale(self.createSprite(spriteSheet, 150, 3, 26, 35, (55, 99, 77)), (40, 50)), True,
                False))
            left.append(pygame.transform.flip(
                pygame.transform.scale(self.createSprite(spriteSheet, 179, 5, 26, 35, (55, 99, 77)), (40, 50)), True,
                False))

            down = []
            down.append(pygame.transform.scale(self.createSprite(spriteSheet, 55, 80, 26, 35, (55, 99, 77)), (40, 50)))
            down.append(pygame.transform.scale(self.createSprite(spriteSheet, 79, 84, 26, 35, (55, 99, 77)), (40, 50)))
            down.append(pygame.transform.scale(self.createSprite(spriteSheet, 102, 81, 26, 35, (55, 99, 77)), (40, 50)))
            down.append(pygame.transform.scale(self.createSprite(spriteSheet, 125, 80, 26, 35, (55, 99, 77)), (40, 50)))
            down.append(pygame.transform.scale(self.createSprite(spriteSheet, 148, 83, 26, 35, (55, 99, 77)), (40, 50)))
            down.append(pygame.transform.scale(self.createSprite(spriteSheet, 171, 81, 26, 35, (55, 99, 77)), (40, 50)))

            stayUp = []
            stayUp.append(pygame.transform.scale(self.createSprite(spriteSheet, 3, 41, 26, 35, (55, 99, 77)), (40, 50)))

            stayDown = []
            stayDown.append(
                pygame.transform.scale(self.createSprite(spriteSheet, 2, 79, 26, 35, (55, 99, 77)), (40, 50)))

            stayRight = []
            stayRight.append(
                pygame.transform.scale(self.createSprite(spriteSheet, 3, 3, 26, 35, (55, 99, 77)), (40, 50)))

            stayLeft = []
            stayLeft.append(
                pygame.transform.scale(self.createSprite(spriteSheet, 3, 3, 26, 35, (55, 99, 77)), (40, 50)))

            throw = []
            throw.append(
                pygame.transform.scale(self.createSprite(spriteSheet, 89, 576, 26, 35, (55, 99, 77)), (40, 50)))
            throw.append(
                pygame.transform.scale(self.createSprite(spriteSheet, 125, 580, 26, 35, (55, 99, 77)), (40, 50)))
            throw.append(
                pygame.transform.scale(self.createSprite(spriteSheet, 169, 578, 26, 35, (55, 99, 77)), (40, 50)))
            throw.append(
                pygame.transform.scale(self.createSprite(spriteSheet, 201, 577, 26, 35, (55, 99, 77)), (40, 50)))

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


