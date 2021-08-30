# from sprites import *
import pygame
from config import *
from algorithms import *
from Node import *
from random import randrange
import sys
from Ball import *

'''
this class runs player controls
all inputs from user are handled by this class
'''
class Player(Node):
    def __init__(self, grid, row, col, width, total_rows, spriteSheet, spriteGroup, characters):

        Node.__init__(self, row, col, width, total_rows, spriteSheet)
        #sprite layer
        self._layer = 2
        self.image = self.createSprite(spriteSheet, 3, 2, width, width)
        self.grid = grid
        self.items = []
        self.spriteGroup = spriteGroup
        self.characters = characters

    def pickUp(self):
        for i, item in enumerate(self.characters.get('Items')):
            if item.get_pos() == self.get_pos():
                #add items to players dictrionary
                self.items.append(item)

                #remove from interactive characters item list
                self.removeCharacter('Items', i)
                #remove item sprite from sprite group
                item.kill()

    def removeCharacter(self, characterType, position):
        tempArray = self.characters.get(characterType)
        tempArray.pop(position)
        self.characters.update({characterType: tempArray})



    def addCharcter(self, characterType, character):
        #get the specific array from the interactive characters dictionary
        tempArray = self.characters.get(characterType)

        #add character to array
        tempArray.append(character)
        #update characters dictionary
        self.characters.update({characterType: tempArray})



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

    def dropItem(self, node, item):

        #update item's position
        item.updatePosition(node.get_pos())

        #add item sprite back into the game
        self.spriteGroup.add(item)

        #add the character back into the game
        self.addCharcter('Items', item)

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

                    if self.grid.getGrid()[nextNode[0]][nextNode[1]] not in self.characters.get('Barriers'):
                        self.updatePosition(nextNode)

                #down
                elif event.key == pygame.K_DOWN:
                    nextNode = [self.row, self.col + 1]

                    if self.grid.getGrid()[nextNode[0]][nextNode[1]] not in self.characters.get('Barriers'):
                        self.updatePosition(nextNode)

                #left
                elif event.key == pygame.K_LEFT:
                    nextNode = [self.row - 1, self.col]

                    if self.grid.getGrid()[nextNode[0]][nextNode[1]] not in self.characters.get('Barriers'):
                        self.updatePosition(nextNode)

                #right
                elif event.key == pygame.K_RIGHT:
                    nextNode = [self.row + 1, self.col]

                    if self.grid.getGrid()[nextNode[0]][nextNode[1]] not in self.characters.get('Barriers'):
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
