import pygame
from pygame.locals import *
from movable.ball import  Ball
from movable.paddle import  Paddle
from unmovable.wallBricks import Wall

pygame.init()

width = 600
height = 600
bg_color = (234, 218, 184)

cols = 6
rows = 6

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Arkanoid")
clock = pygame.time.Clock()
fps = 60
font = pygame.font.SysFont('Constantia', 30)
text_col = (78, 81, 139)


def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	window.blit(img, (x, y))

class Game:
    def __init__(self):
        self.continueGame = True
        self.paddle = Paddle(width, height)
        self.ball = Ball(int(self.paddle.x + (self.paddle.width // 2)), int(self.paddle.y - self.paddle.height))# must be replaced with paddle dimensions
        self.wall = Wall(width, height, bg_color, cols, rows )       
        self.wall.create_wall()
        self.wall.draw_wall(window)

        self.paddle.draw(window)
        

    def run(self):



        while self.continueGame:

            self.ball.draw(window)            
            window.fill(bg_color)
            self.ball.draw(window)
            self.wall.draw_wall(window)
            self.paddle.move(width)
            self.paddle.draw(window)
            
            live_ball =True

            if live_ball:
                # draw paddle
                self.paddle.move(width)
                # draw ball
                game_over = self.ball.move(self.wall, self.paddle, width, height)
                if game_over != 0:
                    live_ball = False

                # print player instructions
            if not live_ball:
                if game_over == 0:
                    draw_text('CLICK ANYWHERE TO START', font, text_col, 100, height // 2 + 100)
                elif game_over == 1:
                    draw_text('YOU WON!', font, text_col, 240, height // 2 + 50)
                    draw_text('CLICK ANYWHERE TO START', font, text_col, 100, height // 2 + 100)
                elif game_over == -1:
                    draw_text('YOU LOST!', font, text_col, 240, height // 2 + 50)
                    draw_text('CLICK ANYWHERE TO START', font, text_col, 100, height // 2 + 100)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.continueGame = False





            pygame.display.update()
            clock.tick(fps)


        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()