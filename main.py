import pygame, os
from Wave import Wave, Coord
os.environ["SDL_VIDEO_WINDOW_POS"] = "15,30"

pygame.display.init()
size = Coord(1000,600)
screen = pygame.display.set_mode(size)
wave = Wave(screen, size)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    wave.update()
    wave.draw()
    pygame.display.update()
