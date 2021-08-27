# from sprites import *
from config import *
from algorithms import *
import sys

class NPC():
    def __init__(self, grid, node):

        self.grid = grid
        self.node = node
        self.path = []
        self.state = "stay"

    def updateGrid(self, grid):
        self.grid = grid

    def update(self):

        if(h(ENEMY[0].getNode().get_pos(), PLAYER[0].getNode().get_pos()) < 10) and (self.state == 'stay'):
            for row in self.grid.getGrid():
                for node in row:
                    node.update_neighbors(self.grid.getGrid())

            self.path = algorithm(self.grid.getGrid(), self.node, PLAYER[0].getNode())
            self.state = 'come'

        elif (h(ENEMY[0].getNode().get_pos(), PLAYER[0].getNode().get_pos()) < 5) and (self.state == 'come'):

            self.state = 'stay'

        elif self.state == 'come':

            self.movement()



        elif len(self.path) == 0:
            self.state = 'stay'

    def getNode(self):
        return self.node

    def movement(self):
        if len(self.path) == 0:
            self.state = 'stay'
        else:
            self.node.reset()
            # get node

            self.node = self.path.pop()
            self.node.make_NPC()


    def updatePath(self, path):
        print(path)
        self.path = path