import pygame
# from sprites import *
from config import *
import sys
from Node import Node
import math
from queue import PriorityQueue
from Barrier import *
from BarrierDown import *
from BarrierAccross import *
from Player import Player
from Grid import*
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
            node = Ground(i, j, gap, len(tilemap), spriteSheets[5])
            spriteGroup.add(node)

            #create barrier sprite
            if(tilemap[j][i] == "B"):
                node = Barrier(i, j, gap, len(tilemap), spriteSheets[1])
                #barrier gets added to gamegrid for pathfinding
                grid[i].append(Node(i, j, gap, len(tilemap), iteractionCharacters))
                spriteGroup.add(node)
                barriers.append(node)

            elif (tilemap[j][i] == "I"):
                node = BarrierDown(i, j, gap, len(tilemap), spriteSheets[5])
                # barrier gets added to gamegrid for pathfinding
                grid[i].append(Node(i, j, gap, len(tilemap), iteractionCharacters))
                spriteGroup.add(node)
                barriers.append(node)

            elif (tilemap[j][i] == "-"):
                node = BarrierAccross(i, j, gap, len(tilemap), spriteSheets[5])
                # barrier gets added to gamegrid for pathfinding
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
                node = TreeTop(i, j, gap, len(tilemap), spriteSheets[5])
                # barrier gets added to gamegrid for pathfinding
                grid[i].append(Node(i, j, gap, len(tilemap),  iteractionCharacters))
                spriteGroup.add(node)
                #trees.append(node)

            # create Treebottom sprite
            elif (tilemap[j][i] == "T"):
                node = TreeBottom(i, j, gap, len(tilemap), spriteSheets[5])
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
                node = Squirrel(i, j, gap, len(tilemap), gameGrid, spriteSheets[4], spriteGroup, iteractionCharacters)
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
    iteractionCharacters.update({'Trees': trees})

    #iteractionCharacters.update({'Animals': animals})

def show_score(text, x, y, screen):
    font = pygame.font.Font('freesansbold.ttf', 12)
    score = font.render(text, True, (255, 255, 255))
    screen.blit(score, (x, y))


def main():
    #initialise pygam
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, WIDTH))

    #load in the sprite sheets
    spriteSheets = []
    spriteSheets.append(pygame.image.load('img/roguelikeChar_transparent.png').convert())
    spriteSheets.append(pygame.image.load('img/terrain.png').convert())
    spriteSheets.append(pygame.image.load('img/shibu inu sprite sheet.jpeg').convert())
    spriteSheets.append(pygame.image.load('img/sheet_equipment.png').convert())
    spriteSheets.append(pygame.image.load('img/squirrel.png').convert())
    spriteSheets.append(pygame.image.load('img/terrain2.png').convert())


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
        show_score("Press space to get the dog to follow you", 600, 60, screen)
        show_score("Use arrow keys to control your player", 60, 60, screen)
        show_score("Press p to pick up the ball", 60, 400, screen)
        show_score("Press t to throw the ball", 60, 440, screen)
        show_score("Press press left ctrl to play chase with the dog",600, 120, screen)
        show_score("Squirrels aren't afraid of humans but will run and hide from dogs", 60, 800, screen)
        pygame.display.update()
        pygame.display.flip()

if __name__ == "__main__":
    main()

