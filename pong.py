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


class Ball():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_y = 3
        self.speed_x = 3
        self.radius = 10

    def render_ball(self, screen):
        pygame.draw.circle(screen, (255,255,255), (self.x, self.y), self.radius, 0)

    def update(self):
        # ball moves horizontally to the right
        self.x = self.x + self.speed_x
        # ball moves downwards
        self.y = self.y + self.speed_y
        # if ball reaches right edge of screen
        if self.x > canvas_width:
            # redirect ball to the left
            self.speed_x = -self.speed_x
        # if ball reaches left edge of screen
        if self.x < 0:
            self.speed_x = -self.speed_x
        # if ball reaches bottom of screen
        if self.y > canvas_height:
            # redirect ball upwards
            self.speed_y = -self.speed_y
        # if ball reaches top of screen
        if self.y < 0:
            # redirect ball downwards
            self.speed_y = -self.speed_y







def main():
    #Create screen


    pygame.init()
    screen = pygame.display.set_mode((canvas_width, canvas_height))
    pygame.display.set_caption('Pong Game')

    # create instance of Paddle class
    player_one_paddle = Paddle(35, 400)
    player_two_paddle = Paddle(725, 400)
    # create instance of Ball class
    ball = Ball(400, 400)


    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            
            # if a key is pressed down
            if event.type == pygame.KEYDOWN:
                # if down arrow is pressed
                if event.key == KEY_DOWN:
                    player_one_paddle.speed_y = 6
                # if s key is pressed
                elif event.key == pygame.K_s:
                    player_two_paddle.speed_y = 6
                # if up arrow is pressed
                if event.key == KEY_UP:
                    player_one_paddle.speed_y = -6
                # if w key is pressed
                elif event.key == pygame.K_w:
                    player_two_paddle.speed_y = -6
            
            # if a key is pressed up (released)
            if event.type == pygame.KEYUP:
                # if down arrow is released
                if event.key == KEY_DOWN:
                    player_one_paddle.speed_y = 0
                # if s key is released
                elif event.key == pygame.K_s:
                    player_two_paddle.speed_y = 0
                # if up arrow is released
                if event.key == KEY_UP:
                    player_one_paddle.speed_y = 0
                # if w key is released
                elif event.key == pygame.K_w:
                    player_two_paddle.speed_y = 0

            
        

        player_one_paddle.update()
        player_two_paddle.update()
        ball.update()
        # fills the screen and makes it black
        screen.fill((0,0,0))
        # renders both paddles to the screen
        player_one_paddle.render(screen)
        player_two_paddle.render(screen)
        ball.render_ball(screen)



        # updates game display
        pygame.display.update()


main()
    
