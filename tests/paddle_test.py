import pytest
import pygame
from movable.paddle import Paddle
from pygame.locals import *
@pytest.fixture
def screen_width():
    return 750

@pytest.fixture
def screen_height():
    return 750

@pytest.fixture
def paddle(screen_width, screen_height):
    pygame.init()
    return Paddle(screen_width, screen_height)

def test_initialization(paddle, screen_width, screen_height):
    assert paddle.width == screen_width // 6
    assert paddle.height == 20
    assert paddle.speed == 5
    assert paddle.direction == 0

def test_reset(paddle, screen_width, screen_height):
    paddle.reset(screen_width, screen_height)
    assert paddle.x == int((screen_width /2) - (paddle.width / 2))
    assert paddle.y == screen_height - (paddle.height * 2)
    assert isinstance(paddle.rectangle, pygame.Rect)

def test_move_left(paddle, screen_width, screen_height):
    initial_x = paddle.x
    left_key_event = pygame.event.Event(KEYDOWN, key=pygame.K_LEFT)
    pygame.event.post(left_key_event)
    paddle.move(screen_width)
    expected_x = initial_x - paddle.speed * paddle.direction
    assert paddle.x == expected_x

def test_move_right(paddle, screen_width, screen_height):
    initial_x = paddle.x
    right_key_event = pygame.event.Event(KEYDOWN, key=pygame.K_LEFT)
    pygame.event.post(right_key_event)
    #pygame.key.set_key(pygame.K_RIGHT, True)
    paddle.move(screen_width)
    expected_x = initial_x - paddle.speed * paddle.direction
    assert paddle.x == expected_x

def test_move_out_of_bounds_left(paddle, screen_width, screen_height):
    paddle.x = 0
    left_key_event = pygame.event.Event(KEYDOWN, key=pygame.K_LEFT)
    pygame.event.post(left_key_event)
    paddle.move(screen_width)
    assert paddle.x == 0

def test_move_out_of_bounds_right(paddle, screen_width, screen_height):
    paddle.x = screen_width - paddle.width
    right_key_event = pygame.event.Event(KEYDOWN, key=pygame.K_LEFT)
    pygame.event.post(right_key_event)
    paddle.move(screen_width)
    assert paddle.x == screen_width - paddle.width
