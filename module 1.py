import time
from random import randrange


class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)

class Npc():

    def __init__(self, x):
        self.position = x
        self.value = "$"
        self.directions = ['up', 'down', 'left', 'right',  'up-left', 'up-right', 'down-left', 'down-right']

    def getLocation(self):
        return (self.position)

    def updatePostion(self, maze, newPosition):

        print(newPosition)
       
        if(maze.returnGridValue(newPosition))== 0:
            #print("hello")
           
            maze.updateMaze(self.position, 0)
            self.position = newPosition
           
            maze.updateMaze(self.position, self.value)
        elif (maze.returnGridValue(newPosition))== 4:
            print("finished")
           
       
    def chooseRandomDirection(self, maze):
        self.moveNpc(maze, self.directions[randrange(7)])
       


    def moveNpc(self, maze, direction):
        newPosition = [0,0]
       

        if direction == 'up':
            newPosition[0] = self.position[0] - 1
            newPosition[1] = self.position[1]
            self.updatePostion(maze, newPosition)
               

        elif direction == 'up-left':
            newPosition[0] = self.position[0] - 1
            newPosition[1] = self.position[1] - 1
            self.updatePostion(maze, newPosition)

        elif direction == 'up-right':
            newPosition[0] = self.position[0] - 1
            newPosition[1] = self.position[1] + 1
            self.updatePostion(maze, newPosition)



        elif direction == 'down':
            newPosition[0] = self.position[0] + 1
            newPosition[1] = self.position[1]
            self.updatePostion(maze, newPosition)



        elif direction == 'down-left':
            newPosition[0] = self.position[0] + 1
            newPosition[1] = self.position[1] - 1
            self.updatePostion(maze, newPosition)



        elif direction == 'down-right':
            newPosition[0] = self.position[0] + 1
            newPosition[1] = self.position[1] + 1
            self.updatePostion(maze, newPosition)

        elif direction == 'left':
            newPosition[0] = self.position[0]
            newPosition[1] = self.position[1] - 1
            self.updatePostion(maze, newPosition)



        elif direction == 'right':
            newPosition[0] = self.position[0]
            newPosition[1] = self.position[1] + 1
            self.updatePostion(maze, newPosition)



class Environment():
    def __init__(self, maze):
        self.maze = maze

    def updateMaze(self, position, value):
        #print("kay")
        #print(value)
        #print(position)
        self.maze[position[0]][position[1]] = value
        #print(self.maze)

    def getMaze(self):
        return self.maze

    def returnGridValue(self, position):
        try:
            return self.maze[position[0]][position[1]]
        except:
            return 100

   

def main():

    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    maze1 = Environment(maze)

    npc1 = Npc([0,0])



    path = astar(maze1.getMaze(), npc1.getLocation(), (7, 6))
    print(path)

    maze1.updateMaze(npc1.getLocation(), "$")
    maze1.updateMaze((7,6), 4)
   
    gameOn = True
   
    while gameOn:
        if (time.time() % 5) == 0:
            #npc1.chooseRandomDirection(maze1)
            print(maze1.getMaze())
            npc1.updatePostion(maze1, path.pop(0))
           
   


if __name__ == '__main__':
    main()
