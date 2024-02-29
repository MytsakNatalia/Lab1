import pygame

class Button:    
    def __init__(self, screen):
        """Constructor for creating an object of the Button class
        
        Parameters:
            screen (object): The object of class Window 
        """
        self.window = screen
        self.button_width = 180
        self.button_height = 50
        self.button_color = (100, 100, 100)
        self.button_text_color = (255, 255, 255)
        self.button_font = pygame.font.SysFont('Arial', 20)

        
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
    
    
    def draw_button(self, window, text, x, y, action):
        pygame.draw.rect(window, self.button_color, (x, y, self.button_width, self.button_height))
        
        """ Draw a button on the window with the specified text and position.

        Parameters:
            window (object): An object of the window class 
            text (string): The text to display on the button
            x (float): The x-coordinate of the upper left corner of the button
            y (float): The y-coordinate of the upper left corner of the button
            action (function): The function to be executed when the button is clicked
        """
        self.draw_text(text, self.button_font, self.button_text_color, x + 10, y + 10)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.button_width and y < mouse[1] < y + self.button_height:
            if click[0] == 1:
                action()
    
            
    def button_clicked(self, mouse_x, mouse_y, button_x, button_y, button_width, button_height):
        """Determine whether certain button was clicked or not 
        
            Parameters:
                mouse_x (float): The x-coordinate of mouse 
                mouse_y (float): The y-coordinate of mouse 
                button_x (float): The x-coordinate of the upper left corner of the button
                button_y (float): The y-coordinate of the upper left corner of the button
                button_width (float): The widht of button
                button_height (float): The height of button
                
            Returns:
                bool: True if the button was clicked, False otherwise
        """
        return button_x < mouse_x < button_x + button_width and button_y < mouse_y < button_y + button_height