import pygame

class Wall:
    def __init__(self, difficulty, screen_width, screen_height, bg, cols, rows):
        """Constructor for creating an object of the Wall class

        Parameters:
            difficulty (string): The diffiuculty level of the game 
            screen_width (float): The width of screen
            screen_height (float): The height of screen
            bg (tuple): color of background in RGB format
            cols (int): amount of cloumns (for bricks)
            rows (int): amount of rows (for bricks)
        """
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
        self.block_orange = (234, 159, 10)
        self.block_violet = (211, 13, 229)
        self.blocks = []  # an empty list for all blocks

    def generate_block_strength(self, row):
        """Generate strenght of all bricks on the wall depending of the level of the game 

        Parameters:
            row (float): amount of rows 

        Returns:
            int: The strength of certain brick
        """
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
        """Create list bricks for the wall 
        """
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
        """Draw bricks on the window 

        Parameters:
            screen (object): An object of the Window class
        """
        for row in self.blocks:
            for block in row:
                block_col = 0
                # assign colour based on block strength
                if block[1] == 5:
                    block_col = self.block_violet
                elif block[1] == 4:
                    block_col = self.block_orange
                elif block[1] == 3:
                    block_col = self.block_blue
                elif block[1] == 2:
                    block_col = self.block_green
                elif block[1] == 1:
                    block_col = self.block_red
                pygame.draw.rect(screen, block_col, block[0])
        for row in self.blocks:
            for block in row:
                pygame.draw.rect(screen, self.bg, block[0], 4)
   