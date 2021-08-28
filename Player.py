# from sprites import *
import pygame

from config import *
from algorithms import *
from Node import *
import sys

class Player(Node):
    def __init__(self, grid, row, col, width, total_rows, spriteSheet):

        Node.__init__(self, row, col, width, total_rows, spriteSheet)
        self._layer = 2
        self.image = self.createSprite(spriteSheet, 3, 2, width, width)

        self.grid = grid

    def update(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    nextNode = [self.row, self.col - 1]

                    if self.grid.getGrid()[nextNode[0]][nextNode[1]] not in BARRIER:
                        # update grid
                        # update player position
                        self.updatePosition(nextNode)
                        # update node

                elif event.key == pygame.K_DOWN:
                    nextNode = [self.row, self.col + 1]

                    if self.grid.getGrid()[nextNode[0]][nextNode[1]] not in BARRIER:
                        # update players previous position
                        # update player position
                        self.updatePosition(nextNode)
                        # update node


                elif event.key == pygame.K_LEFT:
                    nextNode = [self.row - 1, self.col]

                    if self.grid.getGrid()[nextNode[0]][nextNode[1]] not in BARRIER:
                        # update players previous position
                        # update player position
                        self.updatePosition(nextNode)
                        # update node


                elif event.key == pygame.K_RIGHT:
                    nextNode = [self.row + 1, self.col]

                    if self.grid.getGrid()[nextNode[0]][nextNode[1]] not in BARRIER:
                        # update players previous position
                        # update player position
                        self.updatePosition(nextNode)
                        # update node

                elif event.key == pygame.K_SPACE:
                    for dog in ENEMY:
                        dog.toggleState()


                    # create sphere of influence
                    '''
                    for i in getGridSquare(self.node.get_pos(), 4, self.grid.getGrid()):
                        for j in i:
                            if j.get_color() == WHITE:
                                print(j)
                                j.make_light_blue()
                                '''
