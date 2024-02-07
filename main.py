import pygame
from pygame.locals import *

pygame.init()

width = 600
height = 600

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Arkanoid")

class Game:
    def __init__(self):
        self.continueGame = True

    def run(self):
        while self.continueGame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.continueGame = False

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()