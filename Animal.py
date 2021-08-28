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
        self.playerCommand = ''


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
        this function handles moving the animal between states
        no other function can change the animal's state
        '''

        #do nothing if in stay state
        if self.animalState == 'stay':
            if self.playerCommand == 'flee':
                self.animalState = 'flee'
                self.playerCommand = ''

            elif self.playerCommand == 'follow':
                self.animalState = 'follow'
                self.playerCommand = ''

            elif self.playerCommand == 'stay':
                self.animalState = 'stay'
                self.playerCommand = ''

        elif self.animalState == 'flee':
            #change state if appropriote
            if self.playerCommand == 'follow':
                self.animalState = 'follow'
                self.playerCommand = ''

            #else if animal is far enough from player do nothing
            elif (h(self.get_pos(), PLAYER[0].get_pos()) > 5):
                self.path = []

            #else if animal still has places to move move
            elif len(self.path) > 0:
                self.movement()

            #else if player is too close find a place to move to
            elif (h(self.get_pos(), PLAYER[0].get_pos()) < 5):
                self.runAway()

        elif self.animalState == 'follow':
            #change state if appropriote
            if self.playerCommand == 'stay':
                self.animalState = 'stay'
                self.playerCommand = ''

            # change state if appropriote
            elif self.playerCommand == 'flee':
                self.animalState = 'flee'
                self.playerCommand = ''

            #if player is within 4 spaces of animal do nothing
            elif h(self.get_pos(), PLAYER[0].get_pos()) < 4:
                self.path = []

            #if there are still spaces to move in the path - then move
            elif len(self.path) > 0:
                self.movement()

            #if player is over 4 spaces away from animal then create a path to player
            elif h(self.get_pos(), PLAYER[0].get_pos())  > 4:
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