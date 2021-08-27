from config import *
from pygame import *
class Node(pygame.sprite.Sprite):
	def __init__(self, row, col, width, total_rows, spriteSheet):


		pygame.sprite.Sprite.__init__(self)
		self._layer = 0
		self.image = self.createSprite(spriteSheet, 178, 143, width, width)
		self.rect = self.image.get_rect()
		self.x = row * width
		self.y = col * width
		self.rect.x = self.x
		self.rect.y = self.y
		self.pos = vec((self.x, self.y))


		self.row = row
		self.col = col

		self.width = width
		self.color = PINK
		self.neighbors = []
		self.width = width
		self.total_rows = total_rows
		self.state = ''
		self.f = 0
		self.g = 0
		self.h = 0
		self.parent = [0, 0]


	def get_pos(self):
		return self.row, self.col

	def createSprite(self, spriteSheet, x, y, width, height):
		sprite = pygame.Surface([width, height])
		sprite.blit(spriteSheet, (0, 0), (x, y, width, height))
		sprite.set_colorkey(BLACK)
		return sprite

	def updatePosition(self, position):

		self.row = position[0]
		self.col = position[1]
		self.pos.x = position[0] * 30
		self.pos.y = position[1] * 30

		self.rect.x = self.pos.x
		self.rect.y = self.pos.y


	def get_pos(self):
		return self.row, self.col

	def get_color(self):
		return self.color

	def is_closed(self):
		return self.color == RED

	def is_open(self):
		return self.color == GREEN

	def is_barrier(self):
		return self.color == BLACK

	def is_start(self):
		return self.color == ORANGE

	def is_end(self):
		return self.color == TURQUOISE

	def make_light_blue(self):
		self.color = LIGHTBLUE

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

	def make_path(self):
		self.color = PURPLE

	def make_player(self):
		self.color = GREY

	def make_NPC(self):
		self.color = BLUE

	def update_neighbors(self, grid):
		self.neighbors = []
		if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].getState() == 'barrier': # DOWN
			self.neighbors.append(grid[self.row + 1][self.col])

		if self.row > 0 and not grid[self.row - 1][self.col].getState() == 'barrier': # UP
			self.neighbors.append(grid[self.row - 1][self.col])

		if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].getState() == 'barrier': # RIGHT
			self.neighbors.append(grid[self.row][self.col + 1])

		if self.col > 0 and not grid[self.row][self.col - 1].getState() == 'barrier': # LEFT
			self.neighbors.append(grid[self.row][self.col - 1])

	def __lt__(self, other):
		return False