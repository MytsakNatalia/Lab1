import pygame
from unmovable.controllers.button import  Button
from main import Game

class Difficulty:    
    def __init__(self, screen, height, width):
        """Constructor for creating an object of the Diffficulty class

        Parameters:
            screen (object): An object of the Window class
            height (float): The height of screeen
            width (float): The width of screen 
        """
        self.window = screen
        self.bg_color = (234, 218, 184)
        self.height = height
        self.width = width
        self.font = pygame.font.SysFont('Constantia', 30)
        self.text_col = (78, 81, 139)
        self.button = Button(self.window)
    
    def draw_text(self, text, font, text_col, x, y):
        """Add (draw) text on window 
        
        Parameters:
            text (str): The text to draw
            font (pygame.Font): An object representing the font features
            text_col (tuple): The color of the text in RGB format
            x (float): The x-coordinate of the text
            y (float): The y-coordinate of the text        
        """
        img = font.render(text, True, text_col)
        self.window.blit(img, (x, y))
    
    def show_difficulty_levels(self):
        """Displays levels of difficulty, allowing the user to choose
            Add buttons for each level and text 
        """
        self.window.fill(self.bg_color)
        self.draw_text('Choose Difficulty Level:', self.font, self.text_col, 150, 200)
        self.button.draw_button(self.window, 'Easy', 210, 300, self.start_game_easy)
        self.button.draw_button(self.window, 'Medium', 210, 370, self.start_game_medium)
        self.button.draw_button(self.window, 'Hard', 210, 440, self.start_game_hard)
        pygame.display.update()

    def start_game_easy(self):
        """Starts the game with an easy difficulty level
            Creates an instance of the Game class configured for the easy difficulty level
        """
        game = Game(self.window, self.height, self.width, difficulty='easy')
        game.run()

    def start_game_medium(self):
        """Starts the game with an medium difficulty level
            Creates an instance of the Game class configured for the easy difficulty level
        """
        game = Game(self.window, self.height, self.width, difficulty='medium')
        game.run()

    def start_game_hard(self):
        """Starts the game with an hard difficulty level
            Creates an instance of the Game class configured for the easy difficulty level
        """
        game = Game(self.window, self.height, self.width, difficulty='hard')
        game.run()