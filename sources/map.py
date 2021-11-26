from random import randint

def draw_tile(x, y):
	for i in [1, -1]:
		for j in [i, -i]:
			xr = 1920//2 + x + i * 50 
			yr = 700 + j * 50
			points.append((x, y))
	pygame.draw.polygon(screen, (255, 0, 0), points)

class Map:
	def __init__(self):
		self.tiles = []
		self.lastscore = 0
		for i in range(10):
			self.__get_next_tile()
	
	def __get_next_tile(self):
		self.tiles.append(2 * randint(0, 1) - 1)

	def display(self, score: int):
		if score - 5 > self.lastscore:
    		self.__get_next_tile()
			self.tiles = self.tiles[1:]
		x = 0
		for t in self.tiles:
			x += t * 

