## Create a functioning pong game using the pygame library

import pygame

## Create paddle class
class Paddle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = 0
        self.speed_y = 0
        # area of the rectangle
        self.rect = 100

    def render(self, screen):
        pygame.draw.rect(screen, (255,0,0), (self.x, self.y, 20, 75,), 0)



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
        screen.fill((0,0,0))
        player_one_paddle.render(screen)
        player_two_paddle.render(screen)
        pygame.display.update()


main()
    
