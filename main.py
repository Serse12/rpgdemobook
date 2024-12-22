import sys, pygame
from FirstMap.FirstMap import FirstMap
from config import *

def main():
    pygame.init()

    size = width, height = WINDOW_WIDTH, WINDOW_HEIGHT
    speed = [2, 2]
    black = 0, 0, 0
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    firstMap = FirstMap(screen)
    # ball = pygame.image.load("img/photo_2024-10-23_21-56-02.jpg")
    # ballrect = ball.get_rect()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()


        firstMap.draw()

        screen.fill(black)
        firstMap.draw()
        # screen.blit(ball, ballrect)
        pygame.display.flip()
        clock.tick(60)

if __name__=="__main__":
    main()