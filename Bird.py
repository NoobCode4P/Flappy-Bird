from Common import *
from Ground import YCOORD_GROUND

class Bird:
    MAX_TILT = 20
    MIN_TILT = -90
    BIRD_IMG = []
    BOUNCE_UP = True

    def __init__(self, x, y, color = 0):
        self.VelocityY = 0
        self.tilt = 0
        self.image_index = 0
        if color == 0:
            self.BIRD_IMG = YELLOW_BIRD_IMG
        elif color == 1:
            self.BIRD_IMG = BLUE_BIRD_IMG
        else:
            self.BIRD_IMG = RED_BIRD_IMG

        for i in range(len(self.BIRD_IMG)):
            self.BIRD_IMG[i].convert_alpha()

        self.image = self.BIRD_IMG[self.image_index]

        self.Rect = self.image.get_rect()
        self.Rect.topleft = (x, y)
        self.state = True

        self.MAX_HEIGHT_BOUNCE_UP = y - 10
        self.MAX_HEIGHT_BOUNCE_DOWN = y + 10
            
    def flyUp(self):
        if self.state:
            self.VelocityY = -7
            if self.Rect.top >= -100:
                self.Rect.top += int(self.VelocityY)
            
            if self.VelocityY >= 0:
                if self.tilt > self.MIN_TILT:
                    self.tilt -= 2

            else:
                if self.tilt < self.MAX_TILT:
                    self.tilt = self.MAX_TILT
                
    def fallDown(self):
        self.VelocityY += 0.5
        if self.VelocityY > 7:     # limit the free-fall velocity
            self.VelocityY = 7
        if self.Rect.top + self.image.get_height() < YCOORD_GROUND:   # yCoord is unchanged when it touches the ground
            self.Rect.top += int(self.VelocityY)
  
        if self.VelocityY >= 0:
            if self.tilt > self.MIN_TILT:
                self.tilt -= 2

        else:
            if self.tilt < self.MAX_TILT:
                self.tilt = self.MAX_TILT

    def bounce(self):
        if self.BOUNCE_UP:
            self.Rect.top -= 1
            if self.Rect.top == self.MAX_HEIGHT_BOUNCE_UP:
                self.BOUNCE_UP = False
        else:
            self.Rect.top += 1
            if self.Rect.top == self.MAX_HEIGHT_BOUNCE_DOWN:
                self.BOUNCE_UP = True

    def draw(self, win):
        self.image_index += 1

        if self.image_index >= 30:
            self.image_index = 0
        
        self.image = self.BIRD_IMG[self.image_index // 10]
        
        self.image = pygame.transform.rotate(self.image, self.tilt)
        
        win.blit(self.image, self.Rect.topleft)

    def getMask(self):
        return pygame.mask.from_surface(self.image)

    def isCollidedWithGround(self):
        if self.Rect.top + self.image.get_height() >= YCOORD_GROUND:
            return True
        return False

    def passPipe(self, pipe):
        return self.Rect.left > pipe.x + pipe.pipeWidth