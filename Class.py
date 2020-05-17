import pygame
pygame.init()
from numpy import random

pygame.display.set_caption("Pong")

screenwidth = 850
screenheight = 650
win = pygame.display.set_mode((screenwidth, screenheight))

score1 = 0
score2 = 0

run = True


class Ball(object):
    def __init__(self):
        self.ballx = int(screenwidth/2)
        self.bally = int(screenheight/2)
        self.ballr = 10  # radius
        self.balld = self.ballr + self.ballr  # diameter

        self.ballv_x = 4  # hor. vel
        self.ballv_y = 3  # ver. vel

        self.ballInitiate = False
        self.ballHor = True # if true, move left; if false, move right
        self.ballVer = True

        self.count = 0

    def collision_count(self):
        if self.ballHor:
            self.ballHor = False
        else:
            self.ballHor = True

        self.count += 1

    def update_ball(self):
        self.ballv_x += 2
        self.ballv_y += 3
        self.count += 1

    def reset_ball(self):
        self.ballv_x = 4
        self.ballv_y = 3
        self.count = 0
        self.ballx = int(screenwidth/2)
        self.bally = int(screenheight/2)
        self.ballInitiate = False

    def start(self):
        x = random.randint(4)
        if x == 0:
            self.ballHor = False
            self.ballVer = False
        elif x == 1:
            self.ballHor = True
            self.ballVer = False
        elif x == 2:
            self.ballHor = False
            self.ballVer = True
        else:
            self.ballHor = True
            self.ballVer = True

        self.ballInitiate = True


class Player(object):
    def __init__(self):
        self.width = 15
        self.height = 100
        self.x = None
        self.y = int(screenheight/2 - self.height/2)
        self.vel = 5

    def update_player(self):
        self.height -= 10
        self.height -= 10
        self.vel += 1
        self.vel += 1

    def reset_player(self):
        self.height = 100
        self.y = int(screenheight/2 - self.height/2)
