import pygame
from pygame.locals import Rect

class Wall:
    def __init__(self, difficulty, screen_width, screen_height, bg, cols, rows):
        self.difficulty = difficulty
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.bg = bg
        self.cols = cols
        self.rows = rows
        self.width = screen_width // cols
        self.height = 50
        self.button_height = 50
        # block colours
        # will be changed depending on level of game 
        self.block_red = (242, 85, 96)
        self.block_green = (86, 174, 87)
        self.block_blue = (69, 177, 232)
        self.blocks = []  # an empty list for all blocks

    def generate_block_strength(self, row):
        if self.difficulty == 'easy':
            if row < 2:
                return 3
            elif row < 4:
                return 2
            else:
                return 1
        elif self.difficulty == 'medium':
            if row < 2:
                return 4
            elif row < 4:
                return 3
            else:
                return 2
        elif self.difficulty == 'hard':
            if row < 2:
                return 5
            elif row < 4:
                return 4
            else:
                return 3

    def create_wall(self):
        for row in range(self.rows):
            block_row = []  # the block row list
            for col in range(self.cols):
                # generate x and y positions for each block
                block_x = col * self.width
                block_y =  row * self.height + self.button_height
                rect = pygame.Rect(block_x, block_y, self.width, self.height)
                # assign block strength based on row and difficulty
                strength = self.generate_block_strength(row)
                # store individual block
                block_row.append([rect, strength])
            self.blocks.append(block_row)  # append the block row to the wall
            
    def draw_wall(self, screen):
        for row in self.blocks:
            for block in row:
                # assign colour based on block strength
                if block[1] == 3:
                    block_col = self.block_blue
                elif block[1] == 2:
                    block_col = self.block_green
                elif block[1] == 1:
                    block_col = self.block_red
                pygame.draw.rect(screen, block_col, block[0])
        for row in self.blocks:
            for block in row:
                pygame.draw.rect(screen, self.bg, block[0], 4)
   