import pygame
from pygame.locals import *
from movable.ball import  Ball
from movable.paddle import  Paddle
from unmovable.wallBricks import Wall

pygame.init()

width = 750
height = 750
bg_color = (234, 218, 184)

cols = 6
rows = 6

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Arkanoid")
clock = pygame.time.Clock()
fps = 60
font = pygame.font.SysFont('Constantia', 30)
text_col = (78, 81, 139)

button_width = 180
button_height = 50
button_color = (100, 100, 100)
button_text_color = (255, 255, 255)
button_font = pygame.font.SysFont('Arial', 20)

def draw_button(text, x, y, action):
    pygame.draw.rect(window, button_color, (x, y, button_width, button_height))
    draw_text(text, button_font, button_text_color, x + 10, y + 10)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x < mouse[0] < x + button_width and y < mouse[1] < y + button_height:
        if click[0] == 1:
            action()
  
def button_clicked(mouse_x, mouse_y, button_x, button_y, button_width, button_height):
    return button_x < mouse_x < button_x + button_width and button_y < mouse_y < button_y + button_height
  
def pause_window():
    pause_window_width = 300
    pause_window_height = 230  
    pause_window_x = (width - pause_window_width) // 2
    pause_window_y = (height - pause_window_height) // 3 - 10  
    pause_window_bg_color = (200, 200, 200)
    pause_window_font = pygame.font.SysFont('Arial', 24)

    pause_window_surface = pygame.Surface((pause_window_width, pause_window_height))
    pause_window_surface.fill(pause_window_bg_color)

    window.blit(pause_window_surface, (pause_window_x, pause_window_y))
    draw_text("PAUSED", pause_window_font, (0, 0, 0), pause_window_x + 80, pause_window_y + 10)  
        
    button_gap = 10  
    button_x = pause_window_x + 50
    button_y = pause_window_y + 53  

    draw_button("Continue", button_x, button_y, continue_game) 
    draw_button("Play Again", button_x, button_y + button_height + button_gap, play_again) 
    draw_button("Quit", button_x, button_y + 2 * (button_height + button_gap), quit_game) 

    while True:  # Loop to handle user input within the pause window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               return "quit"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button_clicked(mouse_pos[0], mouse_pos[1], button_x, button_y, button_width, button_height):
                    return "continue"
                elif button_clicked(mouse_pos[0], mouse_pos[1], button_x, button_y + button_height + button_gap, button_width, button_height):
                    return "play_again" 
                elif button_clicked(mouse_pos[0], mouse_pos[1], button_x, button_y + 2 * (button_height + button_gap), button_width, button_height):
                    return "quit" 

        pygame.display.update()
        clock.tick(fps)

def play_again():
    ##
    pass

def continue_game():
    ##refreeze ball
    pass

def quit_game():
    pygame.quit()

def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	window.blit(img, (x, y))

def show_difficulty_levels():
    window.fill(bg_color)
    draw_text('Choose Difficulty Level:', font, text_col, 150, 200)
    draw_button('Easy', 210, 300, start_game_easy)
    draw_button('Medium', 210, 370, start_game_medium)
    draw_button('Hard', 210, 440, start_game_hard)
    pygame.display.update()

def start_game_easy():
    game = Game(difficulty='easy')
    game.run()

def start_game_medium():
    game = Game(difficulty='medium')
    game.run()

def start_game_hard():
    game = Game(difficulty='hard')
    game.run()

class Game:
    def __init__(self, difficulty):
        self.continueGame = True
        self.difficulty = difficulty
        self.paddle = Paddle(width, height)
        self.ball = Ball(int(self.paddle.x + (self.paddle.width // 2)), int(self.paddle.y - self.paddle.height))# must be replaced with paddle dimensions
        self.wall = Wall(difficulty, width, height, bg_color, cols, rows )       
        self.wall.create_wall()
        self.wall.draw_wall(window)

        self.paddle.draw(window)
        
    
    def pause_game(self):
        self.continueGame = False  # Pause the game loop
        paused = True  
        
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Quit the game if the user closes the window

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        paused = False  # Resume the game if the user presses Escape
            
            res = pause_window()
            if res == "continue":  
                paused = False
                self.continueGame = True  
            elif res == "play_again":              
               paused = False
               self.continueGame = True
               difficulty = self.difficulty               
               game = Game(difficulty)
               game.run()                          
            elif res == "quit":  
                pygame.quit() 


    def run(self):
        paused = False


        while self.continueGame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.continueGame = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        paused = not paused 

            if not paused:

                self.ball.draw(window)            
                window.fill(bg_color)
                self.ball.draw(window)
                self.wall.draw_wall(window)
                self.paddle.move(width)
                self.paddle.draw(window)
                            
                draw_button("Pause", 210, 0, self.pause_game)            
                
                live_ball =True

                if live_ball:
                    # draw paddle
                    self.paddle.move(width)
                    # draw ball
                    game_over = self.ball.move(self.wall, self.paddle, width, height)
                    if game_over != 0:
                        live_ball = False

                    # print player instructions
                if not live_ball:
                    if game_over == 0:
                        draw_text('CLICK ANYWHERE TO START', font, text_col, 100, height // 2 + 100)
                    elif game_over == 1:
                        draw_text('YOU WON!', font, text_col, 240, height // 2 + 50)
                       # draw_text('CLICK ANYWHERE TO START', font, text_col, 100, height // 2 + 100)
                    elif game_over == -1:
                        draw_text('YOU LOST!', font, text_col, 240, height // 2 + 50)
                      #  draw_text('CLICK ANYWHERE TO START', font, text_col, 100, height // 2 + 100)

            else:
                self.pause_game()

            

            pygame.display.update()
            clock.tick(fps)


        pygame.quit()

def main():
    show_difficulty_levels()
    while True:  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 210 < mouse_pos[0] < 390 and 300 < mouse_pos[1] < 350:
                        start_game_easy()
                elif 210 < mouse_pos[0] < 390 and 370 < mouse_pos[1] < 420:
                        start_game_medium()
                elif 210 < mouse_pos[0] < 390 and 440 < mouse_pos[1] < 490:
                        start_game_hard()
                    
        pygame.display.update()
        
if __name__ == '__main__':
    main()