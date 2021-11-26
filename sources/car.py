import pygame
import math

coef_turn = 0.3
coef_drift = 0.07 # adhérence au sol
coef_vel = 10

class Car:
    def __init__(self):
        self.dir_target = -1
        self.dir = -1
        self.posx = 0
        self.velx = -1

        self.w = 50
        self.h = 100

    def update(self, dt):
        self.dir += dt * coef_turn * (self.dir_target - self.dir)
        if abs(self.dir - self.velx) < 0.1:
            self.velx = self.dir
        self.velx += dt * coef_drift * (self.dir - self.velx)
        self.posx += dt * coef_vel * self.velx

    def display(self, screen):
        theta = math.atan2(self.dir, 1)
        points = []
        
        for i in [1, -1]:
            for j in [i, -i]:
                x = 1920/2 + i * self.w / 2 * math.cos(theta) - j * self.h / 2 * math.sin(theta)
                y = 700 + i * self.w / 2 * math.sin(theta) + j * self.h / 2 * math.cos(theta)
                points.append((x, y))
        pygame.draw.polygon(screen, (255, 0, 0), points)