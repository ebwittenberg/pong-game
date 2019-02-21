## Create a functioning pong game using the pygame library

import pygame

# Initialize key values
KEY_UP = 273
KEY_DOWN = 274
# Initialize screen width/height
canvas_width = 800
canvas_height = 800

## Create paddle class
class Paddle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_y = 0
        # area of the rectangle
        self.rect = 100

    def render(self, screen):
        pygame.draw.rect(screen, (255,0,0), (self.x, self.y, 20, 75,), 0)

    def update(self):
        self.y = self.y + self.speed_y
        # paddle cannot go off the bottom of the screen
        if self.y > canvas_height - 75:
            self.y = canvas_height - 75
        # paddle cannot go off top of screen
        elif self.y < 0:
            self.y = 0




def main():
    #Create screen


    pygame.init()
    screen = pygame.display.set_mode((canvas_width, canvas_height))
    pygame.display.set_caption('Pong Game')

    # create instance of Paddle class
    player_one_paddle = Paddle(35, 400)
    player_two_paddle = Paddle(725, 400)


    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            
            # if a key is pressed down
            if event.type == pygame.KEYDOWN:
                # active upwards or downwords movement when specific
                # key is keyed down
                if event.key == KEY_DOWN:
                    player_one_paddle.speed_y = 6
                    # if player one paddle is at the bottom of the screen
                    # do not allow it to move further down
                    #if player_one_paddle.y > canvas_height:
                        #player_one_paddle.y = 0
                if event.key == KEY_UP:
                    player_one_paddle.speed_y = -6
            
            # if a key is pressed up (released)
            if event.type == pygame.KEYUP:
                # want paddle to stop moving
                if event.key == KEY_DOWN:
                    player_one_paddle.speed_y = 0
                if event.key == KEY_UP:
                    player_one_paddle.speed_y = 0

            
        

        player_one_paddle.update()
        # fills the screen and makes it black
        screen.fill((0,0,0))
        # renders both paddles to the screen
        player_one_paddle.render(screen)
        player_two_paddle.render(screen)



        # updates game display
        pygame.display.update()


main()
    
