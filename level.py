import sys, pygame
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 255, 255, 255

screen = pygame.display.set_mode(size)

ball = pygame.image.load("img/Ball_1.jpg")
ball = pygame.transform.scale(ball, (50, 50))
ballrect = ball.get_rect()

while 1:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    print( ballrect)
    print(speed[0], speed[1])
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()