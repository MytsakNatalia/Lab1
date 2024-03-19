import pytest
import pygame
from movable.ball import Ball

@pytest.fixture
def ball():
    pygame.init()
    return Ball(100, 100)

def test_reset(ball):
    ball.reset(200, 200)
    assert  ball.ball_rad == 10
    assert ball.x == 190
    assert ball.y == 200
    assert ball.rect.width == 20
    assert ball.rect.height == 20
    assert ball.speed_x == 4
    assert ball.speed_y == -4
    assert ball.game_over == 0

def test_draw(ball):
    # Not the ideal way to test draw function, but we can at least check if it doesn't raise an error
    window = pygame.display.set_mode((800, 600))
    ball.draw(window)

def test_move_wall_collision(ball):
    # Simulate collision with a wall
    class MockWall:
        def __init__(self):
            self.blocks = [[[pygame.Rect(50, 50, 50, 20), 1]]]  # Example block
    wall = MockWall()
    paddle = None  # Not needed for this test
    game_state = ball.move(wall, paddle, 600, 800)
    assert game_state == 0  # Game state should still be ongoing

def test_move_top_collision(ball):
    # Simulate collision with top of the screen
    ball.y = 0
    ball.speed_y = -4
    ball.move(None, None, 600, 800)
    assert ball.speed_y == 4  # Y speed should be reversed

def test_move_bottom_collision(ball):
    # Simulate collision with bottom of the screen
    ball.y = 600 - ball.ball_rad * 2
    ball.speed_y = 4
    game_state = ball.move(None, None, 600, 800)
    assert game_state == -1  # Game state should be game over

def test_move_paddle_collision(ball):
    # Simulate collision with paddle
    class MockPaddle:
        def __init__(self):
            self.rectangle = pygame.Rect(100, 500, 100, 20)  # Example paddle position
            self.direction = 0  # Example paddle direction
    paddle = MockPaddle()
    ball.y = 480
    ball.speed_y = 4
    game_state = ball.move(None, paddle, 600, 800)
    assert game_state == 0  # Game state should still be ongoing
    

