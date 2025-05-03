import pygame
from constants import *
from player import PlayerClass

screen = pygame.display.set_mode((1280, 720))

def main():
    print ("Starting Asteroids!")
    print (f"Screen width: 1280")
    print (f"Screen height: 720")
    game_run = pygame.init()
    game_clock = pygame.time.Clock()
    player = PlayerClass(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    while game_run:
        screen.fill("black")
        
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        ticker = game_clock.tick(60)
        dt += ticker / 1000
        

if __name__ == "__main__":
    main()
    