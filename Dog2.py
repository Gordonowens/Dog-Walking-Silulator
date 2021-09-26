from Dog import *


class Dog2(Dog):

    def __init__(self, row, col, width, gameData, clock):


        Dog.__init__(self, row, col, width,  gameData, clock, gameData.spriteSets.get('Dog2'))

        self.image = gameData.spriteSets.get('Dog2').get('Stay Right')[0]
        self.weights = [['Flower', 1], ['Rough', 1], ['Ground', 1], ['Path', 1]]
        self.pooTime = -100
        self.coolDown = 5
        self.coolDownTimer = 5