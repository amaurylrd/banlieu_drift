import pygame
import ctypes

from car import Car
from map import Map

start = None
score = 0

def render(screen):
    screen_width, screen_height = pygame.display.get_surface().get_size()
    screen.fill((0, 0, 0))
    
    global score
    score = (pygame.time.get_ticks() - start) / 330
    font = pygame.font.Font('./ressources/fonts/Over the Rainbow.ttf', 60)
    txt = font.render(str(int(score)), True, (255, 255, 255))
    txt_pos = txt.get_rect(center = (screen_width / 2, font.get_ascent()))
    screen.blit(txt, txt_pos)
    
    
    map.display(screen, score, car.posx)
    car.display(screen)
    
    pygame.display.update()
    
def update(dt : int = 1):
    car.update(dt)

def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                car.dir_target = -1
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return True
            if event.key == pygame.K_SPACE:
                car.dir_target = 1
    
    return False

car = Car()
map = Map()

def main():
    pygame.init()
    
    screen_size = pygame.display.Info().current_w, pygame.display.Info().current_h
    screen = pygame.display.set_mode(screen_size, False)
    
    pygame.display.set_caption('Banlieu Drift')

    global start
    clock = pygame.time.Clock()
    start = pygame.time.get_ticks()
    
    while not process_events():
        update()
        render(screen)
        clock.tick(60)
        
    pygame.quit()

if __name__ == '__main__':
    main()