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
        if self.checkEnemyClose(8):
            self.animalState = 'go towards water'
            self.stateReset()

        elif self.checkFoodClose(4):
            self.animalState ='go towards food'
            self.stateReset()

        elif not self.checkCloseToWater(self):
            self.animalState = 'go towards water'
            self.stateReset()

        elif self.coolDownTimer <= -60:
            self.randomMove()
            self.movement()
            self.coolDownTimer = self.coolDown

    def goTowardsFoodState(self):

        #enemy is close go to water
        if self.checkEnemyClose(5):
            self.animalState = 'go towards water'
            self.stateReset()

        #no food close change state
        elif not self.checkFoodClose(5):
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

            #duck is ontop of food
            if bestFood.get_pos() == self.get_pos():
                self.pickUp()
                self.animalState = 'sniff'
                self.stateReset()

            else:
                self._layer = 0
                self.come(bestFood)

    def checkFoodClose(self, distance):
        '''

        :param distance: int distance duck will go for food
        :return: bool false if no food close, True if food is close
        '''

        foodClose = False
        #iterate over items to find food
        for item in self.characters.get('Items'):
            #if food is close foodClose is now True
            if (isinstance(item, Bread) and h(self.get_pos(), item.get_pos()) < distance):
                foodClose = True
                self.bread = item

        return foodClose

    def checkCloseToWater(self, node):
        '''
        will check if water is 4 spaces close
        :param node: node that is check if water is close
        :return: True if water is close, false if water not close
        '''

        waterClose = False

        #iterate over water nodes
        for water in self.characters.get('Water'):
            #if water is less than 4 spaces close, Water close not true
            if ((h(node.get_pos(), water.get_pos()) < 4)):
                waterClose = True

        return waterClose

    def randomMove(self):

        #get randome number
        self.direction = randrange(4)

        #up
        if self.direction == 0:

            nextNode = self.grid.getGrid()[self.row][self.col - 1]
            #iterate through water and check if close
            for i in self.characters.get('Water'):
                if not self.checkNodes((self.row, self.col - 1)) and h(nextNode.get_pos(), i.get_pos()) < 3:
                    self.path.append(nextNode)

        #down
        elif self.direction == 1:
            nextNode = self.grid.getGrid()[self.row][self.col + 1]
            # iterate through water and check if close
            for i in self.characters.get('Water'):
                if not self.checkNodes((self.row, self.col + 1)) and h(nextNode.get_pos(), i.get_pos()) < 3:
                    self.path.append(nextNode)

        #left
        elif self.direction == 2:

            nextNode = self.grid.getGrid()[self.row - 1][self.col]
            # iterate through water and check if close
            for i in self.characters.get('Water'):
                if not self.checkNodes((self.row - 1, self.col)) and h(nextNode.get_pos(), i.get_pos()) < 3:
                    self.path.append(nextNode)

        #right
        elif self.direction == 3:
            nextNode = self.grid.getGrid()[self.row + 1][self.col]
            # iterate through water and check if close
            for i in self.characters.get('Water'):
                if not self.checkNodes((self.row + 1, self.col)) and h(nextNode.get_pos(), i.get_pos()) < 3:
                    self.path.append(nextNode)

    def randomMoveWater(self):
        '''
        duck will only random move on a water tile
        :return:
        '''

        self.direction = randrange(4)

        if self.direction == 0:
            nextNode = self.grid.getGrid()[self.row][self.col - 1]

        elif self.direction == 1:

            nextNode = self.grid.getGrid()[self.row][self.col + 1]

        elif self.direction == 2:

            nextNode = self.grid.getGrid()[self.row - 1][self.col]

        elif self.direction == 3:
            nextNode = self.grid.getGrid()[self.row + 1][self.col]

        #check if next node is water, update duck position if water
        for i in self.characters.get('Water'):
            if i.get_pos() == nextNode.get_pos():
                self.path.append(nextNode)

    def goTowardsWater(self):
        '''

        '''
        #if an enemy is not close and duck is close to water change state to sniff
        if not self.checkEnemyClose(8) and self.checkCloseToWater(self):
            self.animalState = 'sniff'
            self.stateReset()
            self._layer = 3


        # if there are still spaces to move in the path - then move
        elif len(self.path) > 0 and self.coolDownTimer <= 0:
            self.coolDownTimer = self.coolDown
            self.movement()

        # get closest water
        elif len(self.path) <= 0:

            #initially set best tree as first tree in list
            bestTree = self.characters.get('Water')[0]
            for tree in self.characters.get('Water'):
                #check if next water is better than best water. Update if better
                if h(tree.get_pos(), self.get_pos()) < h(bestTree.get_pos(), self.get_pos()):
                    bestTree = tree

            #if duck is in water update state to hide in water
            if bestTree.get_pos() == self.get_pos():
                self.movement()
                self.animalState = 'hide in water'
                self.stateReset()
                self._layer = 6

            #create path
            else:
                self._layer = 0
                self.come(bestTree)

    def hideInWaterState(self):

        #chck if player is gone and enough time has passed
        if not self.checkEnemyClose(10) and self.coolDownTimer < -20:
            self.animalState = 'sniff'
            self.stateReset()
            self._layer = 3

        #if player is still there reset cooldown timer
        elif self.checkEnemyClose(6) and self.coolDownTimer <= -40:
            self.randomMoveWater()
            self.movement()
            self.coolDownTimer = self.coolDown
            self._layer = 6
