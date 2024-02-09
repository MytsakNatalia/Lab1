import pygame
from pygame.locals import Rect


class Paddle:
    def __init__(self, width, height):# screen width and height
        self.height = 20
        self.width = int(width/6)# has to be changed based on number of colors
        self.x = int((width/2) - (self.width/2))
        self.y = height - (self.height*2)
        self.speed = 10
        self.rectangle = Rect(self.x, self.y, self.width, self.height)
        self.direction = 0