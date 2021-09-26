from Squirrel import *
from Bread import *
class Duck(Squirrel):

    def __init__(self, row, col, width, gameData):

        Animal.__init__(self, row, col, width, gameData.gameGrid, gameData.spriteSets.get('Duck'),
                        gameData.spriteGroup, gameData.characters)
        self.animalState = 'sniff'
        self.barriers = ['Trees', 'Barriers']
        self.characterFlee = ['Dogs']
        self.characterFood = ['Bread']
        self.bread = None
        self.items = []

    def update(self):
        self.coolDownTimer = self.coolDownTimer - 1
        if self.animalState == 'sniff':
            self.sniffState()

        elif self.animalState == 'go towards water':
            self.goTowardsWater()

        elif self.animalState == 'hide in water':
            self.hideInWaterState()

        elif self.animalState == 'go towards food':
            self.goTowardsFoodState()

        # update rectangle of sprite, x,y refers to upper left corner of sprite box
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

    def sniffState(self):
        #if person is close by change state to go towards tree
        if self.checkEnemyClose(5):
            self.animalState = 'go towards water'
            self.stateReset()

        elif self.checkFoodClose(4):
            self.animalState ='go towards food'
            self.stateReset()

        elif not self.checkCloseToWater(self):
            self.animalState = 'go towards water'
            self.stateReset()

        elif self.coolDownTimer <= -40:
            self.randomMove()
            self.movement()
            self.coolDownTimer = self.coolDown

    def goTowardsFoodState(self):
        if not self.checkFoodClose(5):
            self.animalState = 'sniff'
            self.stateReset()

        # if there are still spaces to move in the path - then move
        elif len(self.path) > 0 and self.coolDownTimer <= 0:
            self.coolDownTimer = self.coolDown
            self.movement()

        # create path
        elif len(self.path) <= 0:

            bestFood = self.bread
            for item in self.characters.get('Items'):
                if isinstance(item, Bread) and h(item.get_pos(), self.get_pos()) < h(bestFood.get_pos(), self.get_pos()):
                    bestFood = item

            if bestFood.get_pos() == self.get_pos():
                self.pickUp()
                self.animalState = 'sniff'
                self.stateReset()

            else:
                self._layer = 0
                self.come(bestFood)

    def checkPlayerClose(self):

        playerClose = False


        if h(self.get_pos(), self.characters.get('Player').get_pos()) < 5 and self.checkCloseToWater(self.characters.get('Player')):
            playerClose = True

        return playerClose


    def checkFoodClose(self, distance):

        foodClose = False
        for foodType in self.characterFood:
            for item in self.characters.get('Items'):
                if (isinstance(item, Bread) and h(self.get_pos(), item.get_pos()) < distance):
                    foodClose = True
                    self.bread = item

        return foodClose

    def checkCloseToWater(self, node):

        waterClose = False

        for water in self.characters.get('Water'):
            if ((h(node.get_pos(), water.get_pos()) < 4)):
                waterClose = True

        return waterClose

    def randomMove(self):

        self.direction = randrange(4)

        if self.direction == 0:
            nextNode = self.grid.getGrid()[self.row][self.col - 1]
            #iterate through trees if squirrel is close
            for i in self.characters.get('Water'):
                if not self.checkNodes((self.row, self.col - 1)) and h(nextNode.get_pos(), i.get_pos()) < 3:
                    self.path.append(nextNode)

        elif self.direction == 1:

            nextNode = self.grid.getGrid()[self.row][self.col + 1]

            for i in self.characters.get('Water'):
                if not self.checkNodes((self.row, self.col + 1)) and h(nextNode.get_pos(), i.get_pos()) < 3:
                    self.path.append(nextNode)

        elif self.direction == 2:

            nextNode = self.grid.getGrid()[self.row - 1][self.col]

            for i in self.characters.get('Water'):
                if not self.checkNodes((self.row - 1, self.col)) and h(nextNode.get_pos(), i.get_pos()) < 3:
                    self.path.append(nextNode)

        elif self.direction == 3:
            nextNode = self.grid.getGrid()[self.row + 1][self.col]

            for i in self.characters.get('Water'):
                if not self.checkNodes((self.row + 1, self.col)) and h(nextNode.get_pos(), i.get_pos()) < 3:
                    self.path.append(nextNode)

    def randomMoveWater(self):

        self.direction = randrange(4)

        if self.direction == 0:
            nextNode = self.grid.getGrid()[self.row][self.col - 1]

        elif self.direction == 1:

            nextNode = self.grid.getGrid()[self.row][self.col + 1]

        elif self.direction == 2:

            nextNode = self.grid.getGrid()[self.row - 1][self.col]

        elif self.direction == 3:
            nextNode = self.grid.getGrid()[self.row + 1][self.col]

        for i in self.characters.get('Water'):
            if i.get_pos() == nextNode.get_pos():
                self.path.append(nextNode)

    def goTowardsWater(self):
        if not self.checkEnemyClose(5) and self.checkCloseToWater(self):
            self.animalState = 'sniff'
            self.stateReset()
            self._layer = 3


        # if there are still spaces to move in the path - then move
        elif len(self.path) > 0 and self.coolDownTimer <= 0:
            self.coolDownTimer = self.coolDown
            self.movement()

        # create path
        elif len(self.path) <= 0:

            bestTree = self.characters.get('Water')[0]
            for tree in self.characters.get('Water'):
                if h(tree.get_pos(), self.get_pos()) < h(bestTree.get_pos(), self.get_pos()):
                    bestTree = tree

            if bestTree.get_pos() == self.get_pos():
                #move squirrel up one square to top of tree
                #self.path = [self.grid.getGrid()[self.row][self.col - 1]]
                self.movement()
                self.animalState = 'hide in water'
                self.stateReset()
                self._layer = 6

            else:
                self._layer = 0
                self.come(bestTree)
                print('hello')

    def hideInWaterState(self):

        #chck if player is gone and enough time has passed
        if not self.checkEnemyClose(6) and self.coolDownTimer < -20:
            self.animalState = 'sniff'
            self.stateReset()
            self._layer = 3

        #if player is still there reset cooldown timer
        elif self.checkEnemyClose(6) and self.coolDownTimer <= -40:
            self.randomMoveWater()
            self.movement()
            self.coolDownTimer = self.coolDown
            self._layer = 6
