from random import randint
import pygame

def draw_tile(screen, x, y, camx):
	points = []
	for i in range(4):
		xr = 1920//2 + x * 200 + i%2 * (i-2) * 200 - camx
		yr = 1280 - y * 200 + (i + 1)%2 * ((i + 1)%4-2) * 200
		points.append((xr, yr))
	pygame.draw.polygon(screen, (255, 255, 255), points)

class Map:
	def __init__(self):
		self.lastscore = 0
		self.dir = 1
		self.tiles = [-i for i in range(10)]
	
	def get_next_tile(self):
		r = randint(0, 2)
		if r == 0:
			self.dir *= -1
		if self.tiles:
			self.tiles.append(self.tiles[-1] + self.dir)
		else:
			self.tiles.append(0)

	def display(self, screen, score, camx):
		if score > self.lastscore + 1:
			self.get_next_tile()
			self.tiles = self.tiles[1:]
			self.lastscore += 1
		y = self.lastscore - score
		for t in self.tiles:
			x = t
			y += 1
			draw_tile(screen, x, y, camx)

