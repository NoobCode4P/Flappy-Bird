from Common import*
import random

class Pipe:
    pipeImg = pipeImage
    pipeHeight = pipeImg.get_height()
    pipeWidth = pipeImg.get_width()

    def __init__(self, left, speed):
        self.x = left
        self.upperPipe = pygame.transform.rotate(self.pipeImg,180).convert_alpha()
        self.lowerPipe = self.pipeImg.convert_alpha()
        self.distance = 150
        self.speed = speed

        self.upperRect = self.upperPipe.get_rect()
        self.upperRect.left = left
        self.lowerRect = self.lowerPipe.get_rect()
        self.lowerRect.left = left

        self.build()

        self.isPassed = False

    def getX(self):
        return self.x

    def build(self):
        yBottomOfTopPipe = random.randint(int(self.pipeHeight / 5), int((self.pipeHeight << 2) / 5))
        self.upperRect.bottom = yBottomOfTopPipe
        self.lowerRect.top = yBottomOfTopPipe + self.distance
    
    def move(self):
        self.x -= self.speed
        self.upperRect.left = self.x
        self.lowerRect.left = self.x
    
    def draw(self, window):
        window.blit(self.upperPipe, (self.x, self.upperRect.top))
        window.blit(self.lowerPipe, (self.x, self.lowerRect.top))
    
    def isCollidedWith(self, bird):          # PIXEL-PERFECT COLLISION
        birdMask = bird.getMask()
        upMask = pygame.mask.from_surface(self.upperPipe)
        loMask = pygame.mask.from_surface(self.lowerPipe)
        
        uOffset = (self.x - bird.Rect.left, self.upperRect.top - bird.Rect.top)
        lOffset = (self.x - bird.Rect.left, self.lowerRect.top - bird.Rect.top)

        pointOfUpperIntersection = birdMask.overlap(upMask, uOffset)
        pointOfLowerIntersection = birdMask.overlap(loMask, lOffset)

        if pointOfUpperIntersection or pointOfLowerIntersection:
            return True
        return False
