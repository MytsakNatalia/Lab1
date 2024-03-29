import pygame
from pygame.locals import Rect


class Paddle:
    def __init__(self, screen_width, screen_height):# screen width and height
        self.reset(screen_width, screen_height)


    def move(self, screen_width):
        """
                Move the paddle based on user input.

                Parameters:
                - screen_width (int): Width of the game screen.

                Returns:
                Rect: Updated rectangle representing the paddle.
                """

        self.direction = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rectangle.left>0:
            self.rectangle.x -=self.speed
            self.direction = -1
        if key[pygame.K_RIGHT] and self.rectangle.right<screen_width:
            self.rectangle.x +=self.speed
            self.direction  =1
        return self.rectangle

    def draw(self, screen):
        """
                Draw the paddle on the specified screen.

                Parameters:
                - screen: Pygame window to draw on.
                """
        pygame.draw.rect(screen, self.fill_color, self.rectangle)
        pygame.draw.rect(screen, self.outline_color, self.rectangle, 3)

    def reset(self, screen_width, screen_height):
        """
                Initialize the paddle with specified screen width and height.

                Parameters:
                - screen_width (int): Width of the game screen.
                - screen_height (int): Height of the game screen.
                """
        # reset paddle variables
        self.height = 20
        self.width = int(screen_width / 6)  # has to be changed based on number of colors
        self.x = int((screen_width / 2) - (self.width / 2))
        self.y = int(screen_height - (self.height * 2))
        self.speed = 5
        self.rectangle = Rect(self.x, self.y, self.width, self.height)
        self.direction = 0
        self.fill_color = (142, 135, 123)
        self.outline_color = (100, 100, 100)

