from Bird import Bird
from Ground import *
from Pipe import Pipe
import random

clock = pygame.time.Clock()

class Game:
    speed = 3
    highScore = 0

    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        
    def startGame(self):
        if random.randint(1,2) == 1:
            self.bg = bgDay
        else:
            self.bg = bgNight

        self.generateObjects()

        pressSPACEMsg = gameFont.render("PRESS SPACEBAR", True, WHITE)
        msgCont = gameFont.render("TO FLAP", True, WHITE)
        enterGame = False

        while not enterGame:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    enterGame = False
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bird.flyUp()
                        flapSound.play()
                        self.initializePipes()
                        self.playGame()

            self.bird.bounce()
            self.ground.move()

            self.screen.blit(self.bg, (0,0))
            self.screen.blit(pressSPACEMsg, pressSPACEMsg.get_rect(center = (WINDOW_WIDTH >> 1, (WINDOW_HEIGHT >> 1) // 3)))
            self.screen.blit(msgCont, msgCont.get_rect(center = (WINDOW_WIDTH >> 1, (WINDOW_HEIGHT >> 1) // 3 + 100)))
            self.bird.draw(self.screen)
            self.ground.draw(self.screen)
            
            pygame.display.update()

    def generateObjects(self):
        self.bird = Bird(100, WINDOW_HEIGHT >> 1, random.randint(0,2))
        self.ground = Ground(0, YCOORD_GROUND, self.speed)
        self.pipes = []
        self.score = 0

    def initializePipes(self):
        for i in range(5):
            if len(self.pipes) == 0:
                self.pipes.append(Pipe(WINDOW_WIDTH + 100, self.speed))
            else:
                self.pipes.append(Pipe(self.pipes[len(self.pipes) - 1].getX() + 300, self.speed))

    def checkPipes(self):
        if self.bird.state:
            passed = False
            removePipes = []
            for pipe in self.pipes:
                if pipe.getX() + pipe.pipeWidth < 0:
                    removePipes.append(pipe)

                if not pipe.isPassed and self.bird.passPipe(pipe):
                    pipe.isPassed = True
                    passed = True
                
                pipe.move()
                    
            if passed:
                self.score += 1
                self.pipes.append(Pipe(self.pipes[len(self.pipes) - 1].getX() + 300, self.speed))
                scoreSound.play()

            for rmvPipe in removePipes:
                self.pipes.remove(rmvPipe)

    def checkPipeCollision(self):
        if self.bird.state:
            for pipe in self.pipes:
                if self.bird.Rect.colliderect(pipe.upperRect) or self.bird.Rect.colliderect(pipe.lowerRect): 
                    if pipe.isCollidedWith(self.bird):
                        return True
        return False

    def drawAnimation(self):
        self.screen.blit(self.bg,(0,0))
        for pipe in self.pipes:
            pipe.draw(self.screen) 

        self.ground.draw(self.screen)

        self.bird.draw(self.screen)

        self.printScore(self.screen)

    def playGame(self):
        topleftPlayButton = ((WINDOW_WIDTH >> 1) - (playButton.get_width() >> 1), YCOORD_GROUND - playButton.get_height() - 3)

        self.IS_RUNNING = True
        self.IS_GAMEOVER = False
        while self.IS_RUNNING:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.IS_RUNNING = False
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_SPACE and self.bird.state):
                        self.bird.flyUp()
                        flapSound.play()

                if self.IS_GAMEOVER and event.type == pygame.MOUSEBUTTONDOWN:
                    mPos = pygame.mouse.get_pos()
                    PB_left = topleftPlayButton[0]
                    PB_right = topleftPlayButton[0] + playButton.get_width()
                    PB_top = topleftPlayButton[1]
                    PB_bottom = topleftPlayButton[1] + playButton.get_height()
                    if (PB_left <= mPos[0] and mPos[0] <= PB_right) and (PB_top <= mPos[1] and mPos[1] <= PB_bottom):
                        self.startGame()

            if self.bird.state:
                groundCollision = self.bird.isCollidedWithGround()
                pipesCollision = self.checkPipeCollision()                

                if pipesCollision or groundCollision:
                    hitSound.play()
                    self.bird.state = False
                    self.IS_GAMEOVER = True

            self.bird.fallDown()

            if self.bird.state:
                self.ground.move()

                self.checkPipes()
            
            self.drawAnimation()

            if self.IS_GAMEOVER and self.bird.isCollidedWithGround():
                self.GameOver()

            pygame.display.update()
                                          
        pygame.quit()

    def GameOver(self):
        if self.score > self.highScore:
            self.highScore = self.score

        topleftGameOver = ((WINDOW_WIDTH >> 1) - (gameOverImage.get_width() >> 1),200)
        self.screen.blit(gameOverImage.convert_alpha(), topleftGameOver)
        topleftPlayButton = ((WINDOW_WIDTH >> 1) - (playButton.get_width() >> 1), YCOORD_GROUND - playButton.get_height() - 3)
        self.screen.blit(playButton.convert_alpha(), topleftPlayButton)

        score_surface = gameFont.render("YOUR SCORE: " + str(self.score), True, BLUE)
        score_rect = score_surface.get_rect(center = (WINDOW_WIDTH >> 1, WINDOW_HEIGHT >> 1))
        self.screen.blit(score_surface, score_rect)

        highscore_surface = gameFont.render("BEST SCORE: " + str(self.highScore), True, BLUE)
        highscore_rect = highscore_surface.get_rect(center = (WINDOW_WIDTH >> 1, (WINDOW_HEIGHT >> 1) + 80))
        self.screen.blit(highscore_surface, highscore_rect)
        
    def printScore(self, window):
        digits = []
        tmp = self.score
        startPosX = 5
        startPosY = 0
        if tmp == 0:
            window.blit(NUMBERS_IMG[0].convert_alpha(), (startPosX, startPosY))
        else:
            while tmp > 0:
                digits.append(tmp % 10)
                tmp = tmp // 10
            
            for digit in digits[::-1]:
                window.blit(NUMBERS_IMG[digit].convert_alpha(), (startPosX, startPosY))
                startPosX += NUMBERS_IMG[digit].get_width()
