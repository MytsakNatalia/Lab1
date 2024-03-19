import pygame
import pytest
from main import Game


@pytest.fixture
def screen_width():
    return 750

@pytest.fixture
def screen_height():
    return 750

@pytest.fixture
def game_instance(screen_width, screen_height, screen):
    difficulty = "easy"
    return Game(screen, screen_width, screen_height, difficulty)


@pytest.fixture
def screen(screen_width, screen_height):
    pygame.init()
    return pygame.display.set_mode((screen_width, screen_height))
def test_init(game_instance, screen_width, screen_height):
    assert game_instance.window != None
    assert game_instance.height == screen_width
    assert game_instance.width == screen_height
    assert game_instance.cols == 6
    assert game_instance.rows == 6
    assert game_instance.bg_color == (234, 218, 184)
    assert game_instance.clock != None
    assert game_instance.fps == 60
    assert game_instance.continueGame == True
    assert game_instance.difficulty == "easy"
    assert game_instance.font != None
    assert game_instance.text_col == (78, 81, 139)
    assert game_instance.button != None
    assert game_instance.paddle != None
    assert game_instance.ball != None
    assert game_instance.wall != None

def test_draw_text(mocker, screen, screen_width, screen_height):
    font = pygame.font.SysFont(None, 36)

    game_instance = Game(screen, screen_width, screen_height, "easy")

    text = "Hello, World!"
    text_color = (255, 255, 255)
    x, y = 100, 100
    game_instance.draw_text(text, font, text_color, x, y)

    # Update the display
    pygame.display.flip()

    # Check if the text is drawn on the surface
    text_rendered = font.render(text, True, text_color)
    assert screen.blit(text_rendered, (x, y)) == pygame.Rect(x, y, text_rendered.get_width(),
                                                             text_rendered.get_height())

def test_pause_window_continue(game_instance, mocker):
    # Mocking
    mocker.patch.object(game_instance, 'display_pause_window')
    mocker.patch.object(game_instance, 'handle_pause_window_events')

    # Simulate the user clicking on the "Continue" button
    game_instance.handle_pause_window_events.return_value = "continue"


    result = game_instance.pause_window()

    # Assert that the function returns the correct value
    assert result == "continue"
def test_pause_window_play_again(game_instance, mocker):
    # Mock necessary elements
    mocker.patch.object(game_instance, 'display_pause_window')
    mocker.patch.object(game_instance, 'handle_pause_window_events')

    # Simulate the user clicking on the "Play Again" button
    game_instance.handle_pause_window_events.return_value = "play_again"


    result = game_instance.pause_window()

    # Assert that the function returns the correct value
    assert result == "play_again"

def test_pause_window_quit(game_instance, mocker):
    # Mock necessary dependencies
    mocker.patch.object(game_instance, 'display_pause_window')
    mocker.patch.object(game_instance, 'handle_pause_window_events')

    # Simulate the user clicking on the "Quit" button
    game_instance.handle_pause_window_events.return_value = "quit"

    # Call the pause_window method
    result = game_instance.pause_window()

    # Assert that the function returns the correct value
    assert result == "quit"



def test_run(game_instance):
    
    pass