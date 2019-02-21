## Create a functioning pong game using the pygame library

import pygame

KEY_UP = 273
KEY_DOWN = 274

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



def main():
    #Create screen
    canvas_width = 800
    canvas_height = 800

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
                if event.key == KEY_UP:
                    player_one_paddle.speed_y = -6
            
            # if a key is pressed up (released)
            if event.type == pygame.KEYUP:
                # want paddle to stop moving
                if event.key == KEY_DOWN:
                    player_one_paddle.speed_y = 0
                if event.key == KEY_UP:
                    player_one_paddle.speed_y = 0

            
        
        # fills the screen and makes it black

        player_one_paddle.update()

        screen.fill((0,0,0))
        # renders both paddles to the screen
        player_one_paddle.render(screen)
        player_two_paddle.render(screen)



        # updates game display
        pygame.display.update()


main()
    
