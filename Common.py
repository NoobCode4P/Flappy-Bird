import pygame, sys
from pygame import mixer
from os import path

pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.font.init()

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 748

WHITE = (255,255,255)
BLUE = (0,0,255)

cwd = path.dirname(__file__)

gameFont = pygame.font.SysFont("Comic Sans MS", 40)

backgroundNightImgFile = path.join(cwd, 'gameImage/bg_night.png')
backgroundDayImgFile = path.join(cwd, 'gameImage/bg_day.png')

playButton = pygame.image.load(path.join(cwd, 'gameImage/PlayButton.png'))

yellowbirdImgFile = {
    "flapDown" : path.join(cwd,"gameImage/yellowbird-downflap.png"),
    "flapMid" : path.join(cwd,"gameImage/yellowbird-midflap.png"),
    "flapUp" : path.join(cwd,"gameImage/yellowbird-upflap.png"),
}

bluebirdImgFile = {
    "flapDown" : path.join(cwd,"gameImage/bluebird-downflap.png"),
    "flapMid" : path.join(cwd,"gameImage/bluebird-midflap.png"),
    "flapUp" : path.join(cwd,"gameImage/bluebird-upflap.png"),
}

redbirdImgFile = {
    "flapDown" : path.join(cwd,"gameImage/redbird-downflap.png"),
    "flapMid" : path.join(cwd,"gameImage/redbird-midflap.png"),
    "flapUp" : path.join(cwd,"gameImage/redbird-upflap.png"),
}

groundImgFile = path.join(cwd,"gameImage/ground.png")

pipeImgFile = path.join(cwd,"gameImage/pipe-green.png")

gameoverImgFile = path.join(cwd,"gameImage/gameover.png")

gameTitleImgFile = path.join(cwd,"gameImage/title.png")

#===================NUMBERS=================
NUMBERS_IMG = []

for i in range(0,10):
    dir = "gameImage/" + str(i) + ".png"
    imageNumber = pygame.image.load(path.join(cwd, dir))
    imageNumber = pygame.transform.scale2x(imageNumber)
    NUMBERS_IMG.append(imageNumber)

#==============images=================
#******YELLOW BIRD*******
downFlapY = pygame.image.load(yellowbirdImgFile["flapDown"])
midFlapY = pygame.image.load(yellowbirdImgFile["flapMid"])
upFlapY = pygame.image.load(yellowbirdImgFile["flapUp"])

downFlapY = pygame.transform.scale2x(downFlapY)
midFlapY = pygame.transform.scale2x(midFlapY)
upFlapY = pygame.transform.scale2x(upFlapY)

YELLOW_BIRD_IMG = [downFlapY, midFlapY, upFlapY]

#******BLUE BIRD*******
downFlapB = pygame.image.load(bluebirdImgFile["flapDown"])
midFlapB = pygame.image.load(bluebirdImgFile["flapMid"])
upFlapB = pygame.image.load(bluebirdImgFile["flapUp"])

downFlapB = pygame.transform.scale2x(downFlapB)
midFlapB = pygame.transform.scale2x(midFlapB)
upFlapB = pygame.transform.scale2x(upFlapB)

BLUE_BIRD_IMG = [downFlapB, midFlapB, upFlapB]

#******RED BIRD*******
downFlapR = pygame.image.load(redbirdImgFile["flapDown"])
midFlapR = pygame.image.load(redbirdImgFile["flapMid"])
upFlapR = pygame.image.load(redbirdImgFile["flapUp"])

downFlapR = pygame.transform.scale2x(downFlapR)
midFlapR = pygame.transform.scale2x(midFlapR)
upFlapR = pygame.transform.scale2x(upFlapR)

RED_BIRD_IMG = [downFlapR, midFlapR, upFlapR]

#******GROUND*******
groundImage = pygame.transform.scale2x(pygame.image.load(groundImgFile))

#******PIPE*******
pipeImage = pygame.image.load(pipeImgFile)
pipeImage = pygame.transform.scale(pipeImage, (82,506))

#******BACKGROUND********
bgNight = pygame.image.load(backgroundNightImgFile)
bgNight = pygame.transform.scale(bgNight, (WINDOW_WIDTH, WINDOW_HEIGHT))

bgDay = pygame.image.load(backgroundDayImgFile)
bgDay = pygame.transform.scale(bgDay, (WINDOW_WIDTH, WINDOW_HEIGHT))

#*******GAMEOVER*******
gameOverImage = pygame.image.load(gameoverImgFile)
gameOverImage = pygame.transform.scale2x(gameOverImage)

#********GAME TITLE***********
gameTitleImage = pygame.image.load(gameTitleImgFile)

#============================SOUND=================================
flapSound = pygame.mixer.Sound(path.join(cwd,'sound/sfx_wing.wav'))

hitSound = pygame.mixer.Sound(path.join(cwd,'sound/sfx_hit.wav'))

scoreSound = pygame.mixer.Sound(path.join(cwd,'sound/sfx_score.wav'))
