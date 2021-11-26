import pygame
import math

coefdrift = 0.6
coefvel = 10

class Car:
    def __init__(self):
        self.dir = -1
        self.posx = 0
        self.velx = -1

        self.w = 50
        self.h = 100

    def update(self, dt):
        self.velx += dt * coefdrift * (self.dir - self.velx)
        self.posx += dt * coefvel * self.velx

    def display(self, screen):
        theta = math.atan2(self.velx, 2)
        points = []
        
        for i in [1, -1]:
            for j in [i, -i]:
                x = 1920//2 + self.posx + i * self.w / 2 * math.cos(theta) - j * self.h / 2 * math.sin(theta) 
                y = 700 + i * self.w / 2 * math.sin(theta) + j * self.h / 2 * math.cos(theta)
                points.append((x, y))
        pygame.draw.polygon(screen, (255, 0, 0), points)