import pygame
pygame.init()
from numpy import random
import Class as C

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Pong")

screenwidth = 500

score1 = 0
score2 = 0

run = True

ball = C.Ball()
player1 = C.Player(screenwidth - 25)
player2 = C.Player(0)

while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    font = pygame.font.Font(None, 36)

    # player 1 (Right)
    if keys[pygame.K_UP] and player1.y > 0:
        player1.y -= player1.vel
    if keys[pygame.K_DOWN] and player1.y < (screenwidth - player1.height):
        player1.y += player1.vel

    # player 2 (Left)
    if keys[pygame.K_w] and player2.y > 0:
        player2.y -= player2.vel
    if keys[pygame.K_s] and player2.y < (screenwidth - player2.height):
        player2.y += player2.vel

    # ball
    if ball.ballInitiate:
        if ball.ballHor:
            ball.ballx -= ball.ballv_x
        else:
            ball.ballx += ball.ballv_x

        if ball.ballVer:
            ball.bally -= ball.ballv_y
            if ball.bally <= ball.ballr:
                ball.ballVer = False
        else:
            ball.bally += ball.ballv_y
            if ball.bally >= (screenwidth - ball.ballr):
                ball.ballVer = True

    # Collision
    if (ball.ballx + ball.ballr) >= player1.x and (player1.y <= ball.bally <= (player1.y + player1.height)):
        ball.ballHor = True

    if (ball.ballx - ball.ballr) <= (player2.x + player2.width) and (player2.y <= ball.bally <= (player2.y + player2.height)):
        ball.ballHor = False

    # Game Over
    if (ball.ballx + ball.ballr) >= screenwidth:
        # print("Player 2 wins a point")
        score2 += 1
        ball.ballx = 250
        ball.bally = 100
        ball.ballInitiate = False

    if (ball.ballx - ball.ballr - ball.ballv_x) <= 0:
        # print("Player 1 wins a point")
        score1 += 1
        ball.ballx = 250
        ball.bally = 100
        ball.ballInitiate = False

    win.fill((255, 255, 255))

    text = font.render(str(score2), 1, (0, 0, 0))
    win.blit(text, (150, 10))
    text = font.render(str(score1), 1, (0, 0, 0))
    win.blit(text, (350, 10))

    if not ball.ballInitiate:
        font = pygame.font.Font(None, 18)
        direction = "Press SPACE key to Begin..."
        text = font.render(direction, 1, (0, 0, 0))
        win.blit(text, (180, 50))

        if keys[pygame.K_SPACE]:
            x = random.randint(4)
            if x == 0:
                ball.ballHor = False
                ball.ballVer = False
            elif x == 1:
                ball.ballHor = True
                ball.ballVer = False
            elif x == 2:
                ball.ballHor = False
                ball.ballVer = True
            else:
                ball.ballHor = True
                ball.ballVer = True

            ball.ballInitiate = True

    pygame.draw.rect(win, (255, 0, 0), (player1.x, player1.y, player1.width, player1.height))
    pygame.draw.rect(win, (0, 255, 0), (player2.x, player2.y, player2.width, player2.height))
    pygame.draw.circle(win, (0, 0, 0), (ball.ballx, ball.bally), ball.ballr)
    pygame.display.update()

pygame.quit()
