from config import *
from pygame import *
class Node(pygame.sprite.Sprite):
	def __init__(self, row, col, width, total_rows, spriteSheet):

		pygame.sprite.Sprite.__init__(self)
		#variables for sprite
		self._layer = 0
		self.image = self.createSprite(spriteSheet, 178, 143, width, width)
		self.rect = self.image.get_rect()
		self.x = row * width
		self.y = col * width
		self.rect.x = self.x
		self.rect.y = self.y
		self.width = width

		#variables for game grid
		self.pos = vec((self.x, self.y))
		self.row = row
		self.col = col
		self.total_rows = total_rows

		#these variables are used by the pathfinding algorithm
		self.state = ''
		self.neighbors = []

	def get_pos(self):
		return self.row, self.col

	def createSprite(self, spriteSheet, x, y, width, height):
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
		#this is used to create transperancy in the sprite
		sprite.set_colorkey(BLACK)
		return sprite

	def updatePosition(self, position):
		'''
		:tuple position: x, y
		:return:
		'''

		#update position on game grid
		self.row = position[0]
		self.col = position[1]
		#set position of upper left of sprites rectangle
		self.pos.x = position[0] * 30
		self.pos.y = position[1] * 30

		#update sprite rectangle
		self.rect.x = self.pos.x
		self.rect.y = self.pos.y


	def get_pos(self):
		return self.row, self.col

	def getState(self):
		return self.state

	def reset(self):
		self.color = WHITE

	def make_start(self):
		self.state = 'start'

	def make_closed(self):
		self.state = 'closed'

	def make_open(self):
		self.state = 'open'

	def make_barrier(self):
		self.state = 'barrier'

	def make_end(self):
		self.state = 'end'

	def update_neighbors(self, grid):
		'''
		gets all the neighbor nodes that are not barriers and updates self.neighbors
		:list grid: grid to find path on

		'''

		self.neighbors = []

		#down
		if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].getState() == 'barrier':
			self.neighbors.append(grid[self.row + 1][self.col])

		#up
		if self.row > 0 and not grid[self.row - 1][self.col].getState() == 'barrier':
			self.neighbors.append(grid[self.row - 1][self.col])

		#right
		if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].getState() == 'barrier':
			self.neighbors.append(grid[self.row][self.col + 1])

		#left
		if self.col > 0 and not grid[self.row][self.col - 1].getState() == 'barrier':
			self.neighbors.append(grid[self.row][self.col - 1])

	def __lt__(self, other):
		'''
		i dont know what this does
		'''
		return False