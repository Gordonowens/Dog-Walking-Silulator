# from sprites import *
from config import *
from algorithms import *
import sys
from random import randrange

class NPC():
    def __init__(self, grid, node):

        self.grid = grid
        self.node = node
        self.path = []
        self.state = "stay"
        self.direction = 0

    def updateGrid(self, grid):
        self.grid = grid

    def randomMove(self, timeChange):

        if GAMETIME.get_time() % timeChange == 0:
            self.direction = randrange(4)
            print(self.direction)

        if self.direction == 0:
            nextNode = self.grid.getGrid()[self.node.get_pos()[0]][self.node.get_pos()[1] - 1]
            if nextNode not in BARRIER:
                self.updateNode(nextNode)

        elif self.direction == 1:
            nextNode = self.grid.getGrid()[self.node.get_pos()[0]][self.node.get_pos()[1] + 1]

            if nextNode not in BARRIER:
                self.updateNode(nextNode)

        elif self.direction == 2:

            nextNode = self.grid.getGrid()[self.node.get_pos()[0] - 1][self.node.get_pos()[1]]

            if nextNode not in BARRIER:
                self.updateNode(nextNode)

        elif self.direction == 3:
            nextNode = self.grid.getGrid()[self.node.get_pos()[0] + 1][self.node.get_pos()[1]]

            if nextNode not in BARRIER:
                self.updateNode(nextNode)

    def come(self, toNode):
        for row in self.grid.getGrid():
            for node in row:
                node.update_neighbors(self.grid.getGrid())

        self.path = algorithm(self.grid.getGrid(), self.node, toNode)
        self.state = 'come'



    def update(self):

        #animal in stay state do nothing
        if self.state == 'stay':
            return

        #animal has just been asked to come
        elif self.state == 'come' and len(self.path) == 0:
            self.come()

        #animal is still following path to player
        elif len(self.path) != 0 and self.state == 'come':
           self.movement()



    def movement(self):
        if len(self.path) == 0:
            self.state = 'stay'
        else:
            self.node.reset()
            # get node

            self.node = self.path.pop()
            self.node.make_NPC()

    def updateNode(self, nextNode):
        self.node.reset()
        # get node
        self.node = nextNode
        self.node.make_player()

    def updatePath(self, path):
        print(path)
        self.path = path