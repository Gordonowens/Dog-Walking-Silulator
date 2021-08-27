import pygame
# from sprites import *
from config import *
import sys
from Node import Node
import math
from queue import PriorityQueue

from Player import Player
from NPC import NPC
from Grid import*
from NPCAway import *


def make_grid(width):
    grid = []
    gameGrid = Grid([])
    gap = width // len(tilemap)
    for i in range(len(tilemap)):
        grid.append([])
        for j in range(len(tilemap)):
            if(tilemap[j][i] == "B"):
                node = Node(i, j, gap, len(tilemap), BLACK)
                grid[i].append(node)

            elif(tilemap[j][i] == "E"):
                node = Node(i, j, gap, len(tilemap), YELLOW)

                ENEMY.append(NPC(gameGrid, node))
                grid[i].append(node)

            elif(tilemap[j][i] == "P"):
                node = Node(i, j, gap, len(tilemap), GREY)
                PLAYER.append(Player(gameGrid, node))
                grid[i].append(node)

            elif(tilemap[j][i] == "A"):
                node = Node(i, j, gap, len(tilemap), BLUE)
                ENEMY.append(NPCAway(gameGrid, node))
                grid[i].append(node)


            else:
                node = Node(i, j, gap, len(tilemap))
                grid[i].append(node)

        gameGrid.setGrid(grid)
        #print(grid)
    return gameGrid


def draw(win, grid, width):
    win.fill(WHITE)

    for row in grid:
        for node in row:
            node.draw(win)

    draw_grid(win, width)
    pygame.display.update()


def draw_grid(win, width):
    gap = width // len(tilemap)
    for i in range(len(tilemap)):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(len(tilemap)):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))


def main():
    grid = make_grid(WIDTH)


    start = None
    end = None

    run = True
    while run:
        draw(WIN, grid.getGrid(), WIDTH)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    for row in grid.getGrid():
                        for node in row:
                            node.update_neighbors(grid.getGrid())



        PLAYER[0].update()
        for i in ENEMY:
            i.update()



    pygame.quit()


main()
