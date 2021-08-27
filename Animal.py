from Node import *
# from sprites import *
from config import *
from algorithms import *
import sys
from random import randrange

class Animal(Node):
    def __init__(self, row, col, width, total_rows, grid, spriteSheet):

        self._layer = 3
        Node.__init__(self, row, col, width, total_rows, spriteSheet)
        self._layer = 3
        self.image = self.createSprite(spriteSheet, 26, 101, 26, 35)
        self.path = []
        self.animalState = 'come'
        self.direction = 0
        self.color = BLUE
        self.grid = grid

    def toggleState(self):
        if self.animalState == 'stay':

            self.animalState = 'come'
        #else:
            #self.animalState = 'stay'
            #self.path = []

    def get_sprite(self, x, y, width, height):

        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))

        return sprite

    def randomMove(self):


        self.direction = randrange(4)

        if self.direction == 0:
            nextNode = self.grid.getGrid()[self.row][self.col - 1]
            if nextNode not in BARRIER:

                self.updateRect()

        elif self.direction == 1:
            nextNode = self.grid.getGrid()[self.row][self.col + 1]

            if nextNode not in BARRIER:
                pass
                #self.col = self.col + 1
                #self.updateRect()

        elif self.direction == 2:

            nextNode = self.grid.getGrid()[self.row - 1][self.col]

            if nextNode not in BARRIER:
                pass
                #self.row = self.row - 1
                #self.updateRect()

        elif self.direction == 3:
            nextNode = self.grid.getGrid()[self.row + 1][self.col]

            if nextNode not in BARRIER:
                pass
                #self.row = self.row + 1
                #self.updateRect()

    def update(self):

        #print(self.animalState)
        # animal in stay state do nothing
        if self.animalState == 'stay':
            return

        # animal is still following path to player
        elif len(self.path) > 1 and self.animalState == 'come':

            self.movement()

        elif len(self.path) == 0 and self.animalState == 'come':
            self.come(PLAYER[0])

        else:
            self.animalState = 'stay'
            self.path = []

        self.rect.x = self.pos.x
        self.rect.y = self.pos.y



    def movement(self):
        #print(len(self.path))
        if len(self.path) == 1:
            self.state = 'stay'
            self.path = []

        else:

            self.node = self.path.pop()

            self.updatePosition(self.node.get_pos())



    def come(self, toNode):

        for row in self.grid.getGrid():
            for node in row:
                node.update_neighbors(self.grid.getGrid())
                #print(node.neighbors)

        #time.sleep()
        #print(self.get_pos(), toNode.get_pos())
        #print(self.grid.getGrid())

        self.path = algorithm(self.grid.getGrid(), self.grid.getGrid()[self.row][self.col], self.grid.getGrid()[toNode.row][toNode.col])
        self.state = 'come'

        #print(self.path)
