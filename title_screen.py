import pygame

canvas_width = 800
canvas_height = 800

KEY_DOWN = 274




def title_screen():
    pygame.init()

    done = False
    screen = pygame.display.set_mode((canvas_width, canvas_height))
    pygame.display.set_caption('Pong Game')

    player_one_name = ''
    player_two_set_name = False
    player_two_name = ''

    # keeps looping
    while not done:
        
        # create black background for title screen

        screen.fill((0,0,0))

        # Title
        title_font = pygame.font.Font('bit5x3.ttf', 150)
        game_title = title_font.render("Pong", True, (255,255,255))
        screen.blit(game_title, (250, 100))

        # Player One and Player Two names


        player_font = pygame.font.Font('bit5x3.ttf', 50)
        player_one_render = player_font.render("Player One: %s" % player_one_name, True, (255,255,255))
        player_two_render = player_font.render("Player Two: %s" % player_two_name, True, (255,255,255))
        screen.blit(player_one_render, (75, 275))
        screen.blit(player_two_render, (75, 335))

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
            if event.type == pygame.QUIT:
                done = True
            if player_two_set_name == False:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        player_one_name += 'a'
                    if event.key == pygame.K_b:
                        player_one_name += 'b'
                    if event.key == pygame.K_c:
                        player_one_name += 'c'
                    if event.key == pygame.K_d:
                        player_one_name += 'd'
                    if event.key == pygame.K_e:
                        player_one_name += 'e'
                    if event.key == pygame.K_f:
                        player_one_name += 'f'
                    if event.key == pygame.K_g:
                        player_one_name += 'g'
                    if event.key == pygame.K_h:
                        player_one_name += 'h'
                    if event.key == pygame.K_i:
                        player_one_name += 'i'
                    if event.key == pygame.K_j:
                        player_one_name += 'j'
                    if event.key == pygame.K_k:
                        player_one_name += 'k'
                    if event.key == pygame.K_l:
                        player_one_name += 'l'
                    if event.key == pygame.K_m:
                        player_one_name += 'm'
                    if event.key == pygame.K_n:
                        player_one_name += 'n'
                    if event.key == pygame.K_o:
                        player_one_name += 'o'
                    if event.key == pygame.K_p:
                        player_one_name += 'p'
                    if event.key == pygame.K_q:
                        player_one_name += 'q'
                    if event.key == pygame.K_r:
                        player_one_name += 'r'
                    if event.key == pygame.K_s:
                        player_one_name += 's'
                    if event.key == pygame.K_t:
                        player_one_name += 't'
                    if event.key == pygame.K_u:
                        player_one_name += 'u'
                    if event.key == pygame.K_v:
                        player_one_name += 'v'
                    if event.key == pygame.K_w:
                        player_one_name += 'w'
                    if event.key == pygame.K_x:
                        player_one_name += 'x'
                    if event.key == pygame.K_y:
                        player_one_name += 'y'
                    if event.key == pygame.K_z:
                        player_one_name += 'z'

            

                    if event.key == pygame.K_RETURN:
                        player_two_set_name = True
            
            if player_two_set_name == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        player_two_name += 'a'
                    if event.key == pygame.K_b:
                        player_two_name += 'b'
                    if event.key == pygame.K_c:
                        player_two_name += 'c'
                    if event.key == pygame.K_d:
                        player_two_name += 'd'
                    if event.key == pygame.K_e:
                        player_two_name += 'e'
                    if event.key == pygame.K_f:
                        player_two_name += 'f'
                    if event.key == pygame.K_g:
                        player_two_name += 'g'
                    if event.key == pygame.K_h:
                        player_two_name += 'h'
                    if event.key == pygame.K_i:
                        player_two_name += 'i'
                    if event.key == pygame.K_j:
                        player_two_name += 'j'
                    if event.key == pygame.K_k:
                        player_two_name += 'k'
                    if event.key == pygame.K_l:
                        player_two_name += 'l'
                    if event.key == pygame.K_m:
                        player_two_name += 'm'
                    if event.key == pygame.K_n:
                        player_two_name += 'n'
                    if event.key == pygame.K_o:
                        player_two_name += 'o'
                    if event.key == pygame.K_p:
                        player_two_name += 'p'
                    if event.key == pygame.K_q:
                        player_two_name += 'q'
                    if event.key == pygame.K_r:
                        player_two_name += 'r'
                    if event.key == pygame.K_s:
                        player_two_name += 's'
                    if event.key == pygame.K_t:
                        player_two_name += 't'
                    if event.key == pygame.K_u:
                        player_two_name += 'u'
                    if event.key == pygame.K_v:
                        player_two_name += 'v'
                    if event.key == pygame.K_w:
                        player_two_name += 'w'
                    if event.key == pygame.K_x:
                        player_two_name += 'x'
                    if event.key == pygame.K_y:
                        player_two_name += 'y'
                    if event.key == pygame.K_z:
                        player_two_name += 'z'

                    if event.key == pygame.K_SPACE:
                        return True
        pygame.display.update()

