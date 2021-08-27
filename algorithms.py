from queue import PriorityQueue
import numpy as np

def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        current = came_from[current]
        path.append(current)

    return path


def algorithm(grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            #ENEMY[0].updatePath(reconstruct_path(came_from, end))
            #end.make_end()
            return reconstruct_path(came_from, end)

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()



        if current != start:
            current.make_closed()

    return []


def getGridSquare(pos, size, grid):
    '''
    slices a list and returns a square around a position
    :param pos: (int, int) tuple at the centre of the square
    :param size: int size of the square. how many rows and columns out
    :param grid: 2d list [[]]
    :return: 2d list
    '''
    #set to numpy array
    grid = np.array(grid)

    # need to update grid[ax]
    # get upper square co-ordinates
    ax = pos[0] - size
    ay = pos[0] + size + 1

    # get lower square co-ordinates
    bx = pos[1] - size
    by = pos[1] + size + 1


    # check if upper left square inbounds
    if (ax < 0 and bx < 0):
        return grid[0:ay, 0:by].tolist()

    # check if upper right square inbounds
    elif (ax < 0 and by > len(grid[ax])):

        return grid[0:ay, bx:len(grid[ax])].tolist()

    #check if lower left is in bounds
    elif (ay > len(grid) and bx < 0):

        return grid[ax:len(grid), 0: by].tolist()

    #check if lower right is in bounds
    elif (ay > len(grid) and by > len(grid[ax])):

        return grid[ax:len(grid), bx: len(grid[ax])].tolist()

    #upper
    elif(ax < 0):
        print("upper")
        return grid[0:ay, bx:by].tolist()

    #left
    elif(bx < 0):
        print("left")
        return grid[ax:ay, 0:by].tolist()

    #lower
    elif(ax > len(grid)):
        print("lower")
        return grid[len(grid):ay, bx:by].tolist()

    #right
    elif(bx > len(grid[ax])):
        print("right")
        return grid[ax:ay, 0:by].tolist()

    else:
        print("return")
        return grid[ax:ay, bx:by].tolist()