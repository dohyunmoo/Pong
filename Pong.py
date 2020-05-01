import pygame
pygame.init()
from numpy import random

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Pong")

screenwidth = 500

width = 25
height = 100

x1 = (screenwidth - width)
y1 = 200

x2 = 0
y2 = 200

vel = 5

ballr = 10 #radius
balld = ballr + ballr #diameter

ballv_x = 4 #hor. vel
ballv_y = 3 #ver. vel

ballx = 250
bally = 100
ballInitiate = False
ballHor = True
ballVer = True

score1 = 0
score2 = 0

run = True

while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    font = pygame.font.Font(None, 36)

    # player 1 (Right)
    if keys[pygame.K_UP] and y1 > 0:
        y1 -= vel
    if keys[pygame.K_DOWN] and y1 < (screenwidth - height):
        y1 += vel

    # player 2 (Left)
    if keys[pygame.K_w] and y2 > 0:
        y2 -= vel
    if keys[pygame.K_s] and y2 < (screenwidth - height):
        y2 += vel

    # ball
    if ballInitiate:
        if ballHor:
            ballx -= ballv_x
        else:
            ballx += ballv_x

        if ballVer:
            bally -= ballv_y
            if bally <= ballr:
                ballVer = False
        else:
            bally += ballv_y
            if bally >= (screenwidth - ballr):
                ballVer = True

    # Collision
    if (ballx + ballr) >= x1 and (y1 <= bally <= (y1 + height)):
        ballHor = True

    if (ballx - ballr) <= (x2 + width) and (y2 <= bally <= (y2 + height)):
        ballHor = False

    # Game Over
    if (ballx + ballr) >= screenwidth:
        # print("Player 2 wins a point")
        score2 += 1
        ballx = 250;bally = 100;ballInitiate = False

    if (ballx - ballr - ballv_x) <= 0:
        # print("Player 1 wins a point")
        score1 += 1
        ballx = 250;bally = 100;ballInitiate = False

    win.fill((0, 0, 0))

    text = font.render(str(score2), 1, (255, 255, 255))
    win.blit(text, (150, 10))
    text = font.render(str(score1), 1, (255, 255, 255))
    win.blit(text, (350, 10))

    if not ballInitiate:
        font = pygame.font.Font(None, 18)
        direction = "Press SPACE key to Begin..."
        text = font.render(direction, 1, (255, 255, 255))
        win.blit(text, (180, 50))

        if keys[pygame.K_SPACE]:
            x = random.randint(4)
            if x == 0:
                ballHor = False
                ballVer = False
            elif x == 1:
                ballHor = True
                ballVer = False
            elif x == 2:
                ballHor = False
                ballVer = True
            else:
                ballHor = True
                ballVer = True

            ballInitiate = True

    pygame.draw.rect(win, (255, 0, 0), (x1, y1, width, height))
    pygame.draw.rect(win, (0, 255, 0), (x2, y2, width, height))
    pygame.draw.circle(win, (255, 255, 255), (ballx, bally), ballr)
    pygame.display.update()

pygame.quit()
