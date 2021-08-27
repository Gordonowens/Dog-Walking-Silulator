import pygame
# from sprites import *
from config import *
import sys
from Node import Node


def make_grid(width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):

            node = Node(i, j, gap, rows)
            grid[i].append(node)

    return grid


def draw(win, grid, rows, width):
    win.fill(WHITE)

    for row in grid:
        for node in row:
            node.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()


def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))


def main():
    grid = make_grid(WIDTH)

    start = None
    end = None

    run = True
    while run:
        draw(WIN, grid, WIDTH)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False



    pygame.quit()


main()
