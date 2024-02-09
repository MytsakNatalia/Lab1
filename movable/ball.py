import pygame
from pygame.locals import *


class Ball:
    def __init__(self, x, y):
        self.reset(x, y)
        self.fill_color = (142, 135, 123)
        self.outline_color = (100, 100, 100)

    def reset(self, x, y):
        self.ball_rad = 10
        self.x = x - self.ball_rad
        self.y = y
        self.rect = Rect(self.x, self.y, self.ball_rad * 2, self.ball_rad * 2)
        self.speed_x = 4
        self.speed_y = -4
        self.speed_max = 5
        self.game_over = 0

    def draw(self, window):
        pygame.draw.circle(window, self.fill_color, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad),
                           self.ball_rad)
        pygame.draw.circle(window, self.fill_color, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad),
                           self.ball_rad, 3)