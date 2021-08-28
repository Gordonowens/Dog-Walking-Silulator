from Node import *
# from sprites import *
from config import *
from algorithms import *
import sys
from random import randrange

'''
basic animal
AI can follow player, stay and flee
animal is set to stay state at creation

States:
stay: do nothing
follow: if player is over 5 paces away move to the player
flee: if player is 5 paces away, move away
'''
class Animal(Node):
    def __init__(self, row, col, width, total_rows, grid, spriteSheet):

        Node.__init__(self, row, col, width, total_rows, spriteSheet)
        self._layer = 3
        self.image = self.createSprite(spriteSheet, 26, 101, 26, 35)

        #this stores path calculated by pathfinding algorithm
        #[end, node, node, start]
        self.path = []
        self.animalState = 'stay'
        self.direction = 0
        self.grid = grid


    def makeFleeState(self):

        self.animalState = 'flee'


    def toggleFollowState(self):
        '''
        when called will toggle between stay and follow
        :
        '''
        if self.animalState == 'stay':
            self.animalState = 'follow'
            self.come(PLAYER[0])
        else:
            self.animalState = 'stay'
            self.path = []

    def get_sprite(self, x, y, width, height):
        '''
        creates sprite surface and blits the image from sprite sheet onto it
        :param x:
        :param y:
        :param width:
        :param height:
        '''

        #create surface
        sprite = pygame.Surface([width, height])
        #blit image from sprite sheet onto surface
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))

        return sprite


    def update(self):
        '''
        handles
        '''

        #do nothing if in stay state
        if self.animalState == 'stay':
            return

        elif self.animalState == 'flee' and len(self.path) == 0:
            if (h(self.get_pos(), PLAYER[0].get_pos()) < 5):
                self.runAway()
            else:
                print('stay')

        # animal is still following path
        elif len(self.path) > 0:
            self.movement()

        elif ((h(self.get_pos(), PLAYER[0].get_pos()) < 10) and
              (h(self.get_pos(), PLAYER[0].get_pos()) > 5) and
              (self.animalState == 'follow')):
            self.come(PLAYER[0])

        #update rectangle of sprite, x,y refers to upper left corner of sprite box
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

    def movement(self):
        '''
        moves animal one step along path
        '''
        if len(self.path) == 0:
            return

        else:
            self.node = self.path.pop()
            self.updatePosition(self.node.get_pos())



    def come(self, toNode):
        '''
        call pathfinding algorithm and update animal path
        :Node toNode: Node you want animal to pathfind to
        '''

        for row in self.grid.getGrid():
            for node in row:
                node.update_neighbors(self.grid.getGrid())

        self.path = algorithm(self.grid.getGrid(), self.grid.getGrid()[self.row][self.col], self.grid.getGrid()[toNode.row][toNode.col])

    def runAway(self):
        '''
        slices out a grid 5 * 5 from game grid and tries to find a path to a node
        8 spaces or more from the player

        '''
        #get sphere of influence
        bestNode = None
        bestDist = 8

        #iterate through sliced out grid
        for i in getGridSquare(self.get_pos(), 5, self.grid.getGrid()):

            for j in i:
                if j not in BARRIER and j not in PLAYER:
                    #if distance of node is better update
                    if h(j.get_pos(), PLAYER[0].get_pos()) > bestDist:

                        bestNode = j
                        bestDist = h(j.get_pos(), PLAYER[0].get_pos())

        #a good node has been found update animals path to it
        if bestNode != None:
            self.come(bestNode)