from Animal import *
from config import *
from Poo import *
from Ball import *
from Heart import *

class Dog(Animal):

    def __init__(self, row, col, width, gameData, clock, spritesheet):


        Animal.__init__(self, row, col, width,  gameData.gameGrid, spritesheet, gameData.spriteGroup, gameData.characters)

        self.recordTime = 0
        self.coolDown = 7
        self.coolDownTimer = 7
        self.goal = None
        self.items = []
        self.characters = gameData.characters
        self.animalState = 'stay'
        self.items = [Poo()]
        self.clock = clock
        self.pooTime = 0
        self.heart = Heart(1, 1, 30, pygame.image.load('img/love.png').convert())
        self.weights = [['Flower', 10], ['Rough', 10], ['Ground', 4], ['Path', 1]]




    def stateReset(self):
        '''resets path and player command when transfering between states'''

        self.path = []
        self.playerCommand = ''


    def stayState(self):
        if self.playerCommand == 'flee':
            self.animalState = 'flee'
            self.stateReset()


        elif self.playerCommand == 'follow':
            self.animalState = 'follow'
            self.stateReset()

        elif self.playerCommand == 'stay':
            self.animalState = 'stay'
            self.stateReset()

        elif self.playerCommand == 'fetch':
            self.animalState = 'fetch'
            self.stateReset()

        elif self.playerCommand == 'love':
            self.animalState = 'love'
            self.stateReset()

        elif self.coolDownTimer == -250:

            self.animalState = 'sleep'
            self.movementSprite = 'Sleep'
            self.updateSprite()
            self.stateReset()



    def sleepState(self):


        if self.playerCommand == 'flee':
            self.animalState = 'flee'
            self.stateReset()


        elif self.playerCommand == 'follow':
            self.animalState = 'follow'
            self.stateReset()

        elif self.playerCommand == 'stay':
            self.animalState = 'stay'
            self.stateReset()

        elif self.coolDownTimer < 0:
            self.updateSprite()
            self.coolDownTimer = 25

    def fleeState(self):
        # change state if appropriote
        if self.playerCommand == 'follow':
            self.animalState = 'follow'
            self.stateReset()

        elif self.playerCommand == 'fetch':
            self.animalState = 'fetch'
            self.stateReset()

        elif self.playerCommand == 'stay':
            self.animalState = 'stay'
            self.stateReset()

        # else if animal is far enough from player change state to flee sniff
        elif (h(self.get_pos(), self.characters.get('Player').get_pos()) > 5):
            self.animalState = 'flee sniff'
            self.stateReset()

        # else if animal still has places to move move
        elif len(self.path) > 0 and self.coolDownTimer <= 25:

            self.movement()
            self.coolDownTimer = self.coolDown

        # else if player is too close find a place to move to
        elif (h(self.get_pos(), self.characters.get('Player').get_pos()) < 5) and len(self.path) <= 0:
            self.runAway()

    def fleeSniffState(self):
        # if player is less than 5 blocks away change state to flee
        if (h(self.get_pos(), self.characters.get('Player').get_pos()) < 5):
            self.animalState = 'flee'
            self.stateReset()

        elif self.playerCommand == 'stay':
            self.animalState = 'stay'
            self.stateReset()

        elif self.playerCommand == 'follow':

            self.animalState = 'follow'

            self.stateReset()

        elif self.playerCommand == 'fetch':
            self.animalState = 'fetch'
            self.stateReset()

        elif self.coolDownTimer <= 1:
            self.randomMove()
            self.movement()
            self.coolDownTimer = self.coolDown

    def followState(self):
        # change state if appropriote
        if self.playerCommand == 'stay':
            self.animalState = 'stay'
            self.stateReset()

        # change state if appropriote
        elif self.playerCommand == 'flee':
            self.animalState = 'flee'
            self.stateReset()

        elif self.playerCommand == 'fetch':
            self.animalState = 'fetch'
            self.stateReset()

        # if player is within 4 spaces of animal change state to follow sniff
        elif h(self.get_pos(), self.characters.get('Player').get_pos()) < 4:
            self.animalState = 'follow sniff'
            self.stateReset()

        # if there are still spaces to move in the path - then move
        elif len(self.path) > 0 and self.coolDownTimer <= 1:
            self.coolDownTimer = self.coolDown
            self.movement()

        elif len(self.path) <= 0:
            self.come(self.characters.get('Player'))

    def followSniffState(self):
        # if player is over 4 spaces away from animal then create a path to player
        if self.playerCommand == 'follow':
            self.animalState = 'follow'
            self.stateReset()

        elif self.playerCommand == 'stay':
            self.animalState = 'stay'
            self.stateReset()

        elif self.playerCommand == 'flee':
            self.animalState = 'flee'
            self.stateReset()

        elif self.playerCommand == 'fetch':
            self.animalState = 'fetch'
            self.stateReset()

        # if player is more than 4 spaces from dog change state to follow
        elif h(self.get_pos(), self.characters.get('Player').get_pos()) > 4:
            self.animalState = 'follow'
            self.stateReset()

        elif self.coolDownTimer <= -15:
            self.randomMove()
            self.movement()
            self.coolDownTimer = self.coolDown

    def fetchState(self):
        #get location of ball

        if self.goal not in self.characters.get('Items'):
            self.animalState = 'follow'
            self.stateReset()
            self.goal = None

        elif len(self.path) <= 0:
            self.come(self.goal)
            pass

        # if there are still spaces to move in the path - then move
        elif len(self.path) > 0 and self.coolDownTimer <= 2:
            self.coolDownTimer = self.coolDown
            self.movement()


        elif self.get_pos() == self.goal.get_pos():
            self.pickUp()
            self.animalState = 'return ball'
            self.stateReset()

    def returnBallState(self):

        #if dog is near player drop ball and change state to follow
        if h(self.get_pos(), self.characters.get('Player').get_pos()) <= 1:
            for i, item in enumerate(self.items):
                if isinstance(item, Ball):

                    self.dropItem(self, item)
                    self.animalState = 'follow'
                    self.stateReset()
                    self.items = []


        # if there are still spaces to move in the path - then move
        elif len(self.path) > 0 and self.coolDownTimer <= 0:
            self.coolDownTimer = self.coolDown
            self.movement()

        #create path
        elif len(self.path) <= 0:
            self.come(self.characters.get('Player'))

    def update(self):
        '''
        this function handles moving the dog between states
        no other function can change the dog's state
        '''

        if self.pooTime < 1002:
            self.pooTime = self.pooTime + 1



        self.coolDownTimer = self.coolDownTimer - 1

        #do nothing if in stay state
        if self.animalState == 'stay':
            self.stayState()
            if self.pooTime > 1000:
                self.poo()

        elif self.animalState == 'sleep':
            self.sleepState()

        elif self.animalState == 'love':
            self.loveState()

        elif self.animalState == 'flee':
            self.fleeState()
            if self.pooTime > 1000:
                self.poo()

        elif self.animalState == 'flee sniff':
            self.fleeSniffState()
            if self.pooTime > 1000:
                self.poo()

        elif self.animalState == 'follow':
            self.followState()
            if self.pooTime > 1000:
                self.poo()

        elif self.animalState == 'follow sniff':
            self.followSniffState()
            if self.pooTime > 1000:
                self.poo()

        elif self.animalState == 'fetch':
            self.fetchState()

        elif self.animalState == 'return ball':
            self.returnBallState()

        #update rectangle of sprite, x,y refers to upper left corner of sprite box
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

    def poo(self):
        # check player has ball
        for i, item in enumerate(self.items):
            if isinstance(item, Poo):

                self.dropItem(self.grid.getGrid()[self.row][self.col], item)
                self.items.pop(i)

    def loveState(self):

        if self.movementSprite != 'Love':
            self.animationCells = self.spriteSets.get('Love').copy()
            self.movementSprite = 'Love'
            # create heart
            self.heart.updatePosition(((self.row + 1), self.col))
            #heart = Heart(, self.heart)
            # add heart to
            self.spriteGroup.add(self.heart)

        elif self.movementSprite == 'Love' and len(self.animationCells) == 0:
            self.animalState = 'stay'
            self.movementSprite = 'Stay'
            self.updateSprite()

        # if there are still spaces to move in the path - then move
        elif self.movementSprite == 'Love' and self.coolDownTimer <= -1:
            self.animateAnimals()
            self.coolDownTimer = self.coolDown