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
        self.animalState = 'stay'
        self.direction = 0
        self.color = BLUE
        self.grid = grid



    def toggleState(self):
        if self.animalState == 'stay':
            self.animalState = 'follow'
            self.come(PLAYER[0])
        else:
            self.animalState = 'stay'
            self.path = []

    def get_sprite(self, x, y, width, height):

        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))

        return sprite


    def update(self):


        # animal in stay state do nothing

        if self.animalState == 'stay':
            return

        # animal is still following path
        elif len(self.path) > 0:
            self.movement()

        elif ((h(self.get_pos(), PLAYER[0].get_pos()) < 10) and
              (h(self.get_pos(), PLAYER[0].get_pos()) > 5) and
              (self.animalState == 'follow')):
            self.come(PLAYER[0])
            #self.movement()




        self.rect.x = self.pos.x
        self.rect.y = self.pos.y



    def movement(self):

        if len(self.path) == 0:
            self.path = []

        else:

            self.node = self.path.pop()

            self.updatePosition(self.node.get_pos())



    def come(self, toNode):

        for row in self.grid.getGrid():
            for node in row:
                node.update_neighbors(self.grid.getGrid())

        self.path = algorithm(self.grid.getGrid(), self.grid.getGrid()[self.row][self.col], self.grid.getGrid()[toNode.row][toNode.col])
