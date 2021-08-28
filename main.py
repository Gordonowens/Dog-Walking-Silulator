import pygame
# from sprites import *
from config import *
import sys
from Node import Node
import math
from queue import PriorityQueue
from Barrier import *
from Player import Player
from NPC import NPC
from Grid import*
from NPCAway import *
from NPCHangAround import *
from Animal import *
from Ground import *


def make_grid(width, spriteGroup, spriteSheets):
    grid = []
    gameGrid = Grid([])
    gap = 30

    for i in range(len(tilemap)):
        grid.append([])
        for j in range(len(tilemap)):
            node = Ground(i, j, gap, len(tilemap), spriteSheets[1])
            spriteGroup.add(node)
            if(tilemap[j][i] == "B"):
                node = Barrier(i, j, gap, len(tilemap), spriteSheets[1])
                grid[i].append(node)
                spriteGroup.add(node)
                BARRIER.append(node)

            elif(tilemap[j][i] == "A"):
                node = Animal(i, j, gap, len(tilemap), gameGrid, spriteSheets[2])
                grid[i].append(Node(i, j, gap, len(tilemap), spriteSheets[0]))
                spriteGroup.add(node)
                ENEMY.append(node)

            elif (tilemap[j][i] == "P"):

                node = Player(gameGrid, i, j, gap, len(tilemap), spriteSheets[0])
                grid[i].append(Node(i, j, gap, len(tilemap), spriteSheets[0]))
                spriteGroup.add(node)
                PLAYER.append(node)

            else:
                node = Node(i, j, gap, len(tilemap), spriteSheets[0])
                grid[i].append(node)
                #spriteGroup.add(node)

            #print(grid)


        gameGrid.setGrid(grid)
    #print(grid)

    return gameGrid






def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, WIDTH))
    #sprite sheets go character, terrain, enemy
    spriteSheets = []
    spriteSheets.append(pygame.image.load('img/character.png').convert())
    spriteSheets.append(pygame.image.load('img/terrain.png').convert())
    spriteSheets.append(pygame.image.load('img/dogs.jpg').convert())
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.LayeredUpdates()

    #create grid
    make_grid(WIDTH, all_sprites, spriteSheets)

    #game loop
    running = True
    while running:

        clock.tick(FPS)
        screen.fill(BLACK)
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.update()
        pygame.display.flip()




    pygame.quit()


if __name__ == "__main__":
    main()

