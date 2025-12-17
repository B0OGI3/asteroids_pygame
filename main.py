import pygame, sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Window
    clock = pygame.time.Clock() # In game clock
    dt = 0 # Delta Time (i.e. time passed since last frame drawn)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

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

        for up in updatable:
            up.update(dt)

        for ast in asteroids:
            if ast.collides_with(ship):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
            for sh in shots:
                if ast.collides_with(sh):
                    sh.kill()
                    ast.split()
        
        for dr in drawable:
            dr.draw(screen)

        pygame.display.flip()
        rt = clock.tick(60) # pauses the game loop until 1/60th of a second has passed 
        dt = rt / 1000

if __name__ == "__main__":
    main()
