import pygame
from pygame.locals import Rect

class Wall:
    def __init__(self, screen_width, screen_height, bg, cols, rows):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.bg = bg
        self.cols = cols
        self.rows = rows
        self.width = screen_width // cols
        self.height = 50
        # block colours
        # will be changed depending on level of game 
        self.block_red = (242, 85, 96)
        self.block_green = (86, 174, 87)
        self.block_blue = (69, 177, 232)
        self.blocks = []  # an empty list for all blocks

   