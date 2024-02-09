import pygame
from pygame.locals import *
from movable.ball import  Ball
pygame.init()

width = 600
height = 600
bg_color = (234, 218, 184)

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Arkanoid")

class Game:
    def __init__(self):
        self.continueGame = True
        self.ball = Ball(10, 10)# must be replaced with paddle dimensions


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