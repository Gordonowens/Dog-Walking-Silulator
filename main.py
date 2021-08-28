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


def make_grid(width, spriteGroup, spriteSheets, gap):
    '''
    this function iterates through the tilemap and generates sprites
    and creates game grid for pathfinding
    :int width:
    :pygame.sprite.LayeredUpdates() spriteGroup: holds sprites to be drawn and updated
    :list spriteSheets:  with file directions
    :int gap: how many pixels wide each sprite is
    '''

    grid = []
    gameGrid = Grid([])

    #iterate over tile map and generate sprites and gamegrid
    for i in range(len(tilemap)):
        grid.append([])

        for j in range(len(tilemap)):
            #create a ground sprite for each tile
            node = Ground(i, j, gap, len(tilemap), spriteSheets[1])
            spriteGroup.add(node)

            #create barrier sprite
            if(tilemap[j][i] == "B"):
                node = Barrier(i, j, gap, len(tilemap), spriteSheets[1])
                #barrier gets added to gamegrid for pathfinding
                grid[i].append(node)
                spriteGroup.add(node)
                BARRIER.append(node)

            #create animal sprite
            elif(tilemap[j][i] == "A"):
                node = Animal(i, j, gap, len(tilemap), gameGrid, spriteSheets[2])
                #append a general node to gamegrid for pathfinding
                grid[i].append(Node(i, j, gap, len(tilemap), spriteSheets[0]))
                spriteGroup.add(node)
                ENEMY.append(node)

            #create player
            elif (tilemap[j][i] == "P"):
                node = Player(gameGrid, i, j, gap, len(tilemap), spriteSheets[0])
                # append a general node to gamegrid for pathfinding
                grid[i].append(Node(i, j, gap, len(tilemap), spriteSheets[0]))
                spriteGroup.add(node)
                PLAYER.append(node)

            else:
                node = Node(i, j, gap, len(tilemap), spriteSheets[0])
                # append a general node to gamegrid for pathfinding
                grid[i].append(node)

        #update gamegrid object
        gameGrid.setGrid(grid)






def main():
    #initialise pygam
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, WIDTH))

    #load in the sprite sheets
    spriteSheets = []
    spriteSheets.append(pygame.image.load('img/character.png').convert())
    spriteSheets.append(pygame.image.load('img/terrain.png').convert())
    spriteSheets.append(pygame.image.load('img/dogs.jpg').convert())

    #set the game clock
    clock = pygame.time.Clock()

    #create group to control updating and drawing of sprites
    all_sprites = pygame.sprite.LayeredUpdates()

    #create grid, creates all the game sprites and characters
    make_grid(WIDTH, all_sprites, spriteSheets, GAP)

    #game loop
    running = True
    while running:

        clock.tick(FPS)
        screen.fill(BLACK)
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.update()
        pygame.display.flip()

if __name__ == "__main__":
    main()

