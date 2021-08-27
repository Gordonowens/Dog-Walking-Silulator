# from sprites import *
from config import *
from algorithms import *
from Node import *

class Player(Node):
    def __init__(self, grid, row, col, width, total_rows, spriteSheet):



        Node.__init__(self, row, col, width, total_rows, spriteSheet)
        self._layer = 2
        self.image = self.createSprite(spriteSheet, 3, 2, width, width)

        self.grid = grid

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            nextNode = [self.row, self.col - 1]

            if self.grid.getGrid()[nextNode[0]][nextNode[1]] not in BARRIER:

                #update grid
                #update player position
                self.updatePosition(nextNode)
                #update node

        elif keys[pygame.K_DOWN]:
            nextNode = [self.row, self.col + 1]

            if self.grid.getGrid()[nextNode[0]][nextNode[1]] not in BARRIER:
                # update players previous position
                # update player position
                self.updatePosition(nextNode)
                # update node

        elif keys[pygame.K_LEFT]:
            nextNode = [self.row - 1, self.col]

            if self.grid.getGrid()[nextNode[0]][nextNode[1]] not in BARRIER:
                # update players previous position
                # update player position
                self.updatePosition(nextNode)
                # update node

        elif keys[pygame.K_RIGHT]:
            nextNode = [self.row + 1, self.col]

            if self.grid.getGrid()[nextNode[0]][nextNode[1]] not in BARRIER:
                # update players previous position
                # update player position
                self.updatePosition(nextNode)
                # update node

        keys_pressed = pygame.event.get()  # pygame.event.get(pygame.KEYDOWN)
        # print(keys_pressed)
        for event in keys_pressed:

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:

                for i in ENEMY:
                    i.toggleState()



            # create sphere of influence
            '''
            for i in getGridSquare(self.node.get_pos(), 4, self.grid.getGrid()):
                for j in i:
                    if j.get_color() == WHITE:
                        print(j)
                        j.make_light_blue()
                        '''











