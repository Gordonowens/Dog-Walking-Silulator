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
        self.image = self.createSprite(spriteSheet, 3, 2, width, width)
        self.grid = grid
        self.items = []
        self.spriteGroup = spriteGroup
        self.characters = characters

    def throw(self):

        #check player has ball
        for i, item in enumerate(self.items):
            if isinstance(item, Ball):
                nodeList = []
                #get sphere of influence
                # iterate through grid and add acceptable nodes to list
                for row in getGridSquare(self.get_pos(), 5, self.grid.getGrid()):

                    for node in row:
                        if node not in self.characters.get('Barriers') and node.get_pos() != self.get_pos():
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

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:

                #up
                if event.key == pygame.K_UP:
                    nextNode = [self.row, self.col - 1]

                    if not self.checkNodes('Barriers', (self.row, self.col - 1)):
                        self.updatePosition(nextNode)

                #down
                elif event.key == pygame.K_DOWN:
                    nextNode = [self.row, self.col + 1]

                    if not self.checkNodes('Barriers', (self.row, self.col + 1)):
                        self.updatePosition(nextNode)

                #left
                elif event.key == pygame.K_LEFT:
                    nextNode = [self.row - 1, self.col]

                    if not self.checkNodes('Barriers', (self.row -1, self.col)):
                        self.updatePosition(nextNode)

                #right
                elif event.key == pygame.K_RIGHT:
                    nextNode = [self.row + 1, self.col]

                    if not self.checkNodes('Barriers', (self.row + 1, self.col)):
                        self.updatePosition(nextNode)

                #space come here
                elif event.key == pygame.K_SPACE:
                    for dog in self.characters.get('Dogs'):
                        dog.playerCommand = 'follow'

                elif event.key == pygame.K_LCTRL:
                    for dog in self.characters.get('Dogs'):
                        dog.playerCommand = 'flee'

                elif event.key == pygame.K_s:
                    for dog in self.characters.get('Dogs'):
                        dog.playerCommand = 'stay'

                elif event.key == pygame.K_t:

                    ball = self.throw()
                    if ball != 0:
                        for dog in self.characters.get('Dogs'):
                            dog.goal = ball
                            dog.animalState = "fetch"

                elif event.key == pygame.K_p:
                    self.pickUp()
