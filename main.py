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
from WaterSprite import *
from Water import *
from Duck import *
from DuckSprite import *
from Bread import *
from BlackBarrier import *
from BarrierDownSprite import *
from BarrierAccrossSprite import *



def createTerrain(terrain, i, j, gap):

    terrainSpriteSheet = pygame.image.load('img/terrain2.png').convert()
    if (terrain == '.'):
        # create a ground sprite for each tile
        return Ground(i, j, gap, terrainSpriteSheet)

    elif (terrain == "G"):
        return GoalTile(i, j, gap, terrainSpriteSheet)


    elif (terrain == "R"):
        return RoughGround(i, j, gap, terrainSpriteSheet)


def createActor(actor, i, j , gap, gameData, clock):

    if (actor == "B"):
        actor = Barrier(i, j, gap, gameData.spriteSets.get('Barrier').image)
        gameData.spriteGroup.add(actor)
        gameData.characters.get('Barriers').append(actor)

    elif (actor == ","):
        actor = BlackBarrier(i, j, gap)
        gameData.spriteGroup.add(actor)
        gameData.characters.get('Barriers').append(actor)


    elif (actor == "I"):
        actor = BarrierDown(i, j, gap, gameData.spriteSets.get('Barrier Down').image)
        gameData.spriteGroup.add(actor)
        gameData.characters.get('Barriers').append(actor)

    elif (actor == "W"):
        actor = Water(i, j, gap, gameData.spriteSets.get('Water'))
        gameData.spriteGroup.add(actor)
        gameData.characters.get('Water').append(actor)

    elif (actor == "-"):
        actor = BarrierAccross(i, j, gap, gameData.spriteSets.get('Barrier Accross').image)
        gameData.spriteGroup.add(actor)
        gameData.characters.get('Barriers').append(actor)

    # create animal sprite
    elif (actor == "A"):
        actor = Animal(i, j, gap, gameData)
        gameData.spriteGroup.add(actor)
        gameData.characters.get('Animals').append(actor)


    # create tennis ball sprite
    elif (actor == "Q"):
        actor = Ball(i, j, gap, gameData.spriteSets.get('Ball'))
        gameData.spriteGroup.add(actor)
        gameData.characters.get('Items').append(actor)

        # create tennis ball sprite
    elif (actor == "b"):
        actor = Bread(i, j, gap, gameData.spriteSets.get('Bread'))
        gameData.spriteGroup.add(actor)
        gameData.characters.get('Items').append(actor)

        # create Treebottom sprite
    elif (actor == "t"):
        actor = TreeTop(i, j, gap, gameData.spriteSets.get('Tree Top'))
        gameData.spriteGroup.add(actor)
        # trees.append(node)

    # create Treebottom sprite
    elif (actor == "T"):
        actor = TreeBottom(i, j, gap, gameData.spriteSets.get('Tree Bottom'))
        gameData.spriteGroup.add(actor)
        # barriers.append(node)
        gameData.characters.get('Trees').append(actor)

    # create dog sprite
    elif (actor == "D"):
        actor = Dog(i, j, gap, gameData, clock)
        gameData.spriteGroup.add(actor)
        gameData.characters.get('Dogs').append(actor)

    # create squirrel sprite
    elif (actor == "S"):
        actor = Squirrel(i, j, gap, gameData)
        gameData.spriteGroup.add(actor)
        gameData.characters.get('Squirrels').append(actor)

    # create squirrel sprite
    elif (actor == "N"):
        actor = Duck(i, j, gap, gameData)
        gameData.spriteGroup.add(actor)
        gameData.characters.get('Ducks').append(actor)

    # create player
    elif (actor == "P"):
        player = Player(i, j, gap, gameData)
        gameData.spriteGroup.add(player)
        gameData.characters.update({'Player': player})

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
    duckSprite = DuckSprite(pygame.image.load('img/ducks.png').convert())

    #create single sprite for actors dont need animation

    love = Heart(1, 1, 30, pygame.image.load('img/love.png').convert())


    ball = pygame.Surface([18, 18])
    ball.blit(pygame.image.load('img/sheet_equipment.png').convert(), (0, 0), (69, 71, 18, 18))
    ball.set_colorkey(BLACK)
    ball = pygame.transform.scale(ball, (10, 10))

    breadScraps = pygame.Surface([30, 30])
    breadScraps.blit(pygame.image.load('img/terrain.png').convert(), (0, 0), (929, 578, 29, 29))
    breadScraps.set_colorkey(BLACK)
    breadScraps = pygame.transform.scale(breadScraps, (15, 15))

    bread = pygame.Surface([10, 5])
    bread.blit(pygame.image.load('img/terrain2.png').convert(), (0, 0), (819, 125, 10, 5))
    bread.set_colorkey(WHITE)
    bread = pygame.transform.scale(bread, (20, 15))

    barrierSprite = BarrierSprite(0, 0, 30, pygame.image.load('img/terrain.png').convert())
    barrierDown = BarrierDownSprite(0, 0, 30, pygame.image.load('img/terrain2.png').convert())
    barrierAccross = BarrierAccrossSprite(0, 0, 30, pygame.image.load('img/terrain2.png').convert())

    waterSprite = pygame.Surface([16, 16])
    waterSprite.blit(pygame.image.load('img/terrain2.png').convert(), (0, 0), (51, 17, 16, 16))
    waterSprite.set_colorkey(WHITE)
    waterSprite = pygame.transform.scale(waterSprite, (30, 30))

    treeTopSprite = createSpriteSurface(pygame.image.load('img/terrain2.png').convert(), 221, 170, 16, 16, WHITE)
    treeTopSprite = pygame.transform.scale(treeTopSprite, (30, 30))

    treeBottom = createSpriteSurface(pygame.image.load('img/terrain2.png').convert(), 221, 187, 16, 16, WHITE)
    treeBottom = pygame.transform.scale(treeBottom, (30, 30))

    spriteSets = {'Ball': ball, 'Dog': dogSprite.dogSpriteSheet, 'Player': manSprite.humanSpriteSheet,
                  'Squirrel': squirrelSprite.squirrelSpriteSheet, 'Heart': love, 'Barrier': barrierSprite, 'Water': waterSprite,
                  'Tree Top': treeTopSprite, 'Tree Bottom': treeBottom, 'Duck': duckSprite.duckSpriteSheet, 'Bread': bread, 'Bread Scraps': breadScraps,
                  'Barrier Down': barrierDown, 'Barrier Accross': barrierAccross}

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
    water = []

    iteractionCharacters = {}

    iteractionCharacters.update({'Player': player})
    iteractionCharacters.update({'Dogs': dogs})
    iteractionCharacters.update({'Barriers': barriers})
    iteractionCharacters.update({'Items': items})
    iteractionCharacters.update({'Trees': trees})
    iteractionCharacters.update({'Ground': ground})
    iteractionCharacters.update({'Water': water})
    iteractionCharacters.update({'Squirrels': squirrels})
    iteractionCharacters.update({'Ducks': []})


    return iteractionCharacters

def make_game(gap, clock, terrain, actors):
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
            newTerrain = createTerrain(terrain[j][i], i, j, gap)
            spriteGroup.add(newTerrain)

            gameData.characters.get('Ground').append(newTerrain)

            # append a general node to gamegrid for pathfinding
            grid[i].append(Node(i, j, gap, len(terrain), gameData.characters, newTerrain.weight))

            #create actor
            createActor(actors[j][i], i, j, gap, gameData, clock)

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
            #print(event.button)
            if event.button == 1:

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

            elif event.button == 3:
                for ground in game.characters.get('Ground'):
                    if ground.rect.collidepoint(pos) == 1:

                        game.characters.get('Player').throwBread(ground)


def main():
    #initialise pygam
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, WIDTH))

    #set the game clock
    clock = pygame.time.Clock()

    #create grid, creates all the game sprites and characters
    game = make_game(GAP, clock, pondterrain, pondactors)


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

