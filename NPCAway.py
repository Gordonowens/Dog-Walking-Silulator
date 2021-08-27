from NPC import *


class NPCAway(NPC):
    def update(self):
        if (h(ENEMY[0].getNode().get_pos(), PLAYER[0].getNode().get_pos()) < 10) and (self.state == 'stay'):
            print("run away")
