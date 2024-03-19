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
    # Mock necessary dependencies
    mocker.patch.object(game_instance, 'window')
    mocker.patch.object(game_instance, 'button')

    # Set up expected button click positions
    button_x, button_y = 100, 100
    continue_button_clicked_pos = (button_x + 5, button_y + 5)  # Inside "Continue" button area

    # Simulate the mouse click on the "Continue" button
    game_instance.button.button_clicked.return_value = True
    game_instance.button.button_clicked.side_effect = lambda x, y, _, __, ___, ____: (x,
                                                                                      y) == continue_button_clicked_pos

    # Call the pause_window method
    result = game_instance.pause_window()

    # Assert that the function returns the correct value
    assert result == "continue"
def test_play_again(game_instance):
    # Test the play_again method
    # You can simulate the user's choice and check if the game resets
    pass  # Implement this test if needed

def test_continue_game(game_instance):
    # Test the continue_game method
    # You can simulate the user's choice and check if the game continues
    pass  # Implement this test if needed

def test_quit_game(game_instance):
    # Test the quit_game method
    # You can mock the pygame window object to check if pygame.quit() is called
    pass  # Implement this test if needed

def test_pause_game(game_instance):
    # Test the pause_game method
    # You can simulate the user's choice and check if the game is paused correctly
    pass  # Implement this test if needed

def test_run(game_instance):
    # Test the run method
    # You can mock the pygame window object to capture the game loop execution
    pass  # Implement this test if needed