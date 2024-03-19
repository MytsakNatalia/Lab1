import pygame
from pygame.locals import *


class Ball:
    def __init__(self, x, y):
        self.reset(x, y)
        self.fill_color = (142, 135, 123)
        self.outline_color = (100, 100, 100)

    def reset(self, x, y):
        '''
        Reset the ball to its initial state with specified coordinates.
        :param x: X-coordinate for the ball.
        :param y:Y-coordinate for the ball

        '''
        self.ball_rad = 10
        self.x = x - self.ball_rad
        self.y = y
        self.rect = Rect(self.x, self.y, self.ball_rad * 2, self.ball_rad * 2)
        self.speed_x = 4
        self.speed_y = -4
        self.speed_max = 5
        self.game_over = 0

    def draw(self, window):
        '''
        Draw the ball on the specified window
        :param window: main game window

        '''
        pygame.draw.circle(window, self.fill_color, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad),
                           self.ball_rad)
        pygame.draw.circle(window, self.outline_color, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad),
                           self.ball_rad, 3)

    def move(self, wall, paddle, screen_height, screen_width):
        '''
        Move the ball, handle collisions with walls, paddle, and update game state
        :param wall:Wall object representing the blocks in the game.
        :param paddle: Paddle object representing the player's paddle.
        :param screen_height:Height of the game screen.
        :param screen_width:Width of the game screen.
        :return:Game state (-1 for game over, 0 for ongoing, 1 for victory).

        '''

        # collision threshold
        collision_thresh = 5

        # start off with the assumption that the wall has been destroyed completely
        wall_destroyed = 1
        row_count = 0
        for row in wall.blocks:
            item_count = 0
            for item in row:
                # check collision
                if self.rect.colliderect(item[0]):
                    # check if collision was from above
                    if abs(self.rect.bottom - item[0].top) < collision_thresh and self.speed_y > 0:
                        self.speed_y *= -1
                    # check if collision was from below
                    if abs(self.rect.top - item[0].bottom) < collision_thresh and self.speed_y < 0:
                        self.speed_y *= -1
                    # check if collision was from left
                    if abs(self.rect.right - item[0].left) < collision_thresh and self.speed_x > 0:
                        self.speed_x *= -1
                    # check if collision was from right
                    if abs(self.rect.left - item[0].right) < collision_thresh and self.speed_x < 0:
                        self.speed_x *= -1
                    # reduce the block's strength by doing damage to it
                    if wall.blocks[row_count][item_count][1] > 1:
                        wall.blocks[row_count][item_count][1] -= 1
                    else:
                        wall.blocks[row_count][item_count][0] = (0, 0, 0, 0)

                # check if block still exists, in whcih case the wall is not destroyed
                if wall.blocks[row_count][item_count][0] != (0, 0, 0, 0):
                    wall_destroyed = 0
                # increase item counter
                item_count += 1
            # increase row counter
            row_count += 1
        # after iterating through all the blocks, check if the wall is destroyed
        if wall_destroyed == 1:
            self.game_over = 1

        # check for collision with walls
        if self.rect.left < 0 or self.rect.right > screen_width:
            self.speed_x *= -1

        # check for collision with top and bottom of the screen
        if self.rect.top < 0:
            self.speed_y *= -1
        if self.rect.bottom > screen_height:
            self.game_over = -1

        # look for collission with paddle
        if self.rect.colliderect(paddle.rectangle):
            # check if colliding from the top
            if abs(self.rect.bottom - paddle.rectangle.top) < collision_thresh and self.speed_y > 0:
                self.speed_y *= -1
                self.speed_x += paddle.direction
                if self.speed_x > self.speed_max:
                    self.speed_x = self.speed_max
                elif self.speed_x < 0 and self.speed_x < -self.speed_max:
                    self.speed_x = -self.speed_max
            else:
                self.speed_x *= -1

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        return self.game_over