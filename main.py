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
from Game import *
from GoalTile import *


def make_game(width, spriteSheets, gap, clock, gamemap):
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
    spriteGroup = pygame.sprite.LayeredUpdates()

    dogs = []
    barriers = []
    animals = []
    items = []
    trees = []
    squirrels = []
    player = None

    iteractionCharacters = {}

    #iterate over tile map and generate sprites and gamegrid
    for i in range(len(gamemap)):
        grid.append([])

        for j in range(len(gamemap)):
            #create a ground sprite for each tile
            node = Ground(i, j, gap, len(gamemap), spriteSheets[5])
            spriteGroup.add(node)

            #create barrier sprite
            if(gamemap[j][i] == "B"):
                node = Barrier(i, j, gap, len(gamemap), spriteSheets[1])
                #barrier gets added to gamegrid for pathfinding
                grid[i].append(Node(i, j, gap, len(gamemap), iteractionCharacters))
                spriteGroup.add(node)
                barriers.append(node)


            elif (gamemap[j][i] == "G"):
                node = GoalTile(i, j, gap, len(gamemap), spriteSheets[1])
                # barrier gets added to gamegrid for pathfinding
                grid[i].append(Node(i, j, gap, len(gamemap), iteractionCharacters))
                spriteGroup.add(node)
                #goals.append(node)


            elif (gamemap[j][i] == "I"):
                node = BarrierDown(i, j, gap, len(gamemap), spriteSheets[5])
                # barrier gets added to gamegrid for pathfinding
                grid[i].append(Node(i, j, gap, len(gamemap), iteractionCharacters))
                spriteGroup.add(node)
                barriers.append(node)

            elif (gamemap[j][i] == "-"):
                node = BarrierAccross(i, j, gap, len(gamemap), spriteSheets[5])
                # barrier gets added to gamegrid for pathfinding
                grid[i].append(Node(i, j, gap, len(gamemap), iteractionCharacters))
                spriteGroup.add(node)
                barriers.append(node)

            #create animal sprite
            elif(gamemap[j][i] == "A"):
                node = Animal(i, j, gap, len(gamemap), gameGrid, spriteSheets[2], spriteGroup, iteractionCharacters)
                #append a general node to gamegrid for pathfinding
                grid[i].append(Node(i, j, gap, len(gamemap), iteractionCharacters))
                spriteGroup.add(node)
                animals.append(node)

            # create tennis ball sprite
            elif (gamemap[j][i] == "Q"):
                node = Ball(i, j, gap, len(gamemap), spriteSheets[3])
                # append a general node to gamegrid for pathfinding
                grid[i].append(Node(i, j, gap, len(gamemap), iteractionCharacters))
                spriteGroup.add(node)
                items.append(node)

                # create Treebottom sprite
            elif (gamemap[j][i] == "t"):
                node = TreeTop(i, j, gap, len(gamemap), spriteSheets[5])
                # barrier gets added to gamegrid for pathfinding
                grid[i].append(Node(i, j, gap, len(gamemap), iteractionCharacters))
                spriteGroup.add(node)
                #trees.append(node)

            # create Treebottom sprite
            elif (gamemap[j][i] == "T"):
                node = TreeBottom(i, j, gap, len(gamemap), spriteSheets[5])
                # barrier gets added to gamegrid for pathfinding
                grid[i].append(Node(i, j, gap, len(gamemap), iteractionCharacters))
                spriteGroup.add(node)
                #barriers.append(node)
                trees.append(node)

            # create dog sprite
            elif (gamemap[j][i] == "D"):
                node = Dog(i, j, gap, len(gamemap), gameGrid, spriteSheets[2], spriteGroup, iteractionCharacters)
                # append a general node to gamegrid for pathfinding
                grid[i].append(Node(i, j, gap, len(gamemap), iteractionCharacters))
                spriteGroup.add(node)
                dogs.append(node)

            # create squirrel sprite
            elif (gamemap[j][i] == "S"):
                node = Squirrel(i, j, gap, len(gamemap), gameGrid, spriteSheets[4], spriteGroup, iteractionCharacters)
                # append a general node to gamegrid for pathfinding
                grid[i].append(Node(i, j, gap, len(gamemap), iteractionCharacters))
                spriteGroup.add(node)
                squirrels.append(node)


            #create player
            elif (gamemap[j][i] == "P"):
                node = Player(gameGrid, i, j, gap, len(gamemap), spriteSheets[0], spriteGroup, iteractionCharacters)
                # append a general node to gamegrid for pathfinding
                grid[i].append(Node(i, j, gap, len(gamemap), iteractionCharacters))
                spriteGroup.add(node)
                player = node

            else:
                node = Node(i, j, gap, len(gamemap), iteractionCharacters)
                # append a general node to gamegrid for pathfinding
                grid[i].append(node)

    #update gamegrid object
    gameGrid.setGrid(grid)

    iteractionCharacters.update({'Player': player})
    iteractionCharacters.update({'Dogs': dogs})
    iteractionCharacters.update({'Barriers': barriers})
    iteractionCharacters.update({'Items': items})
    iteractionCharacters.update({'Trees': trees})

    return Game(iteractionCharacters, gameGrid, spriteGroup)

def show_score(text, x, y, screen):
    font = pygame.font.Font('freesansbold.ttf', 18)
    score = font.render(text, True, (255, 255, 255))
    screen.blit(score, (x, y))


def keyEvent(game):
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:

            # up
            if event.key == pygame.K_UP:
                game.characters.get('Player').nextMovement = 'up'

            # down
            elif event.key == pygame.K_DOWN:
                game.characters.get('Player').nextMovement = 'down'

            # left
            elif event.key == pygame.K_LEFT:
                game.characters.get('Player').nextMovement = 'left'

            # right
            elif event.key == pygame.K_RIGHT:
                game.characters.get('Player').nextMovement = 'right'

            # space come here
            elif event.key == pygame.K_SPACE:
                game.characters.get('Player').nextMovement = 'here boy'


            elif (event.key == pygame.K_LCTRL) or (event.key == pygame.K_RCTRL):
                game.characters.get('Player').nextMovement = 'go away'

            elif event.key == pygame.K_s:
                game.characters.get('Player').nextMovement = 'stay'

            elif event.key == pygame.K_t:
                game.characters.get('Player').nextMovement = 'throw'

            elif event.key == pygame.K_p:
                game.characters.get('Player').nextMovement = 'pick up'

        elif event.type == pygame.KEYUP:
            game.characters.get('Player').nextMovement = ''

def main():
    #initialise pygam
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, WIDTH))

    #load in the sprite sheets
    spriteSheets = []
    spriteSheets.append(pygame.image.load('img/player.png').convert())
    spriteSheets.append(pygame.image.load('img/terrain.png').convert())
    spriteSheets.append(pygame.image.load('img/shibu inu sprite sheet.jpeg').convert())
    spriteSheets.append(pygame.image.load('img/sheet_equipment.png').convert())
    spriteSheets.append(pygame.image.load('img/squirrel.png').convert())
    spriteSheets.append(pygame.image.load('img/terrain2.png').convert())


    #set the game clock
    clock = pygame.time.Clock()

    #create group to control updating and drawing of sprites


    #create grid, creates all the game sprites and characters
    game = make_game(WIDTH, spriteSheets, GAP, clock, playball)


    #game loop for game 1
    running = True
    while running:
        keyEvent(game)

        clock.tick(FPS)
        screen.fill(BLACK)

        game.spriteGroup.update()
        game.spriteGroup.draw(screen)
        show_score("Use arrow keys to control your character", 30, 60, screen)
        show_score("Press 'space' to get the dog to follow you", 500, 60, screen)
        show_score("Press 's' to get the dog to stay", 500, 85, screen)
        show_score("Press 'ctrl' to play chase with the dog", 500, 110, screen)

        show_score("Press 'p' to pick up the ball and 't' to throw", 30, 375, screen)
        show_score("the dog will play fetch", 30, 390, screen)
        show_score("Squirrels are scared of dogs but not humans", 350, 825, screen)
        pygame.display.update()
        pygame.display.flip()

if __name__ == "__main__":
    main()

