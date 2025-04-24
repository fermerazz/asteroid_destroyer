import pygame
from constants import *
from player import Player

def __main__():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    Clock = pygame.time.Clock()
    dt = 0 #Change in frames over last call 

    #Creating a display screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player  = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)

    #Infinite game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        Clock.tick(60)
        dt = Clock.tick(60)/1000
        

    






if __name__ == "__main__":
    __main__()