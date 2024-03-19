import pygame
from pygame.locals import *
from movable.ball import  Ball
from movable.paddle import  Paddle
from unmovable.wallBricks import Wall
from unmovable.controllers.button import  Button

pygame.init()

class Game:
    def __init__(self, screen, height, width, difficulty):
        """Constructor for creating an object of the Game class

        Parameters:
            screen (object): The object of Window class
            height (float): The height of the screen
            width (float): The width of the screen
            difficulty (string): The level og difficulty of the game
        """
        self.window = screen
        self.height = height
        self.width = width
        self.cols = 6
        self.rows = 6
        self.bg_color = (234, 218, 184)
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.continueGame = True
        self.difficulty = difficulty
        self.font = pygame.font.SysFont('Constantia', 30)
        self.text_col = (78, 81, 139)
        self.button = Button(self.window)
        self.paddle = Paddle(self.width, self.height)
        self.ball = Ball(int(self.paddle.x + (self.paddle.width // 2)), int(self.paddle.y - self.paddle.height))# must be replaced with paddle dimensions
        self.wall = Wall(self.difficulty, self.width, self.height, self.bg_color, self.cols, self.rows )       
        self.wall.create_wall()
        self.wall.draw_wall(self.window)

        self.paddle.draw(self.window)  
        
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
        
    '''def pause_window(self):
        """Display window when Pause is clicked on main window 
            Allows user to chooose 3 options: Continue, Play Again, Quit
            Draws buttons and text for this 

        Returns:
            string: choosed option 
        """
        pause_window_width = 300
        pause_window_height = 230  
        pause_window_x = (self.width - pause_window_width) // 2
        pause_window_y = (self.height - pause_window_height) // 3 - 10  
        pause_window_bg_color = (200, 200, 200)
        pause_window_font = pygame.font.SysFont('Arial', 24)

        pause_window_surface = pygame.Surface((pause_window_width, pause_window_height))
        pause_window_surface.fill(pause_window_bg_color)

        self.window.blit(pause_window_surface, (pause_window_x, pause_window_y))
        self.draw_text("PAUSED", pause_window_font, (0, 0, 0), pause_window_x + 80, pause_window_y + 10)  
            
        button_gap = 10  
        button_x = pause_window_x + 50
        button_y = pause_window_y + 53  

        self.button.draw_button(self.window, "Continue", button_x, button_y, self.continue_game) 
        self.button.draw_button(self.window, "Play Again", button_x, button_y + self.button.button_height + button_gap, self.play_again) 
        self.button.draw_button(self.window, "Quit", button_x, button_y + 2 * (self.button.button_height + button_gap), self.quit_game) 

        while True:  # Loop to handle user input within the pause window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.button.button_clicked(mouse_pos[0], mouse_pos[1], button_x, button_y, self.button.button_width, self.button.button_height):
                        return "continue"
                    elif self.button.button_clicked(mouse_pos[0], mouse_pos[1], button_x, button_y + self.button.button_height + button_gap, self.button.button_width, self.button.button_height):
                        return "play_again" 
                    elif self.button.button_clicked(mouse_pos[0], mouse_pos[1], button_x, button_y + 2 * (self.button.button_height + button_gap), self.button.button_width, self.button.button_height):
                        return "quit" 

            pygame.display.update()
            self.clock.tick(self.fps)   '''

    def display_pause_window(self):
        """Display the pause window on the Pygame window."""
        pause_window_width = 300
        pause_window_height = 230
        pause_window_x = (self.width - pause_window_width) // 2
        pause_window_y = (self.height - pause_window_height) // 3 - 10
        pause_window_bg_color = (200, 200, 200)
        pause_window_font = pygame.font.SysFont('Arial', 24)

        pause_window_surface = pygame.Surface((pause_window_width, pause_window_height))
        pause_window_surface.fill(pause_window_bg_color)

        self.window.blit(pause_window_surface, (pause_window_x, pause_window_y))
        self.draw_text("PAUSED", pause_window_font, (0, 0, 0), pause_window_x + 80, pause_window_y + 10)

        button_gap = 10
        button_x = pause_window_x + 50
        button_y = pause_window_y + 53

        self.button.draw_button(self.window, "Continue", button_x, button_y, self.continue_game)
        self.button.draw_button(self.window, "Play Again", button_x, button_y + self.button.button_height + button_gap,
                                self.play_again)
        self.button.draw_button(self.window, "Quit", button_x, button_y + 2 * (self.button.button_height + button_gap),
                                self.quit_game)

    def handle_pause_window_events(self):
        """Handle events in the pause window."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.button.button_clicked(mouse_pos[0], mouse_pos[1], button_x, button_y, self.button.button_width,
                                              self.button.button_height):
                    return "continue"
                elif self.button.button_clicked(mouse_pos[0], mouse_pos[1], button_x,
                                                button_y + self.button.button_height + button_gap,
                                                self.button.button_width, self.button.button_height):
                    return "play_again"
                elif self.button.button_clicked(mouse_pos[0], mouse_pos[1], button_x,
                                                button_y + 2 * (self.button.button_height + button_gap),
                                                self.button.button_width, self.button.button_height):
                    return "quit"

    def pause_window(self):
        """Display window when Pause is clicked on main window
            Allows user to choose 3 options: Continue, Play Again, Quit
            Draws buttons and text for this

        Returns:
            string: chosen option
        """
        self.display_pause_window()

        while True:
            result = self.handle_pause_window_events()
            if result:
                return result

            pygame.display.update()
            self.clock.tick(self.fps)
            
    def play_again():
        pass

    def continue_game():    
        pass

    def quit_game():
        pygame.quit()

    def pause_game(self):
        """Handle operatins that was choosed after clicking Pause button
        """
        self.continueGame = False  # Pause the game loop
        paused = True  
        
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Quit the game if the user closes the window

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        paused = False  # Resume the game if the user presses Escape
            
            res = self.pause_window()
            if res == "continue":  
                paused = False
                self.continueGame = True  
            elif res == "play_again":              
               paused = False
               self.continueGame = True                            
               game = Game(self.window, self.height, self.width, self.difficulty)
               game.run()                          
            elif res == "quit":  
                pygame.quit() 


    def run(self):
        """Run the Game
            User play here 
            Draw all components of Game 
            Wall with Bricks, Paddle, Ball, Pause Button 
            Hadle Pause clicking and victory or fault 
        """ 
        paused = False


        while self.continueGame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.continueGame = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        paused = not paused 

            if not paused:

                self.ball.draw(self.window)            
                self.window.fill(self.bg_color)
                self.ball.draw(self.window)
                self.wall.draw_wall(self.window)
                self.paddle.move(self.width)
                self.paddle.draw(self.window)
                            
                self.button.draw_button(self.window, "Pause", 210, 0, self.pause_game)            
                
                live_ball =True

                if live_ball:
                    # draw paddle
                    self.paddle.move(self.width)
                    # draw ball
                    game_over = self.ball.move(self.wall, self.paddle, self.width, self.height)
                    if game_over != 0:
                        live_ball = False

                    # print player instructions
                if not live_ball:
                    if game_over == 0:
                        self.draw_text('CLICK ANYWHERE TO START', self.font, self.text_col, 100, self.height // 2 + 100)
                    elif game_over == 1:

                        self.draw_text('YOU WON!', self.font, self.text_col, 240, self.height // 2 + 50)
                       # draw_text('CLICK ANYWHERE TO START', font, text_col, 100, height // 2 + 100)
                    elif game_over == -1:
                        self.draw_text('YOU LOST!', self.font, self.text_col, 240, self.height // 2 + 50)
                      #  draw_text('CLICK ANYWHERE TO START', font, text_col, 100, height // 2 + 100)




            else:
                self.pause_game()

            

            pygame.display.update()
            self.clock.tick(self.fps)


        pygame.quit()
    

def main():
    """The starting window for Game
        Show difficulty levels
        Handle choosed levels
    """
    from unmovable.controllers.difficulty import Difficulty
    width = 750
    height = 750
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Arkanoid")
    difficulty = Difficulty(window, height, width)
    difficulty.show_difficulty_levels()
    while True:  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 210 < mouse_pos[0] < 390 and 300 < mouse_pos[1] < 350:
                        difficulty.start_game_easy()
                elif 210 < mouse_pos[0] < 390 and 370 < mouse_pos[1] < 420:
                        difficulty.start_game_medium()
                elif 210 < mouse_pos[0] < 390 and 440 < mouse_pos[1] < 490:
                        difficulty.start_game_hard()
                    
        pygame.display.update()
        
if __name__ == '__main__':
    main()