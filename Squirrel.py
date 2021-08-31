from Dog import *

class Squirrel(Animal):

    def __init__(self, row, col, width, total_rows, grid, spriteSheet, spriteGroup, characters):

        Animal.__init__(self, row, col, width, total_rows, grid, spriteSheet, spriteGroup, characters)
        self.image = self.createSprite(spriteSheet, 0, 0, width, width)
        self.animalState = 'sniff'


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
        if ((h(self.get_pos(), self.characters.get('Player').get_pos()) > 5)):
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
                self.animalState = 'hide in tree'
                self.stateReset()
                self._layer = 0

            else:
                self._layer = 0
                self.come(bestTree)

    def hideInTreeState(self):

        #chck if player is gone and enough time has passed
        if ((h(self.get_pos(), self.characters.get('Player').get_pos()) > 10) and self.coolDownTimer < -100):
            self.animalState = 'sniff'
            self.stateReset()
            self._layer = 3

        #if player is still there reset cooldown timer
        elif(h(self.get_pos(), self.characters.get('Player').get_pos()) < 10):
            self.coolDownTimer = self.coolDown

    def sniffState(self):
        #if person is close by change state to go towards tree
        if((h(self.get_pos(), self.characters.get('Player').get_pos()) < 5)):
            self.animalState = 'go towards tree'
            self.stateReset()

        elif self.coolDownTimer <= 0:
            self.randomMove()
            self.movement()
            self.coolDownTimer = self.coolDown

    def randomMove(self):

        self.direction = randrange(4)

        if self.direction == 0:
            nextNode = self.grid.getGrid()[self.row][self.col - 1]
            #iterate through trees if squirrel is close
            for i in self.characters.get('Trees'):
                if not self.checkNodes('Barriers', (self.row, self.col - 1)) and h(nextNode.get_pos(), i.get_pos()) < 5:
                    self.path.append(nextNode)

        elif self.direction == 1:

            nextNode = self.grid.getGrid()[self.row][self.col + 1]

            for i in self.characters.get('Trees'):
                if not self.checkNodes('Barriers', (self.row, self.col + 1)) and h(nextNode.get_pos(), i.get_pos()) < 5:
                    self.path.append(nextNode)

        elif self.direction == 2:

            nextNode = self.grid.getGrid()[self.row - 1][self.col]

            for i in self.characters.get('Trees'):
                if not self.checkNodes('Barriers', (self.row - 1, self.col)) and h(nextNode.get_pos(), i.get_pos()) < 5:
                    self.path.append(nextNode)

        elif self.direction == 3:
            nextNode = self.grid.getGrid()[self.row + 1][self.col]

            for i in self.characters.get('Trees'):
                if not self.checkNodes('Barriers', (self.row + 1, self.col)) and h(nextNode.get_pos(), i.get_pos()) < 5:
                    self.path.append(nextNode)

