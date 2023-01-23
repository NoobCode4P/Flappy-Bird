from Common import *

YCOORD_GROUND = WINDOW_HEIGHT - 110

class Ground:
    groundImg = groundImage

    def __init__(self, x, y, speed):
        self.groundImg.convert_alpha()

        self.Rect1 = self.groundImg.get_rect()
        self.Rect1.topleft = (x, y)

        self.length = self.groundImg.get_width()

        self.Rect2 = self.groundImg.get_rect()
        self.Rect2.topleft = (x + self.length, y)

        self.speed = speed

    def move(self):
        self.Rect1.left -= self.speed
        self.Rect2.left -= self.speed
        if self.Rect1.right < 0:
            self.Rect1.left = self.Rect2.right
        if self.Rect2.right < 0:
            self.Rect2.left = self.Rect1.right

    def draw(self, window):
        window.blit(self.groundImg, self.Rect1.topleft)
        window.blit(self.groundImg, self.Rect2.topleft)
