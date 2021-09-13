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
from RoughGround import *
from SquirrellSprite import *
from HumanManSprite import *
from DogSprite import *
from Heart import *
from BarrierSprite import *


def createTerrain(terrain, i, j, gap, spriteSheets):
    if (terrain == '.'):
        # create a ground sprite for each tile
        return Ground(i, j, gap, len(terrain), spriteSheets[5])


    elif (terrain == "G"):
        return GoalTile(i, j, gap, len(terrain), spriteSheets[5])


    elif (terrain == "R"):
        return RoughGround(i, j, gap, spriteSheets[5])

def createActor(actor):
    pass





def createSpriteSurface(spriteSheet, x, y, width, height, background = BLACK):
    '''

    :param spriteSheet:
    :param x:
    :param y:
    :param width:
    :param height:
    :return:
    '''

    sprite = pygame.Surface([width, height])
    sprite.blit(spriteSheet, (0, 0), (x, y, width, height))
    # this is used to create transperancy in the sprite
    sprite.set_colorkey(background)
    return sprite

def createSpriteSets():

    #create spritesets for animation
    squirrelSprite = SquirrellSprite(pygame.image.load('img/squirrel.png').convert())
    manSprite = HumanManSprite(pygame.image.load('img/player.png').convert())
    dogSprite = DogSprite(pygame.image.load('img/shibu inu sprite sheet.jpeg').convert())

    #create single sprite for actors dont need animation

    love = Heart(1, 1, 30, pygame.image.load('img/love.png').convert())


    ball = pygame.Surface([18, 18])
    ball.blit(pygame.image.load('img/sheet_equipment.png').convert(), (0, 0), (69, 71, 18, 18))
    ball.set_colorkey(BLACK)
    ball = pygame.transform.scale(ball, (10, 10))

    barrierSprite = BarrierSprite( 0, 0, 30, pygame.image.load('img/terrain.png').convert())
    spriteSets = {'Ball': ball, 'Dog': dogSprite.dogSpriteSheet, 'Player': manSprite.humanSpriteSheet,
                  'Squirrel': squirrelSprite, 'Heart': love, 'Barrier': barrierSprite}

    return spriteSets

def createIterationCharacters():

    dogs = []
    barriers = []
    animals = []
    items = []
    trees = []
    squirrels = []
    ground = []
    player = None

    iteractionCharacters = {}

    iteractionCharacters.update({'Player': player})
    iteractionCharacters.update({'Dogs': dogs})
    iteractionCharacters.update({'Barriers': barriers})
    iteractionCharacters.update({'Items': items})
    iteractionCharacters.update({'Trees': trees})
    iteractionCharacters.update({'Ground': ground})


    return iteractionCharacters

def make_game(width, spriteSheets, gap, clock, terrain, actors):
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

    gameData = Game(createIterationCharacters(), gameGrid, spriteGroup, createSpriteSets())

    #iterate over tile map and generate sprites and gamegrid
    for i in range(len(terrain)):
        grid.append([])

        for j in range(len(terrain)):

            #create terrain
            newTerrain = createTerrain(terrain[j][i], i, j, gap, spriteSheets)
            spriteGroup.add(newTerrain)

            gameData.characters.get('Ground').append(newTerrain)

            # append a general node to gamegrid for pathfinding
            grid[i].append(Node(i, j, gap, len(terrain), gameData.characters))

            #create actor
            #newActor = createActor(actors[j][i], i, j, gap, len(terrain), spriteSheets, spriteGroup, iteractionCharacters, clock, love)
            if (actors[j][i] == "B"):
                barrier = Barrier(i, j, gap, gameData.spriteSets.get('Barrier').image)
                spriteGroup.add(barrier)
                gameData.characters.get('Barriers').append(barrier)



            elif (actors[j][i] == "I"):
                node = BarrierDown(i, j, gap, len(terrain), gameData)
                spriteGroup.add(node)
                barriers.append(node)

            elif (actors[j][i] == "-"):
                node = BarrierAccross(i, j, gap, len(terrain), gameData)
                spriteGroup.add(node)
                barriers.append(node)

            #create animal sprite
            elif(actors[j][i] == "A"):
                node = Animal(i, j, gap, len(terrain), gameData)
                spriteGroup.add(node)
                animals.append(node)

            # create tennis ball sprite
            elif (actors[j][i] == "Q"):
                node = Ball(i, j, gap, gameData.spriteSets.get('Ball'))
                spriteGroup.add(node)
                gameData.characters.get('Items').append(node)
                #items.append(node)

                # create Treebottom sprite
            elif (actors[j][i] == "t"):
                node = TreeTop(i, j, gap, len(terrain), gameData)
                spriteGroup.add(node)
                #trees.append(node)

            # create Treebottom sprite
            elif (actors[j][i] == "T"):
                node = TreeBottom(i, j, gap, len(terrain), gameData)
                spriteGroup.add(node)
                #barriers.append(node)
                trees.append(node)

            # create dog sprite
            elif (actors[j][i] == "D"):
                node = Dog(i, j, gap, gameData, clock)
                spriteGroup.add(node)
                gameData.characters.get('Dogs').append(node)

            # create squirrel sprite
            elif (actors[j][i] == "S"):
                node = Squirrel(i, j, gap, len(terrain), gameData)
                spriteGroup.add(node)
                squirrels.append(node)

            #create player
            elif (actors[j][i] == "P"):
                player = Player(i, j, gap, gameData)
                spriteGroup.add(player)
                gameData.characters.update({'Player': player})

    #update gamegrid object
    gameGrid.setGrid(grid)

    gameData.gameGrid = gameGrid



    return gameData

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
                game.characters.get('Player').playerCommand = 'up'

            # down
            elif event.key == pygame.K_DOWN:
                game.characters.get('Player').playerCommand = 'down'

            # left
            elif event.key == pygame.K_LEFT:
                game.characters.get('Player').playerCommand = 'left'

            # right
            elif event.key == pygame.K_RIGHT:
                game.characters.get('Player').playerCommand = 'right'

            # space come here
            elif event.key == pygame.K_SPACE:
                game.characters.get('Player').playerCommand = 'here boy'

            elif (event.key == pygame.K_LCTRL) or (event.key == pygame.K_RCTRL):
                game.characters.get('Player').playerCommand = 'go away'

            elif event.key == pygame.K_s:
                game.characters.get('Player').playerCommand = 'stay'



        elif event.type == pygame.KEYUP:
            game.characters.get('Player').playerCommand = ''

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            for item in game.characters.get('Items'):
                if item.rect.collidepoint(pos) == 1:
                    game.characters.get('Player').pickUp()
                    return

            for ground in game.characters.get('Ground'):
                if ground.rect.collidepoint(pos) == 1:
                    game.characters.get('Player').throw(ground)



            for dog in game.characters.get('Dogs'):
                if dog.rect.collidepoint(pos) == 1:
                    dog.animalState = 'love'
                    print('goood boy')
                    return

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
    spriteSheets.append(pygame.image.load('img/love.png').convert())


    #set the game clock
    clock = pygame.time.Clock()



    #create group to control updating and drawing of sprites


    #create grid, creates all the game sprites and characters
    game = make_game(WIDTH, spriteSheets, GAP, clock, playermoveterrain, playermoveactors)


    #game loop for game 1
    running = True
    while running:
        keyEvent(game)

        clock.tick(FPS)
        screen.fill(BLACK)

        game.spriteGroup.update()
        game.spriteGroup.draw(screen)
        pygame.display.update()
        pygame.display.flip()

if __name__ == "__main__":
    main()

