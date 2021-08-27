from NPC import *

class NPCHangAround(NPC):

    def update(self):
        if (h(ENEMY[0].getNode().get_pos(), PLAYER[0].getNode().get_pos()) > 3) and (self.state == 'stay'):
            self.come(PLAYER[0].getNode())

        elif (h(ENEMY[0].getNode().get_pos(), PLAYER[0].getNode().get_pos()) < 2) and (self.state == 'come'):

            self.state = 'stay'

        elif self.state == 'stay':
            self.randomMove(3)

        elif self.state == 'come':
            self.movement()

        elif len(self.path) == 0:
            self.state = 'stay'