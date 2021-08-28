# from sprites import *
import pygame
from config import *
from algorithms import *
from Node import *
import sys

'''
this class runs player controls
all inputs from user are handled by this class
'''
class Player(Node):
    def __init__(self, grid, row, col, width, total_rows, spriteSheet):

        Node.__init__(self, row, col, width, total_rows, spriteSheet)
        #sprite layer
        self._layer = 2
        self.image = self.createSprite(spriteSheet, 3, 2, width, width)
        self.grid = grid

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

                    if self.grid.getGrid()[nextNode[0]][nextNode[1]] not in BARRIER:
                        self.updatePosition(nextNode)

                #down
                elif event.key == pygame.K_DOWN:
                    nextNode = [self.row, self.col + 1]

                    if self.grid.getGrid()[nextNode[0]][nextNode[1]] not in BARRIER:
                        self.updatePosition(nextNode)

                #left
                elif event.key == pygame.K_LEFT:
                    nextNode = [self.row - 1, self.col]

                    if self.grid.getGrid()[nextNode[0]][nextNode[1]] not in BARRIER:
                        self.updatePosition(nextNode)

                #right
                elif event.key == pygame.K_RIGHT:
                    nextNode = [self.row + 1, self.col]

                    if self.grid.getGrid()[nextNode[0]][nextNode[1]] not in BARRIER:
                        self.updatePosition(nextNode)

                #space
                elif event.key == pygame.K_SPACE:
                    for dog in ENEMY:
                        dog.toggleFollowState()

                elif event.key == pygame.K_LCTRL:
                    for dog in ENEMY:
                        dog.makeFleeState()


                    # create sphere of influence
                    '''
                    for i in getGridSquare(self.node.get_pos(), 4, self.grid.getGrid()):
                        for j in i:
                            if j.get_color() == WHITE:
                                print(j)
                                j.make_light_blue()
                                '''
