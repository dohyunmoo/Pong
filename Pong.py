import Class as C
import pygame
pygame.init()

ball = C.Ball()
player1 = C.Player()
player2 = C.Player()

player1.x = int(C.screenwidth - player1.width)
player2.x = 0

C.win

while C.run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            C.run = False

    keys = pygame.key.get_pressed()
    font = pygame.font.Font(None, 36)

    # player 1 (Right)
    if keys[pygame.K_UP] and player1.y > 0:
        player1.y -= player1.vel
    if keys[pygame.K_DOWN] and player1.y < (C.screenheight - player1.height):
        player1.y += player1.vel

    # player 2 (Left)
    if keys[pygame.K_w] and player2.y > 0:
        player2.y -= player2.vel
    if keys[pygame.K_s] and player2.y < (C.screenheight - player2.height):
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
            if ball.bally >= (C.screenheight - ball.ballr):
                ball.ballVer = True

    # Collision
    if ((((ball.ballx + ball.ballr) >= player1.x) and (player1.y <= ball.bally <= (player1.y + player1.height)))\
            or (((ball.ballx - ball.ballr) <= (player2.x + player2.width)) and (player2.y <= ball.bally <= (player2.y + player2.height)))):
        ball.collision_count()

    # Game Over
    if (ball.ballx + ball.ballr) >= C.screenwidth:
        # print("Player 2 wins a point")
        C.score2 += 1
        ball.reset_ball()

    if (ball.ballx - ball.ballr - ball.ballv_x) <= 0:
        # print("Player 1 wins a point")
        C.score1 += 1
        ball.reset_ball()

    C.win.fill((255, 255, 255))

    # Progressive Updates
    if ((ball.count % 7) == 0) and (ball.count != 0) and (ball.count <= 30):
        player1.update_player()
        player2.update_player()
        ball.update_ball()

    text = font.render(str(C.score2), 1, (0, 0, 0))
    C.win.blit(text, (int(C.screenwidth/2 - 100), 10))
    text = font.render(str(C.score1), 1, (0, 0, 0))
    C.win.blit(text, (int(C.screenwidth/2 + 100), 10))

    if not ball.ballInitiate:
        player1.reset_player()
        player2.reset_player()

        font = pygame.font.Font(None, 18)
        direction = "Press SPACE key to Begin..."
        text = font.render(direction, 1, (0, 0, 0))
        C.win.blit(text, (int(C.screenwidth/2 - 70), 50))

        if keys[pygame.K_SPACE]:
            ball.start()

    pygame.draw.circle(C.win, (0, 0, 0), (ball.ballx, ball.bally), ball.ballr)
    pygame.draw.rect(C.win, (255, 0, 0), (player1.x, player1.y, player1.width, player1.height))
    pygame.draw.rect(C.win, (0, 255, 0), (player2.x, player2.y, player2.width, player2.height))

    pygame.display.update()

pygame.quit()
