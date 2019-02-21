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
        pygame.draw.rect(screen, (255,0,0), (35, 400, self.x, self.y), 0)

def main():
    #Create screen
    canvas_width = 800
    canvas_height = 800

    pygame.init()
    screen = pygame.display.set_mode((canvas_width, canvas_height))
    pygame.display.set_caption('Pong Game')

    # create instance of Paddle class
    paddle = Paddle(40, 75)

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill((0,0,0))
        paddle.render(screen)
        # pygame.draw.rect(screen, (255,0,0), (200, 200, 50, 150), 1)
        pygame.display.update()


main()
    
