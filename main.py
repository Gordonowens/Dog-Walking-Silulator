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
from Dog import *
from Ball import *
from TreeBottom import *
from TreeTop import *
from Squirrel import *


def make_grid(width, spriteGroup, spriteSheets, gap, clock):
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

    dogs = []
    barriers = []
    animals = []
    items = []
    trees = []
    squirrels = []
    player = None

    iteractionCharacters = {}

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
                grid[i].append(Node(i, j, gap, len(tilemap), iteractionCharacters))
                spriteGroup.add(node)
                barriers.append(node)

            #create animal sprite
            elif(tilemap[j][i] == "A"):
                node = Animal(i, j, gap, len(tilemap), gameGrid, spriteSheets[2], spriteGroup, iteractionCharacters)
                #append a general node to gamegrid for pathfinding
                grid[i].append(Node(i, j, gap, len(tilemap), iteractionCharacters))
                spriteGroup.add(node)
                animals.append(node)

            # create tennis ball sprite
            elif (tilemap[j][i] == "Q"):
                node = Ball(i, j, gap, len(tilemap), spriteSheets[3])
                # append a general node to gamegrid for pathfinding
                grid[i].append(Node(i, j, gap, len(tilemap), iteractionCharacters))
                spriteGroup.add(node)
                items.append(node)

                # create Treebottom sprite
            elif (tilemap[j][i] == "t"):
                node = TreeTop(i, j, gap, len(tilemap), spriteSheets[1])
                # barrier gets added to gamegrid for pathfinding
                grid[i].append(Node(i, j, gap, len(tilemap),  iteractionCharacters))
                spriteGroup.add(node)
                trees.append(node)

            # create Treebottom sprite
            elif (tilemap[j][i] == "T"):
                node = TreeBottom(i, j, gap, len(tilemap), spriteSheets[1])
                # barrier gets added to gamegrid for pathfinding
                grid[i].append(Node(i, j, gap, len(tilemap), iteractionCharacters))
                spriteGroup.add(node)
                trees.append(node)

            # create dog sprite
            elif (tilemap[j][i] == "D"):
                node = Dog(i, j, gap, len(tilemap), gameGrid, spriteSheets[2], spriteGroup, iteractionCharacters)
                # append a general node to gamegrid for pathfinding
                grid[i].append(Node(i, j, gap, len(tilemap), iteractionCharacters))
                spriteGroup.add(node)
                dogs.append(node)

            # create squirrel sprite
            elif (tilemap[j][i] == "S"):
                node = Squirrel(i, j, gap, len(tilemap), gameGrid, spriteSheets[4], spriteGroup)
                # append a general node to gamegrid for pathfinding
                grid[i].append(Node(i, j, gap, len(tilemap), iteractionCharacters))
                spriteGroup.add(node)
                squirrels.append(node)


            #create player
            elif (tilemap[j][i] == "P"):
                node = Player(gameGrid, i, j, gap, len(tilemap), spriteSheets[0], spriteGroup, iteractionCharacters)
                # append a general node to gamegrid for pathfinding
                grid[i].append(Node(i, j, gap, len(tilemap), iteractionCharacters))
                spriteGroup.add(node)
                player = node

            else:
                node = Node(i, j, gap, len(tilemap), iteractionCharacters)
                # append a general node to gamegrid for pathfinding
                grid[i].append(node)

    #update gamegrid object
    gameGrid.setGrid(grid)

    iteractionCharacters.update({'Player': player})
    iteractionCharacters.update({'Dogs': dogs})
    iteractionCharacters.update({'Barriers': barriers})
    iteractionCharacters.update({'Items': items})
    #iteractionCharacters.update({'Animals': animals})

def main():
    #initialise pygam
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, WIDTH))

    #load in the sprite sheets
    spriteSheets = []
    spriteSheets.append(pygame.image.load('img/character.png').convert())
    spriteSheets.append(pygame.image.load('img/terrain.png').convert())
    spriteSheets.append(pygame.image.load('img/dogs.jpg').convert())
    spriteSheets.append(pygame.image.load('img/tennis ball.png').convert())
    spriteSheets.append(pygame.image.load('img/squirrel.png').convert())


    #set the game clock
    clock = pygame.time.Clock()

    #create group to control updating and drawing of sprites
    all_sprites = pygame.sprite.LayeredUpdates()

    #create grid, creates all the game sprites and characters
    make_grid(WIDTH, all_sprites, spriteSheets, GAP, clock)

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

