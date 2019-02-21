## Create a functioning pong game using the pygame library

import pygame


def main():
    #Create screen
    canvas_width = 800
    canvas_height = 800

    pygame.init()
    screen = pygame.display.set_mode((canvas_width, canvas_height))
    pygame.display.set_caption('Pong Game')

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill((0,0,0))

main()
    
