from Animal import *

class Dog(Animal):

    def __init__(self, row, col, width, total_rows, grid, spriteSheet, time):

        Animal.__init__(self, row, col, width, total_rows, grid, spriteSheet)
        self.time = time
        self.recordTime = 0

    def stateReset(self):
        '''resets path and player command when transfering between states'''

        self.path = []
        self.playerCommand = ''

    def update(self):
        '''
        this function handles moving the dog between states
        no other function can change the dog's state
        '''

        #do nothing if in stay state
        if self.animalState == 'stay':
            if self.playerCommand == 'flee':
                self.animalState = 'flee'
                self.stateReset()


            elif self.playerCommand == 'follow':
                self.animalState = 'follow'
                self.stateReset()

            elif self.playerCommand == 'stay':
                self.animalState = 'stay'
                self.stateReset()

        elif self.animalState == 'flee':
            #change state if appropriote
            if self.playerCommand == 'follow':
                self.animalState = 'follow'
                self.stateReset()


            #else if animal is far enough from player change state to flee sniff
            elif (h(self.get_pos(), PLAYER[0].get_pos()) > 5):
                self.animalState = 'flee sniff'
                self.stateReset()

            #else if animal still has places to move move
            elif len(self.path) > 0:
                self.movement()

            #else if player is too close find a place to move to
            elif (h(self.get_pos(), PLAYER[0].get_pos()) < 5):
                self.runAway()

        elif self.animalState =='flee sniff':

            #if player is less than 5 blocks away change state to flee
            if (h(self.get_pos(), PLAYER[0].get_pos()) < 5):
                self.animalState = 'flee'
                self.stateReset()

            elif self.playerCommand == 'follow':

                self.animalState = 'follow'

                self.stateReset()

            else:
                self.randomMove()
                self.movement()


        elif self.animalState == 'follow':
            #change state if appropriote
            if self.playerCommand == 'stay':
                self.animalState = 'stay'
                self.stateReset()

            # change state if appropriote
            elif self.playerCommand == 'flee':
                self.animalState = 'flee'
                self.stateReset()

            #if player is within 4 spaces of animal change state to follow sniff
            elif h(self.get_pos(), PLAYER[0].get_pos()) < 4:
                self.animalState = 'follow sniff'
                self.stateReset()

            #if there are still spaces to move in the path - then move
            elif len(self.path) > 0:
                self.movement()

            else:
                self.come(PLAYER[0])

        elif self.animalState == 'follow sniff':
            #if player is over 4 spaces away from animal then create a path to player
            if self.playerCommand == 'follow':
                self.animalState = 'follow'
                self.stateReset()

            elif self.playerCommand == 'stay':
                self.animalState = 'stay'
                self.stateReset()

            elif self.playerCommand == 'flee':
                self.animalState = 'flee'
                self.stateReset()

            #if player is more than 4 spaces from dog change state to follow
            elif h(self.get_pos(), PLAYER[0].get_pos())  > 4:
                self.animalState = 'follow'
                self.stateReset()

            else:
                self.randomMove()
                self.movement()

        #update rectangle of sprite, x,y refers to upper left corner of sprite box
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

    def randomMove(self):

        #self.recordTime
        self.direction = randrange(4)

        if self.direction == 0:
            nextNode = self.grid.getGrid()[self.get_pos()[0]][self.get_pos()[1] - 1]
            if nextNode not in BARRIER:
                self.path.append(nextNode)

        elif self.direction == 1:
            nextNode = self.grid.getGrid()[self.get_pos()[0]][self.get_pos()[1] + 1]

            if nextNode not in BARRIER:
                self.path.append(nextNode)

        elif self.direction == 2:

            nextNode = self.grid.getGrid()[self.get_pos()[0] - 1][self.get_pos()[1]]

            if nextNode not in BARRIER:
                self.path.append(nextNode)

        elif self.direction == 3:
            nextNode = self.grid.getGrid()[self.get_pos()[0] + 1][self.get_pos()[1]]

            if nextNode not in BARRIER:
                self.path.append(nextNode)