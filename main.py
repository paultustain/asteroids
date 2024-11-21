import pygame
from constants import * 
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys 


def main(): 
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')
        
        
        for p in drawable:
            p.draw(screen)

        for p in updatable:
            p.update(dt)
        
        for a in asteroids:
            if a.collide(player):
                print("Game over!")
                sys.exit()
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == '__main__':
    main()
