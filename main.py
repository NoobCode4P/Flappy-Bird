from Game import *

gameTitle = gameTitleImage
topleftGameTitle = ((WINDOW_WIDTH >> 1) - (gameTitle.get_width() >> 1), 100)
topleftPlayButton = ((WINDOW_WIDTH >> 1) - (playButton.get_width() >> 1), YCOORD_GROUND - 60 - playButton.get_height())
topleftFlappyBird = ((WINDOW_WIDTH >> 1) - (RED_BIRD_IMG[0].get_width() >> 1), topleftGameTitle[1] + 200)
clickMsg = gameFont.render("CLICK TO PLAY", True, WHITE)

bg = bgDay
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
flappyBird = Bird(topleftFlappyBird[0], topleftFlappyBird[1], 0)
movingGround = Ground(0, YCOORD_GROUND, 3)

def printScreen():
    movingGround.move()
    screen.blit(bg,(0,0))
    screen.blit(gameTitle.convert_alpha(), topleftGameTitle)
    flappyBird.draw(screen)
    movingGround.draw(screen)
    screen.blit(playButton, topleftPlayButton)
    screen.blit(clickMsg, clickMsg.get_rect(center = (WINDOW_WIDTH >> 1, YCOORD_GROUND - 30)))
    pygame.display.update()

def startingScreen():
    pygame.display.set_caption("Flappy Bird")
    global CLICK

    CLICK = False
    while not CLICK:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                CLICK = True
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mPos = pygame.mouse.get_pos()
                PB_left = topleftPlayButton[0]
                PB_right = topleftPlayButton[0] + playButton.get_width()
                PB_top = topleftPlayButton[1]
                PB_bottom = topleftPlayButton[1] + playButton.get_height()
                if (PB_left <= mPos[0] and mPos[0] <= PB_right) and (PB_top <= mPos[1] and mPos[1] <= PB_bottom):
                    CLICK = True
        flappyBird.bounce()
        printScreen()

def main():
    startingScreen()
    if CLICK:
        game = Game()
        game.startGame()
    
main()
