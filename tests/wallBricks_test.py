import pygame
import pytest
from unmovable.wallBricks import Wall

# Define fixtures
@pytest.fixture
def screen():
    return pygame.display.set_mode((800, 600))

@pytest.fixture
def wall_easy():
    return Wall('easy', 800, 600, (0, 0, 0), 10, 5)

@pytest.fixture
def wall_medium():
    return Wall('medium', 800, 600, (0, 0, 0), 10, 5)

@pytest.fixture
def wall_hard():
    return Wall('hard', 800, 600, (0, 0, 0), 10, 5)

## Test the generation of block strengths for the 'easy' difficulty level
def test_generate_block_strength_easy(wall_easy):
    assert wall_easy.generate_block_strength(0) == 3
    assert wall_easy.generate_block_strength(1) == 3
    assert wall_easy.generate_block_strength(2) == 2
    assert wall_easy.generate_block_strength(3) == 2
    assert wall_easy.generate_block_strength(4) == 1
    
## Test the generation of block strengths for the 'medium' difficulty level
def test_generate_block_strength_medium(wall_medium):
    assert wall_medium.generate_block_strength(0) == 4
    assert wall_medium.generate_block_strength(1) == 4
    assert wall_medium.generate_block_strength(2) == 3
    assert wall_medium.generate_block_strength(3) == 3
    assert wall_medium.generate_block_strength(4) == 2

## Test the generation of block strengths for the 'hard' difficulty level
def test_generate_block_strength_hard(wall_hard):
    assert wall_hard.generate_block_strength(0) == 5
    assert wall_hard.generate_block_strength(1) == 5
    assert wall_hard.generate_block_strength(2) == 4
    assert wall_hard.generate_block_strength(3) == 4
    assert wall_hard.generate_block_strength(4) == 3

## Test the creation of the wall with bricks for different difficulty levels
def test_create_wall(wall_easy, wall_medium, wall_hard):
    wall_easy.create_wall()
    wall_medium.create_wall()
    wall_hard.create_wall()
    assert len(wall_easy.blocks) == 5
    assert len(wall_medium.blocks) == 5
    assert len(wall_hard.blocks) == 5
    assert len(wall_easy.blocks[0]) == 10
    assert len(wall_medium.blocks[0]) == 10
    assert len(wall_hard.blocks[0]) == 10

## Test the drawing of the wall on the screen for different difficulty levels
def test_draw_wall(screen, wall_easy, wall_medium, wall_hard):
    wall_easy.create_wall()
    wall_medium.create_wall()
    wall_hard.create_wall()
    wall_easy.draw_wall(screen)
    wall_medium.draw_wall(screen)
    wall_hard.draw_wall(screen)   
