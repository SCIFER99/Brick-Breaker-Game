# By: Tim Tarver
# Brick Breaker Game

import pygame
import time
from pygame.locals import *

# Initialize the Win functionality

class GameWin():

    def __init__(self):

        self.width = 800
        self.height = 400
        self.game_win_image = pygame.image.load("win.bmp")
        self.game_win_image = pygame.transform.scale(self.game_win_image,
                                                     (self.width, self.height))

    def draw_image(self, screen):
        print("dhfajksdhfa")
        screen.blit(self.game_win_image, (30, 150))

# Initialize the Game Over functionality

class GameOver():

    def __init__(self):

        self.width = 800
        self.height = 400
        self.game_over_x = 30
        self.game_over_y = 150
        self.game_over_image = pygame.image.load("gameover.png")
        self.game_over_image = pygame.transform.scale(self.game_over_image,
                                                      (self.width, self.height))

    def draw_image(self, screen):
        print("sdfjsdlkfj")
        screen.blit(self.game_over_image, (self.game_over_x, self.game_over_y))

# Initialize the drawn Bat to hit the ball

class Bat:

    def __init__(self):

        self.bat_x = 400
        self.bat_y = 570
        self.width = 100
        self.height = 25
        self.ball_kick_width = 800
        self.bat_image = pygame.image.load("bat.bmp")
        self.bat_image = pygame.transform.scale(self.bat_image,
                                                (self.width, self.height))
        self.hitbox = pygame.Rect(self.bat_x, self.bat_y, self.width, self.height)

    def draw_bat(self, window):
        window.blit(self.bat_image, (self.bat_x, self.bat_y))
        # pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

# Initialize the Bricks to be drawn to the screen

class Brick:

    def __init__(self):

        self.brick_width = 80
        self.brick_height = 35
        self.delete_brick_count = 0
        self.number_of_bricks = 21
        self.brick_image = pygame.image.load("brick.bmp")
        self.brick_image = pygame.transform.scale(self.brick_image,
                                                  (self.brick_width, self.brick_height))
        self.brick_rectangle = []
        self.brick_list = []

    def initialize_bricks(self):

        for self.rows in range(50, 151, 50):
            for self.columns in range(50, 651, 100):
                self.brick_list.append([self.columns, self.rows])
                self.brick_rectangle.append([self.columns, self.rows])

    def draw_brick(self, window):

        for row in self.brick_list:

            self.hitbox = pygame.Rect(row[0], row[1], self.brick_width, self.brick_height)
            window.blit(self.brick_image, (row[0], row[1]))
            # pygame.draw.rect(window, (355, 0, 0), self.hitbox, 2)

# Draw the ball for breaking the bricks

class Ball:

    def _init__(self):

        self.ball_x = 350
        self.ball_y = 300
        self.width = 30
        self.height = 60

        self.ball_kick_width = 800
        self.ball_kick_height = 600
        self.ball_kick_width_min = 0
        self.ball_kick_height_min = 0

        self.ball_velocity_x = 2
        self.ball_velocity_y = 2
        self.ball_image = pygame.image.load("ball.bmp")
        self.ball_image = pygame.transform.scale(self.ball_image,
                                                 (self.width, self.height))
        self.ball_kick1 = pygame.image.load("bk.bmp")
        self.ball_kick2 = pygame.image.load("bk.bmp")

        self.hitbox = pygame.Rect(self.ball_x, self.ball_y, self.width, self.height)

    def draw_ball(self, window):

        self.width = 30
        self.height = 60
        self.ball_x = 350
        self.ball_y = 300
        self.ball_kick_width = 800
        self.ball_kick_height = 600
        self.ball_kick_width_min = 0
        self.ball_kick_height_min = 0
        self.ball_velocity_x = 2
        self.ball_velocity_y = 2
        self.ball_image = pygame.image.load("ball.bmp")
        self.ball_kick1 = pygame.image.load("bk.bmp")
        self.ball_kick2 = pygame.image.load("bk.bmp")
        window.blit(self.ball_kick1, (self.ball_kick_width_min, self.ball_kick_height_min))
        window.blit(self.ball_kick2, (self.ball_kick_width, self.ball_kick_height))

        window.blit(self.ball_image, (self.ball_x, self.ball_y))

        # pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

    def move_ball(self):

        self.ball_x = self.ball_x + self.ball_velocity_x
        self.ball_y = self.ball_y + self.ball_velocity_y
        self.hitbox = pygame.Rect(self.ball_x, self.ball_y, self.width, self.height)
        
        

# Main functionality of the game

def main():

    clock = pygame.time.Clock()

    window = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Brick Breaker Game")

    # Instantiate all Classes and call necessary methods
    # for the game.

    ball = Ball()
    ball.draw_ball(window)
    bat = Bat()
    bat.draw_bat(window)
    brick = Brick()
    brick.initialize_bricks()
    
    game_over = GameOver()
    game_win = GameWin()

    pygame.display.update()

    quit1 = False

    # Event Programming Section
    
    while not quit1:

        
        window.fill((240, 240, 240))
        clock.tick(80)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit1 = True

        ball.draw_ball(window)
        bat.draw_bat(window)

        ball.move_ball()        
        brick.draw_brick(window)

        if (ball.ball_x < ball.ball_kick_width_min or ball.ball_x > ball.ball_kick_width - 30):
            ball.ball_velocity_x = -ball.ball_velocity_x

        if ball.ball_y < ball.ball_kick_height_min:
            ball.ball_velocity_y = -ball.ball_velocity_y

        if ball.ball_y > ball.ball_kick_height:
            # ball.ball_velocity_y = -ball.ball_velocity_y
            print("gd")
            game_over.draw_image(window)
            bat.bat_x = 1000

        if ball.hitbox.colliderect(bat.hitbox):
            ball.ball_velocity_y = -ball.ball_velocity_y
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and bat.bat_x > 0:
                bat.bat_x = bat.bat_x - 2
                bat.hitbox = pygame.Rect(bat.bat_x, bat.bat_y, bat.width, bat.height)

            elif event.key == pygame.K_RIGHT and bat.bat_x < bat.ball_kick_width - 100:
                bat.bat_x = bat.bat_x + 2
                bat.hitbox = pygame.Rect(bat.bat_x, bat.bat_y, bat.width, bat.height)

        for row in brick.brick_list:

            brick.hitbox = pygame.Rect(row[0], row[1], brick.brick_width, brick.brick_height)
            # pygame.draw.rect(window, (255, 0, 0), brick.hitbox, 2)

            if ball.hitbox.colliderect(brick.hitbox):
                row[0] = 1000
                row[1] = 1000
                ball.ball_velocity_y = -ball.ball_velocity_y
                window.blit(brick.brick_image, (row[0], row[1]))
                brick.number_of_bricks = brick.number_of_bricks - 1
                print(brick.number_of_bricks)

            else:
                window.blit(brick.brick_image, (row[0], row[1]))

        if brick.number_of_bricks == 0:

            game_win.draw_image(window)
            ball.ball_x == 100
            game_over.game_over_x = 100
            bat.bat_x = 1000

        pygame.display.update()

# Print the main functionality of
# the game to play.

main()
pygame.quit()
                








        
