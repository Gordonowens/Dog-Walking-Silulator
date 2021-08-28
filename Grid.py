'''
this holds the game grid for pathfinding
the grid is expeced to hold only barrier and non barrier nodes
'''
class Grid():

    def __init__(self, grid):

        self.grid = grid

    def getGrid(self):
        return self.grid


    def setGrid(self, grid):
        self.grid = grid