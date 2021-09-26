from Dog import *

class Squirrel(Animal):

    def __init__(self, row, col, width, gameData):

        Animal.__init__(self, row, col, width, gameData.gameGrid, gameData.spriteSets.get('Squirrel'),
                        gameData.spriteGroup, gameData.characters)
        self.animalState = 'sniff'
        self.barriers = ['Trees', 'Barriers']
        self.characterFlee = ['Dogs']


    def update(self):
        self.coolDownTimer = self.coolDownTimer - 1
        if self.animalState == 'sniff':
            self.sniffState()

        elif self.animalState == 'go towards tree':
            self.goTowardsTree()

        elif self.animalState == 'hide in tree':
            self.hideInTreeState()

        # update rectangle of sprite, x,y refers to upper left corner of sprite box
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

    def goTowardsTree(self):
        if not self.checkEnemyClose(5):
            self.animalState = 'sniff'
            self.stateReset()
            self._layer = 3


        # if there are still spaces to move in the path - then move
        elif len(self.path) > 0 and self.coolDownTimer <= 0:
            self.coolDownTimer = self.coolDown
            self.movement()



        # create path
        elif len(self.path) <= 0:

            bestTree = self.characters.get('Trees')[0]
            for tree in self.characters.get('Trees'):
                if h(tree.get_pos(), self.get_pos()) < h(bestTree.get_pos(), self.get_pos()):
                    bestTree = tree

            if bestTree.get_pos() == self.get_pos():
                #move squirrel up one square to top of tree
                self.path = [self.grid.getGrid()[self.row][self.col - 1]]
                self.movement()
                self.animalState = 'hide in tree'
                self.stateReset()
                self._layer = 6

            else:
                self._layer = 0
                self.come(bestTree)

    def hideInTreeState(self):

        #chck if player is gone and enough time has passed
        if not self.checkEnemyClose(10) and self.coolDownTimer < -150:
            self.animalState = 'sniff'
            self.stateReset()
            self._layer = 3

        #if player is still there reset cooldown timer
        elif self.checkEnemyClose(10):
            self.coolDownTimer = self.coolDown
            self._layer = 6

    def sniffState(self):
        #if person is close by change state to go towards tree
        if self.checkEnemyClose(5):
            self.animalState = 'go towards tree'
            self.stateReset()

        elif self.coolDownTimer <= -25:
            self.randomMove()
            self.movement()
            self.coolDownTimer = self.coolDown

    def checkEnemyClose(self, distance):

        enemyClose = False
        for enemyType in self.characterFlee:
            for enemy in self.characters.get(enemyType):
                if ((h(self.get_pos(), enemy.get_pos()) < distance)):
                    enemyClose = True

        return enemyClose


    def randomMove(self):

        self.direction = randrange(4)

        if self.direction == 0:
            nextNode = self.grid.getGrid()[self.row][self.col - 1]
            #iterate through trees if squirrel is close
            for i in self.characters.get('Trees'):
                if not self.checkNodes((self.row, self.col - 1)) and h(nextNode.get_pos(), i.get_pos()) < 5:
                    self.path.append(nextNode)

        elif self.direction == 1:

            nextNode = self.grid.getGrid()[self.row][self.col + 1]

            for i in self.characters.get('Trees'):
                if not self.checkNodes((self.row, self.col + 1)) and h(nextNode.get_pos(), i.get_pos()) < 5:
                    self.path.append(nextNode)

        elif self.direction == 2:

            nextNode = self.grid.getGrid()[self.row - 1][self.col]

            for i in self.characters.get('Trees'):
                if not self.checkNodes((self.row - 1, self.col)) and h(nextNode.get_pos(), i.get_pos()) < 5:
                    self.path.append(nextNode)

        elif self.direction == 3:
            nextNode = self.grid.getGrid()[self.row + 1][self.col]

            for i in self.characters.get('Trees'):
                if not self.checkNodes((self.row + 1, self.col)) and h(nextNode.get_pos(), i.get_pos()) < 5:
                    self.path.append(nextNode)
