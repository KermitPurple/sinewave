import pygame
from collections import namedtuple
from numpy import sin

Coord = namedtuple("Coord", ['x', 'y'])

class Wave:
    def __init__(self, screen, size):
        self.screen = screen
        self.size = size
        self.offset = 0

    def draw(self):
        points = []
        for x in range(self.size.x):
            theta = x / 3.141592 * 180 / 1500 - self.offset
            y = int((self.size.y/2 - 10) * sin(theta)) + self.size.y/2
            points.append(Coord(x, y))
        pygame.draw.aalines(self.screen, self.getColor(), False, points)

    def update(self):
        self.offset += 0.04

    def getColor(self):
        color = pygame.Color(0, 0, 0)
        color.hsva = ((self.offset * 100) % 360, 100, 100)
        return color
