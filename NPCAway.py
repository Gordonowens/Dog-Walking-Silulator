from NPC import *


class NPCAway(NPC):

    def runAway(self):
        #get sphere of influence
        bestNode = None
        bestDist = 8
        for i in getGridSquare(self.node.get_pos(), 5, self.grid.getGrid()):
            for j in i:
                if j not in BARRIER and j not in PLAYER:

                    if h(j.get_pos(), PLAYER[0].getNode().get_pos()) > bestDist:
                        #print("runaway")
                        bestNode = j
                        bestDist = h(j.get_pos(), PLAYER[0].getNode().get_pos())

        if bestNode != None:
            self.come(bestNode)




    def update(self):
        if (h(ENEMY[0].getNode().get_pos(), PLAYER[0].getNode().get_pos()) < 5) and (self.state == 'stay'):

            self.runAway()

        elif self.state == 'come':

            self.movement()
