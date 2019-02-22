import pygame

canvas_width = 800
canvas_height = 800

def title_screen():
    pygame.init()

    done = False
    screen = pygame.display.set_mode((canvas_width, canvas_height))
    pygame.display.set_caption('Pong Game')

    while not done:
        
        # create black background for title screen

        screen.fill((0,0,0))

        # Title
        title_font = pygame.font.Font('bit5x3.ttf', 150)
        game_title = title_font.render("Pong", True, (255,255,255))
        screen.blit(game_title, (250, 100))

        # Instructions
        instructions_font = pygame.font.Font('bit5x3.ttf', 50)
        instructions_details = pygame.font.Font('bit5x3.ttf', 35)
        instructions = instructions_font.render("Instructions: ", True, (255,255,255))
        instructions_2 = instructions_details.render("--Player One controls the left paddle", True, (255,255,255))
        instructions_3 = instructions_details.render("--Player Two controls the right paddle", True, (255,255,255))
        instructions_4 = instructions_details.render("--Arrow keys and W / S keys to control", True, (255,255,255))
        screen.blit(instructions, (50, 400))
        screen.blit(instructions_2, (75, 460))
        screen.blit(instructions_3, (75, 500))
        screen.blit(instructions_4, (75, 540))


        # Space to start
        start_font = pygame.font.Font('bit5x3.ttf', 50)
        start_game = start_font.render("Press space to start", True, (255,255,255))
        screen.blit(start_game, (150, 650))


        for event in pygame.event.get():
            # handle quit
            if event.type == pygame.QUIT:
                done = True
            # handle space to start game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True

        pygame.display.update()

