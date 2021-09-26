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
from Bread import *

'''
this class runs player controls
all inputs from user are handled by this class
'''
class Player(Animal):

    def __init__(self,  row, col, width, gameData):

        Animal.__init__(self, row, col, width, gameData.gameGrid, gameData.spriteSets.get('Player'), gameData.spriteGroup, gameData.characters)
        #sprite layer
        self._layer = 3
        self.items = []
        self.spriteGroup = gameData.spriteGroup
        self.characters = gameData.characters
        self.gameData = gameData
        self.breadCount = 0

        self.playerCommand = ''


    def throw(self, node):

        #check player has ball
        for i, item in enumerate(self.items):
            if isinstance(item, Ball):

                if not self.checkNodes(node.get_pos()) and node.get_pos() != self.get_pos():
                    self.dropItem(node, item)
                    self.items.pop(i)
                    #self.playerCommand = 'throw'
                    if self.movementSprite == 'Stay Right':
                        self.animationCells = self.spriteSets.get('Throw Right').copy()


                    elif self.movementSprite == 'Stay Left':
                        self.animationCells = self.spriteSets.get('Throw Left').copy()

                    self.movementSprite = 'Throw'


                    for dog in self.characters.get('Dogs'):
                        dog.goal = item
                        dog.animalState = "fetch"



    def throwBread(self, node):

        #check player has ball
        for i, item in enumerate(self.items):
            if isinstance(item, Bread):

                if not self.checkNodes(node.get_pos()) and node.get_pos() != self.get_pos():

                    self.dropItem(node, Bread(node.row, node.col, 30, self.gameData.spriteSets.get('Bread Scraps')))
                    self.breadCount = self.breadCount + 1
                    if self.breadCount > 10:
                        self.items.pop(i)
                    #self.playerCommand = 'throw'


    def dropItem(self, node, item):

        item.updatePosition(node.get_pos())
        self.spriteGroup.add(item)

        # add item sprite back into the game
        self.spriteGroup.add(item)

        # add the character back into the game
        self.addCharcter('Items', item)

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


            #down
            elif self.playerCommand == 'down':
                nextNode = [self.row, self.col + 1]

                if not self.checkNodes((self.row, self.col + 1)):
                    self.movementSprite = 'Down'
                    self.updatePosition(nextNode)

            #left
            elif self.playerCommand == 'left':
                nextNode = [self.row - 1, self.col]

                if not self.checkNodes((self.row -1, self.col)):
                    self.movementSprite = 'Left'
                    self.updatePosition(nextNode)

            #right
            elif self.playerCommand == 'right':
                nextNode = [self.row + 1, self.col]

                if not self.checkNodes((self.row + 1, self.col)):
                    self.movementSprite = 'Right'
                    self.updatePosition(nextNode)

            #space come here
            elif self.playerCommand == 'here boy':
                for dog in self.characters.get('Dogs'):
                    dog.playerCommand = 'follow'

            elif self.playerCommand == 'go away':
                for dog in self.characters.get('Dogs'):
                    dog.playerCommand = 'flee'

            elif self.playerCommand == 'stay':
                for dog in self.characters.get('Dogs'):
                    dog.playerCommand = 'stay'

            elif self.playerCommand == 'pick up':
                self.pickUp()


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
                pass
                #print('poo')



