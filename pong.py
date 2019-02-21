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
        pygame.draw.rect(screen, (255,0,0), (self.x, self.y, 10, 75,), 0)

    def update(self):
        self.y = self.y + self.speed_y
        # paddle cannot go off the bottom of the screen
        if self.y > canvas_height - 75:
            self.y = canvas_height - 75
        # paddle cannot go off top of screen
        elif self.y < 0:
            self.y = 0

## Create Ball class

class Ball():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_y = 0
        self.speed_x = 0
        self.radius = 10

    def render_ball(self, screen):
        pygame.draw.circle(screen, (255,255,255), (self.x, self.y), self.radius, 0)
    
    def start_movement(self, speed_x, speed_y):
        self.speed_y = 5
        self.speed_x = 5

    def update(self):

        if self.x > canvas_width:
            self.x = self.x - 400
        # ball moves horizontally to the right
        self.x = self.x + self.speed_x
        # ball moves downwards
        self.y = self.y + self.speed_y
        # if ball reaches bottom of screen
        if self.y > canvas_height:
            # redirect ball upwards
            self.speed_y = -self.speed_y
        # if ball reaches top of screen
        if self.y < 0:
            # redirect ball downwards
            self.speed_y = -self.speed_y


class Net():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def render_net(self, screen):
        pygame.draw.rect(screen, (255,255,255), (self.x, self.y, 5, 10), 0)

def collision(ball, player_one_paddle, player_two_paddle):
    # if the ball's y position and x position matches player two paddle
    if ball.y > player_two_paddle.y - 30 and ball.y < player_two_paddle.y + 80 and (ball.x > player_two_paddle.x - 10 or ball.x == player_two_paddle.x):
        ball.speed_x = -ball.speed_x

    # does same as above code, but for left paddle
    if ball.y > player_one_paddle.y - 50 and ball.y < player_one_paddle.y + 75 and (ball.x < player_one_paddle.x + 20):
        ball.speed_x = -ball.speed_x


def main():
    #Create screen

    pygame.init()
    # initializes fonts for testing
    pygame.font.init()
    screen = pygame.display.set_mode((canvas_width, canvas_height))
    pygame.display.set_caption('Pong Game')

    player_one_score = 0
    player_two_score = 0

    print(pygame.font.get_fonts())
    


    # create two instances of Paddle class
    player_one_paddle = Paddle(35, 200)
    player_two_paddle = Paddle(725, 600)
    # create initial instance of Ball class
    ball = Ball(350, 350)

    done = False
    while not done:

        # Keyboard controls and quitting game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            
            # if a key is pressed down
            if event.type == pygame.KEYDOWN:

                # press space key to start ball movement
                if event.key == pygame.K_SPACE:
                    if player_one_score < player_two_score:
                        ball.start_movement(-5, 0)
                    else:
                        ball.start_movement(5, 0)

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

        # Handle off screen

        # if ball goes off screen to the right
        if ball.x > canvas_width:
            # create new instance of Ball
            ball = Ball(350, 350)
            # increment player one score
            player_one_score += 1
        # if ball goes off screen to the left
        elif ball.x < 0:
            # create new instance of Ball
            ball = Ball(350, 350)
            # increment player two score
            player_two_score += 1

        # handle collision between current Ball instance and paddles
        collision(ball, player_one_paddle, player_two_paddle)

        # --------------------------------------------- #

        # Screen updates / rendering
            
        

        player_one_paddle.update()
        player_two_paddle.update()
        ball.update()
        # fills the screen and makes it black
        screen.fill((0,0,0))
        # create instances of Net class
        i = 5
        while i < 795:
            net = Net(400, i)
            net.render_net(screen)
            i += 25

        font = pygame.font.SysFont('chalkboard', 35)
        score_one = font.render("Player One: %s" % str(player_one_score), True, (255,255,255))
        score_two = font.render("Player Two: %s" % str(player_two_score), True, (255,255,255))
        screen.blit(score_one, (100, 5))
        screen.blit(score_two, (500, 5))

        # renders both paddles to the screen
        player_one_paddle.render(screen)
        player_two_paddle.render(screen)
        ball.render_ball(screen)



        # updates game display
        pygame.display.update()



main()
    
