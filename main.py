import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Window
    clock = pygame.time.Clock() # In game clock
    dt = 0 # Delta Time (i.e. time passed since last frame drawn)

    ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Main Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        log_state()
        screen.fill("black")
        ship.draw(screen)
        pygame.display.flip()
        rt = clock.tick(60) # pauses the game loop until 1/60th of a second has passed 
        dt = rt / 1000

if __name__ == "__main__":
    main()
