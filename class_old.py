class Ball(object):
    def __init__(self):
        self.ballx = 250
        self.bally = 100
        self.ballr = 10  # radius
        self.balld = self.ballr + self.ballr  # diameter

        self.ballv_x = 4  # hor. vel
        self.ballv_y = 3  # ver. vel

        self.ballInitiate = False
        self.ballHor = True
        self.ballVer = True

class Player(object):
    def __init__(self, x):
        self.width = 25
        self.height = 100
        self.x = x
        self.y = 200
        self.vel = 5
