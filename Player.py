# from sprites import *
from config import *

class Player():
    def __init__(self, grid, node):

        self.grid = grid
        self.node = node

    def update(self):
        self.movement()

    def getNode(self):
        return self.node

    def movement(self):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.node.reset()
            #get node
            self.node = self.grid.getGrid()[self.node.get_pos()[0]][self.node.get_pos()[1] - 1]
            self.node.make_player()

        elif keys[pygame.K_DOWN]:
            self.node.reset()
            # get node

            self.node = self.grid.getGrid()[self.node.get_pos()[0]][self.node.get_pos()[1] + 1]
            self.node.make_player()

        elif keys[pygame.K_LEFT]:
            self.node.reset()
            # get node

            self.node = self.grid.getGrid()[self.node.get_pos()[0] - 1][self.node.get_pos()[1]]
            self.node.make_player()

        elif keys[pygame.K_RIGHT]:
            self.node.reset()
            # get node

            self.node = self.grid.getGrid()[self.node.get_pos()[0] + 1][self.node.get_pos()[1]]
            self.node.make_player()




