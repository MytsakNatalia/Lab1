import pytest
import pygame
from movable.ball import Ball
from movable.paddle import Paddle
from unmovable.wallBricks import Wall

@pytest.fixture
def ball():
    pygame.init()
    return Ball(100, 100)

def test_reset(ball):
    ball.reset(200, 200)
    assert  ball.ball_rad == 10
    assert ball.x == 190
    assert ball.y == 200
    assert ball.rect.width == ball.ball_rad * 2
    assert ball.rect.height == ball.ball_rad * 2
    assert ball.speed_x == 4
    assert ball.speed_y == -4
    assert ball.game_over == 0

def test_draw(ball):
    # Not the ideal way to test draw function, but we can at least check if it doesn't raise an error
    window = pygame.display.set_mode((750, 750))
    ball.draw(window)

##Add colision from left/right
##Add colision with wall right/left


## Action: Ball hits the last one weak brick from above (below)
## Result: All wall is desrtoyed 
## VICTORY
def test_move_collision_last_weak_brick(ball):   
    # Simulate collision with a last one weak brick 
    class MockWall:
        def __init__(self):
            self.blocks = [[[pygame.Rect(0, 50, 750, 50), 1]]]  
    wall = MockWall()
    paddle = None 
    init_ball_speed_y = ball.speed_y
    init_ball_rect_y = ball.rect.y
    game_state = ball.move(wall, paddle, 750, 750)
    assert ball.speed_y == init_ball_speed_y 
    assert ball.rect.y == init_ball_rect_y + ball.speed_y
    assert wall.blocks[0][0][1] == 1     
    assert game_state == 0  ##Game victory  

## Action: Ball hits the strong brick from above (below)
## Result: Brick stil ecxisting and wall is also
## CONTINUE
def test_move__collision_strong_brick(ball):   
    # Simulate collision with a strong brick 
    class MockWall:
        def __init__(self):
            self.blocks = [[[pygame.Rect(0, 50, 750, 50), 2]]]  
    wall = MockWall()
    paddle = None 
    init_ball_speed_y = ball.speed_y
    init_ball_rect_y = ball.rect.y
    game_state = ball.move(wall, paddle, 750, 750)
    assert ball.speed_y == init_ball_speed_y 
    assert ball.rect.y == init_ball_rect_y + ball.speed_y
    assert wall.blocks[0][0][1] == 2       
    assert game_state == 0  ##Game continue 
    
## Action: Ball hits the weak brick from above (below)
## Result: Brick is destroyed but wall stil ecxisting
## CONTINUE
def test_move_collision_oneof_weak_bricks_(ball):   
    # Simulate collision with a weak brick 
    class MockWall:
        def __init__(self):
            self.blocks = [[[pygame.Rect(0, 50, 375, 50), 2], [pygame.Rect(375, 50, 375, 50), 1]]]  
    wall = MockWall()
    paddle = None 
    init_ball_speed_y = ball.speed_y
    init_ball_rect_y = ball.rect.y
    game_state = ball.move(wall, paddle, 750, 750)
    assert ball.speed_y == init_ball_speed_y 
    assert ball.rect.y == init_ball_rect_y + ball.speed_y
    assert wall.blocks[0][1][1] == 1
    assert game_state == 0  ##Game continue 


## Action: Ball hits the "ceiling" (top of wall)
## Result: Ball jumps out from the top of the wall 
## CONTINUE
def test_move_top_collision(ball):
    # Simulate collision with top of the screen
    class MockWall:
        def __init__(self):
            self.blocks = []  # No blocks in the wall
    wall = MockWall()
    paddle = None      
    ball.y = -4
    init_ball_rect_y = ball.speed_y
    game_state = ball.move(wall, paddle, 750, 750)
    assert ball.speed_y == init_ball_rect_y    
    assert game_state == 1  ##Game continue 

## Action: Ball hits the "floor" (bottom of wall)
## Result: GAME OVER 
## GAME OVER
def test_move_bottom_collision(ball):
    # Simulate collision with bottom of the screen
    class MockWall:
        def __init__(self):
            self.blocks = []  # No blocks in the wall
    wall = MockWall()
    paddle = None  
    ball.y = 750 - ball.ball_rad * 2
    ball.speed_y = 4
    game_state = ball.move(wall, paddle, 750, 750)
    assert game_state == 1  # Game over


def test_move_collision_left_wall(ball):
    # Simulate collision with left side of the wall
    class MockWall:
        def __init__(self):
            self.blocks = []  # No blocks in the wall
    wall = MockWall()
    paddle = None     
    ball.x = ball.ball_rad  
    ball.speed_x = -4 
    init_ball_speed_x = ball.speed_x
    init_ball_rect_x = ball.rect.x
    print(init_ball_speed_x, "  ", init_ball_rect_x)
    game_state = ball.move(wall, paddle, 750, 750)
    print( ball.speed_x , "  ", ball.rect.x)
    assert ball.speed_x == init_ball_speed_x 
    assert ball.rect.x == init_ball_rect_x + ball.speed_x  
    assert game_state == 1  # Game continue

## Action: Ball hits the paddle
## Result: ball jump out from paddle 
## CONTINUE
def test_move_paddle_collision(ball):
    # Simulate collision with paddle
    class MockWall:
        def __init__(self):
            self.blocks = []  # No blocks in the wall
    wall = MockWall()
    class MockPaddle:
        def __init__(self):
            self.rectangle = pygame.Rect(100, 500, 100, 20) 
            self.direction = 0  
    paddle = MockPaddle()    
    ball.y = 480
    ball.speed_y = 4
    init_ball_speed_y = ball.speed_y
    init_ball_speed_x = ball.speed_x
    init_ball_rect_x = ball.rect.x
    init_ball_rect_y = ball.rect.y
    game_state = ball.move(wall, paddle, 600, 800)
    assert ball.speed_y == init_ball_speed_y 
    assert ball.speed_x == init_ball_speed_x 
    assert ball.rect.x == init_ball_rect_x + ball.speed_x
    assert ball.rect.y == init_ball_rect_y + ball.speed_y    
    assert game_state == 1  # Game continue

