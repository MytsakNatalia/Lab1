import pygame

class Button:
    def __init__(self, screen):
        self.window = screen
        self.button_width = 180
        self.button_height = 50
        self.button_color = (100, 100, 100)
        self.button_text_color = (255, 255, 255)
        self.button_font = pygame.font.SysFont('Arial', 20)

    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.window.blit(img, (x, y))
    
    def draw_button(self, window, text, x, y, action):
        pygame.draw.rect(window, self.button_color, (x, y, self.button_width, self.button_height))
        self.draw_text(text, self.button_font, self.button_text_color, x + 10, y + 10)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.button_width and y < mouse[1] < y + self.button_height:
            if click[0] == 1:
                action()
    
    def button_clicked(self, mouse_x, mouse_y, button_x, button_y, button_width, button_height):
        return button_x < mouse_x < button_x + button_width and button_y < mouse_y < button_y + button_height