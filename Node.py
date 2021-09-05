from config import *
from pygame import *
class Node():

	def __init__(self, row, col, width, total_rows, characters, w = 3):

		#variables for game grid
		self.row = row
		self.col = col
		self.total_rows = total_rows

		#these variables are used by the pathfinding algorithm
		self.state = ''
		self.neighbors = []
		self.characters = characters
		self.w = w

	def get_pos(self):
		return self.row, self.col

	def getState(self):
		return self.state

	def make_start(self):
		self.state = 'start'

	def make_closed(self):
		self.state = 'closed'

	def make_open(self):
		self.state = 'open'

	def make_end(self):
		self.state = 'end'

	def checkNodes(self, barrierType, position):

		nodeState = False

		for barrier in self.characters.get(barrierType):
			if barrier.get_pos() == position:
				nodeState = True
				break

		return nodeState

	def update_neighbors(self, grid, barriers):
		'''
		gets all the neighbor nodes that are not barriers and updates self.neighbors
		:list grid: grid to find path on

		'''

		self.neighbors = []

		#down
		if self.row < self.total_rows - 1 and not self.checkNodes('Barriers', (self.row + 1, self.col)):
			self.neighbors.append(grid[self.row + 1][self.col])

		#down right
		if (self.row < self.total_rows - 1 and self.col < self.total_rows - 1 ) and not self.checkNodes('Barriers', (self.row + 1, self.col + 1)):
			self.neighbors.append(grid[self.row + 1][self.col + 1])

		#down left
		if (self.row < self.total_rows - 1 and self.col > 0) and not self.checkNodes('Barriers', (self.row + 1, self.col - 1)):
			self.neighbors.append(grid[self.row + 1][self.col - 1])


		#up
		if self.row > 0 and not self.checkNodes('Barriers', (self.row - 1, self.col)):
			self.neighbors.append(grid[self.row - 1][self.col])

		#up right
		if (self.row > 0 and self.col < self.total_rows - 1 ) and not self.checkNodes('Barriers', (self.row - 1, self.col + 1)):
			self.neighbors.append(grid[self.row - 1][self.col + 1])

		#up left
		if (self.row > 0 and self.col > 0) and not self.checkNodes('Barriers', (self.row - 1, self.col - 1)):
			self.neighbors.append(grid[self.row - 1][self.col - 1])

		#right
		if self.col < self.total_rows - 1 and not self.checkNodes('Barriers', (self.row, self.col + 1)):
			self.neighbors.append(grid[self.row][self.col + 1])

		#left
		if self.col > 0 and not self.checkNodes('Barriers', (self.row, self.col - 1)):
			self.neighbors.append(grid[self.row][self.col - 1])

	def __lt__(self, other):
		'''
		i dont know what this does
		'''
		return False