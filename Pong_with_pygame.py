
"""
I would like to write pong game using pygame

"""

import pygame
import sys
import os

from ball import Ball
from padds import Padd

pygame.init()

size = width, height = 640, 480
speed = [3, 3]
ball_size = [30, 30]
white = (255, 255, 255)
black = (0, 0, 0)
green = (255, 0 , 0)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Pong Game')


font = pygame.font.Font('freesansbold.ttf', 15)
text = font.render('Player A: 0  Player B: 0', True, black)
textRect = text.get_rect()
textRect.center = (width // 2, 20)

level_1 = Ball(ball_size, height, width)
ball = level_1.show_ball()
ballrect = ball.get_rect(center=(320, 240))


padd_leve01 = Padd(30, 60, 20)
racket_a = padd_leve01.show_padd_a()
racket_b = padd_leve01.show_padd_b()
racket_rect_a = racket_a.get_rect()
racket_rect_b = racket_b.get_rect()


def pad(racket, x, y):
    screen.blit(racket, (x, y))


def keep_padd_inside(y, y_total):
    if y_total < 0:
        y = 2
    if y_total > 440:
        y = -2
    return y


x_a = 0
y_a = (height * 0.4)
y_change_a = 0
x_b = 600
y_b = (height * 0.4)
y_change_b = 0
score_a = 0
score_b = 0

run =True

while run:

    pygame.time.delay(15)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        # Padd movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y_change_a = -5
            elif event.key == pygame.K_s:
                y_change_a = 5
            if event.key == pygame.K_UP:
                y_change_b = -5
            elif event.key == pygame.K_DOWN:
                y_change_b = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                y_change_a = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change_b = 0
    # Keep padds inside of window
    y_a += keep_padd_inside(y_change_a, y_a)
    y_b += keep_padd_inside(y_change_b, y_b)

    # Move the ball and make the ball inside the window
    ballrect = ballrect.move(speed)

    # if ballrect.left < 0 or ballrect.right > width:
    #     speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    # shoot ball with padds

    if (ballrect[1] - 10 <= y_a <= ballrect[1] + 10) and ballrect[0] <= 30:
        speed[0] = -speed[0]

    if (ballrect[1] - 10 <= y_b <= ballrect[1] + 10) and ballrect[0] >= 610:
        speed[0] = -speed[0]

    if ballrect.left < -10:
        score_b += 1
        ballrect = ball.get_rect(center=(320, 240))
    if ballrect.left > 640:
        score_a += 1
        ballrect = ball.get_rect(center=(320, 240))

    text = font.render('Player A: {}  Player B: {}'.format(score_a, score_b), True, black)

    if score_a == 5:
        font = pygame.font.Font('freesansbold.ttf', 25)
        text = font.render('Player A WIN', True, green)
        textRect = text.get_rect()
        textRect.center = (width // 2, height//2)
        screen.blit(text, textRect)
        run = False


    pygame.display.update()
    screen.fill(white)
    pad(racket_a, x_a, y_a)
    pad(racket_b, x_b, y_b)
    screen.blit(ball, ballrect)
    screen.blit(text, textRect)
    pygame.display.flip()