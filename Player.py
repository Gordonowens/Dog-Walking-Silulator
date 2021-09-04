# from sprites import *
import pygame
from config import *
from algorithms import *
from Node import *
from random import randrange
import sys
from Ball import *
from Animal import *

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
        self.nextMovement = ''



    def throw(self):

        #check player has ball
        for i, item in enumerate(self.items):
            if isinstance(item, Ball):
                nodeList = []
                #get sphere of influence
                # iterate through grid and add acceptable nodes to list
                for row in getGridSquare(self.get_pos(), 5, self.grid.getGrid()):

                    for node in row:
                        if not self.checkNodes(node.get_pos()) and node.get_pos() != self.get_pos():
                           nodeList.append(node)

                #pick random node in list and drop ball there
                node = nodeList[randrange(len(nodeList))]
                self.dropItem(node, item)
                self.items.pop(i)

                return item

        return 0

    def update(self):
        '''
        this class deals with user inputs for moving player character and interacting
        with the world
        '''

        self.coolDownTimer = self.coolDownTimer - 1



        #up
        if self.nextMovement == 'up':
            nextNode = [self.row, self.col - 1]

            if not self.checkNodes((self.row, self.col - 1)):
                self.movementNow = 'Up'
                self.updatePosition(nextNode)

            #self.nextMovement = ''

        #down
        elif self.nextMovement == 'down':
            nextNode = [self.row, self.col + 1]

            if not self.checkNodes((self.row, self.col + 1)):
                self.movementNow = 'Down'
                self.updatePosition(nextNode)

            #self.nextMovement = ''

        #left
        elif self.nextMovement == 'left':
            nextNode = [self.row - 1, self.col]

            if not self.checkNodes((self.row -1, self.col)):
                self.movementNow = 'Left'
                self.updatePosition(nextNode)

            #self.nextMovement = ''

        #right
        elif self.nextMovement == 'right':
            nextNode = [self.row + 1, self.col]

            if not self.checkNodes((self.row + 1, self.col)):
                self.movementNow = 'Right'
                self.updatePosition(nextNode)

            #self.nextMovement = ''

        #space come here
        elif self.nextMovement == 'here boy':
            for dog in self.characters.get('Dogs'):
                dog.playerCommand = 'follow'

            #self.nextMovement = ''

        elif self.nextMovement == 'go away':
            for dog in self.characters.get('Dogs'):
                dog.playerCommand = 'flee'

            #self.nextMovement = ''

        elif self.nextMovement == 'stay':
            for dog in self.characters.get('Dogs'):
                dog.playerCommand = 'stay'

            #self.nextMovement = ''

        elif self.nextMovement == 'throw':

            ball = self.throw()
            if ball != 0:
                for dog in self.characters.get('Dogs'):
                    dog.goal = ball
                    dog.animalState = "fetch"
            #self.nextMovement = ''

        elif self.nextMovement == 'pick up':
            self.pickUp()

            #self.nextMovement = ''

        elif self.nextMovement == '':

            if self.movementNow == 'Right':
                self.movementNow = 'Stay Right'
                self.updateSprite()

            elif self.movementNow == 'Left':
                self.movementNow = 'Stay Left'
                self.updateSprite()

            elif self.movementNow == 'Up':
                self.movementNow = 'Stay Up'
                self.updateSprite()

            elif self.movementNow == 'Down':
                self.movementNow = 'Stay Down'
                self.updateSprite()







        #if self.coolDownTimer < 0:

            #self.coolDownTimer = self.coolDown


