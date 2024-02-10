import pygame
from pygame.locals import *
from movable.paddle import  Paddle

pygame.init()

width = 600
height = 600
bg_color = (234, 218, 184)

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Arkanoid")
clock = pygame.time.Clock()
fps = 60

class Game:
    def __init__(self):
        self.continueGame = True
        self.paddle = Paddle(width, height)
        self.paddle.draw(window)

    def run(self):



        while self.continueGame:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.continueGame = False

            window.fill(bg_color)
            self.paddle.move(width)
            self.paddle.draw(window)

            pygame.display.update()
            clock.tick(fps)


        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()