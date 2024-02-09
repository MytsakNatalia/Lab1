import pygame
from pygame.locals import *

pygame.init()

width = 600
height = 600
bg_color = (234, 218, 184)

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Arkanoid")

class Paddle:
    def __init__(self):
        self.height = 20
        self.width = int(width/6)# has to be changed based on number of colors
        self.x = int((width/2) - (self.width/2))
        self.y = height - (self.height*2)
        self.speed = 10
        self.rectangle = Rect(self.x, self.y, self.width, self.height)
        self.direction = 0

class Game:
    def __init__(self):
        self.continueGame = True

    def run(self):
        while self.continueGame:
            window.fill(bg_color)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.continueGame = False
            pygame.display.flip()

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()