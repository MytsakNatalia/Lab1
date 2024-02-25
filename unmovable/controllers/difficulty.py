import pygame
from unmovable.controllers.button import  Button
from main import Game

class Difficulty:    
    def __init__(self, screen, height, width):
        self.window = screen
        self.bg_color = (234, 218, 184)
        self.height = height
        self.width = width
        self.font = pygame.font.SysFont('Constantia', 30)
        self.text_col = (78, 81, 139)
        self.button = Button(self.window)
    
    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.window.blit(img, (x, y))
    
    def show_difficulty_levels(self):
        self.window.fill(self.bg_color)
        self.draw_text('Choose Difficulty Level:', self.font, self.text_col, 150, 200)
        self.button.draw_button(self.window, 'Easy', 210, 300, self.start_game_easy)
        self.button.draw_button(self.window, 'Medium', 210, 370, self.start_game_medium)
        self.button.draw_button(self.window, 'Hard', 210, 440, self.start_game_hard)
        pygame.display.update()

    def start_game_easy(self):
        game = Game(self.window, self.height, self.width, difficulty='easy')
        game.run()

    def start_game_medium(self):
        game = Game(self.window, self.height, self.width, difficulty='medium')
        game.run()

    def start_game_hard(self):
        game = Game(self.window, self.height, self.width, difficulty='hard')
        game.run()