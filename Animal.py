from Node import *
# from sprites import *
from config import *
from algorithms import *
import sys
from random import randrange
from BasicSprite import *

'''
basic animal
AI can follow player, stay and flee
animal is set to stay state at creation

States:
stay: do nothing
follow: if player is over 5 paces away move to the player
flee: if player is 5 paces away, move away
'''
class Animal(BasicSprite):
    def __init__(self, row, col, width, total_rows, grid, spriteSheet, spriteGroup, characters):

        BasicSprite.__init__(self, row, col, width, total_rows, spriteSheet)
        self._layer = 3


        self.path = []
        self.animalState = 'stay'
        self.direction = 0
        self.grid = grid
        self.playerCommand = ''
        self.spriteGroup = spriteGroup
        self.characters = characters
        self.coolDown = 5
        self.coolDownTimer = 5
        self.animationCount = 0
        self.spriteSets = self.createSpriteSheets(spriteSheet)
        self.animationCells = []
        self.movementSprite = 'Left'
        self.image = pygame.transform.scale(self.createSprite(spriteSheet, 2, 2, 26, 35, (55,99,77)), (40, 50))

        self.barriers = ['Barriers', 'Trees']

    def updateSprite(self):
        if self.animationCount > len(self.spriteSets.get(self.movementSprite)) - 1:
            self.animationCount = 0

        self.image = self.spriteSets.get(self.movementSprite)[self.animationCount]
        self.animationCount = self.animationCount + 1


    def animateAnimals(self):
        if len(self.animationCells) > 0:
            self.image = self.animationCells.pop()

    def createSpriteSheets(self, spriteSheet):

        animations = {}
        up = []
        up.append(pygame.transform.scale(self.createSprite(spriteSheet, 55, 40, 26, 35, (55,99,77)), (40, 50)))
        up.append(pygame.transform.scale(self.createSprite(spriteSheet, 123, 39, 26, 35, (55,99,77)), (40, 50)))

        right = []

        right.append(pygame.transform.scale(self.createSprite(spriteSheet, 42, 5, 26, 35, (55, 99, 77)), (40, 50)))
        right.append(pygame.transform.scale(self.createSprite(spriteSheet, 63, 2, 26, 35, (55, 99, 77)), (40, 50)))
        right.append(pygame.transform.scale(self.createSprite(spriteSheet, 100, 4, 26, 35, (55, 99, 77)), (40, 50)))
        right.append(pygame.transform.scale(self.createSprite(spriteSheet, 127, 5, 26, 35, (55, 99, 77)), (40, 50)))
        right.append(pygame.transform.scale(self.createSprite(spriteSheet, 150, 3, 26, 35, (55, 99, 77)), (40, 50)))
        right.append(pygame.transform.scale(self.createSprite(spriteSheet, 179, 5, 26, 35, (55, 99, 77)), (40, 50)))

        left = []

        left.append(pygame.transform.flip(pygame.transform.scale(self.createSprite(spriteSheet, 42, 5, 26, 35, (55, 99, 77)), (40, 50)), True, False))
        left.append(pygame.transform.flip(pygame.transform.scale(self.createSprite(spriteSheet, 63, 2, 26, 35, (55, 99, 77)), (40, 50)), True, False))
        left.append(pygame.transform.flip(pygame.transform.scale(self.createSprite(spriteSheet, 100, 4, 26, 35, (55, 99, 77)), (40, 50)), True, False))
        left.append(pygame.transform.flip(pygame.transform.scale(self.createSprite(spriteSheet, 127, 5, 26, 35, (55, 99, 77)), (40, 50)), True, False))
        left.append(pygame.transform.flip(pygame.transform.scale(self.createSprite(spriteSheet, 150, 3, 26, 35, (55, 99, 77)), (40, 50)), True, False))
        left.append(pygame.transform.flip(pygame.transform.scale(self.createSprite(spriteSheet, 179, 5, 26, 35, (55, 99, 77)), (40, 50)), True, False))

        down = []
        down.append(pygame.transform.scale(self.createSprite(spriteSheet, 55, 80, 26, 35, (55, 99, 77)), (40, 50)))
        down.append(pygame.transform.scale(self.createSprite(spriteSheet, 79, 84, 26, 35, (55, 99, 77)), (40, 50)))
        down.append(pygame.transform.scale(self.createSprite(spriteSheet, 102, 81, 26, 35, (55, 99, 77)), (40, 50)))
        down.append(pygame.transform.scale(self.createSprite(spriteSheet, 125, 80, 26, 35, (55, 99, 77)), (40, 50)))
        down.append(pygame.transform.scale(self.createSprite(spriteSheet, 148, 83, 26, 35, (55, 99, 77)), (40, 50)))
        down.append(pygame.transform.scale(self.createSprite(spriteSheet, 171, 81, 26, 35, (55, 99, 77)), (40, 50)))

        stayUp =[]
        stayUp.append(pygame.transform.scale(self.createSprite(spriteSheet, 3, 41, 26, 35, (55, 99, 77)), (40, 50)))

        stayDown = []
        stayDown.append(pygame.transform.scale(self.createSprite(spriteSheet, 2, 79, 26, 35, (55, 99, 77)), (40, 50)))

        stayRight = []
        stayRight.append(pygame.transform.scale(self.createSprite(spriteSheet, 3, 3, 26, 35, (55, 99, 77)), (40, 50)))

        stayLeft = []
        stayLeft.append(pygame.transform.scale(self.createSprite(spriteSheet, 3, 3, 26, 35, (55, 99, 77)), (40, 50)))

        throw = []
        throw.append(pygame.transform.scale(self.createSprite(spriteSheet, 89, 576, 26, 35, (55, 99, 77)), (40, 50)))
        throw.append(pygame.transform.scale(self.createSprite(spriteSheet, 125, 580, 26, 35, (55, 99, 77)), (40, 50)))
        throw.append(pygame.transform.scale(self.createSprite(spriteSheet, 169, 578, 26, 35, (55, 99, 77)), (40, 50)))
        throw.append(pygame.transform.scale(self.createSprite(spriteSheet, 201, 577, 26, 35, (55, 99, 77)), (40, 50)))

        animations.update({'Up': up})
        animations.update({'Right': right})
        animations.update({'Left': left})
        animations.update({'Down': down})
        animations.update({'Stay Up': stayUp})
        animations.update({'Stay Down': stayDown})
        animations.update({'Stay Right': stayRight})
        animations.update({'Stay Left': stayLeft})
        animations.update({'Throw': throw})

        return animations

    def makeFleeState(self):

        self.animalState = 'flee'

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

            elif self.playerCommand == 'stay':
                self.animalState = 'stay'
                self.playerCommand = ''

            #else if animal is far enough from player do nothing
            elif (h(self.get_pos(), self.characters['Player'].get_pos()) > 5):
                self.path = []

            #else if animal still has places to move move
            elif len(self.path) > 0:
                self.movement()

            #else if player is too close find a place to move to
            elif (h(self.get_pos(), self.characters['Player'].get_pos()) < 5):
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
            elif h(self.get_pos(), self.characters['Player'].get_pos()) < 4:
                self.path = []

            #if there are still spaces to move in the path - then move
            elif len(self.path) > 0:
                self.movement()

            #if player is over 4 spaces away from animal then create a path to player
            elif h(self.get_pos(), self.characters['Player'].get_pos())  > 4:
                self.come(self.characters['Player'])

        #update rectangle of sprite, x,y refers to upper left corner of sprite box
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

    def movement(self):
        '''
        moves animal one step along path
        '''

        if len(self.path) > 0:
            self.node = self.path.pop()
            self.updatePosition(self.node.get_pos())

    def come(self, toNode):
        '''
        call pathfinding algorithm and update animal path
        :Node toNode: Node you want animal to pathfind to
        '''

        for row in self.grid.getGrid():
            for node in row:
                node.update_neighbors(self.grid.getGrid(), self.barriers)

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
        for row in getGridSquare(self.get_pos(), 5, self.grid.getGrid()):

            for node in row:

                if not self.checkNodes(node.get_pos()) and node.get_pos() != self.characters.get('Player').get_pos():
                    #if distance of node is better update
                    if h(node.get_pos(), self.characters.get('Player').get_pos()) > bestDist:

                        bestNode = node
                        bestDist = h(node.get_pos(), self.characters.get('Player').get_pos())

        #a good node has been found update animals path to it
        if bestNode != None:
            self.come(bestNode)


    def randomMove(self):


        self.direction = randrange(4)

        if self.direction == 0:
            #nextNode = self.grid.getGrid()[self.get_pos()[0]][self.get_pos()[1] - 1]
            nextNode = self.grid.getGrid()[self.row][self.col - 1]

            if not self.checkNodes((self.row, self.col - 1)):
                self.path.append(nextNode)

        elif self.direction == 1:
            nextNode = self.grid.getGrid()[self.row][self.col + 1]

            if not self.checkNodes((self.row, self.col + 1)):
                self.path.append(nextNode)

        elif self.direction == 2:

            nextNode = self.grid.getGrid()[self.row - 1][self.col]

            if not self.checkNodes((self.row - 1, self.col)):
                self.path.append(nextNode)

        elif self.direction == 3:
            nextNode = self.grid.getGrid()[self.row + 1][self.col]

            if not self.checkNodes((self.row + 1, self.col)):
                self.path.append(nextNode)

    def pickUp(self):
        for i, item in enumerate(self.characters.get('Items')):
            if h(item.get_pos(), self.get_pos()) < 2.5:
                #add item to dictionary
                self.items.append(item)

                # remove from interactive characters item list
                self.removeCharacter('Items', i)
                # remove item sprite from sprite group
                item.kill()

    def dropItem(self, node, item):
        #update items position
        item.updatePosition(node.get_pos())
        self.spriteGroup.add(item)

        # add item sprite back into the game
        self.spriteGroup.add(item)

        # add the character back into the game
        self.addCharcter('Items', item)

    def removeCharacter(self, characterType, position):
        tempArray = self.characters.get(characterType)
        tempArray.pop(position)
        self.characters.update({characterType: tempArray})



    def addCharcter(self, characterType, character):
        #get the specific array from the interactive characters dictionary
        tempArray = self.characters.get(characterType)

        #add character to array
        tempArray.append(character)
        #update characters dictionary
        self.characters.update({characterType: tempArray})

    def checkNodes(self, position):

        nodeState = False

        for barrierType in self.barriers:
            for barrier in self.characters.get(barrierType):
                if barrier.get_pos() == position:
                    nodeState = True
                    break

        return nodeState

    def stateReset(self):
        '''resets path and player command when transfering between states'''

        self.path = []

    def updatePosition(self, position):
        '''
        :tuple position: x, y
        :return:
        '''

        #update sprites
        #up
        if self.col - 1 == position[1]:
            self.movementSprite = 'Up'


        #down
        elif self.col + 1 == position[1]:
            self.movementSprite = 'Down'


        #left
        elif self.row - 1 == position[0]:
            self.movementSprite = 'Left'


        #right
        elif self.row + 1 == position[0]:
            self.movementSprite = 'Right'


        # update position on game grid
        self.row = position[0]
        self.col = position[1]
        # set position of upper left of sprites rectangle
        self.pos.x = position[0] * 30
        self.pos.y = position[1] * 30

        # update sprite rectangle
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        self.updateSprite()