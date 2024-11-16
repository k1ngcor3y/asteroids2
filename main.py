# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroidfield import *
from shot import Shot

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    game_clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for iter in updatable:
            iter.update(dt)
            for asteroid in asteroids:
                for shot in shots:
                    if asteroid.collision(shot):
                        asteroid.split()
                        shot.kill()
            for asteroid in asteroids:
                if asteroid.collision(player):
                    print("Game over!")
                    sys.exit()
        for iter in drawable:
            iter.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60)/1000


if __name__ == "__main__":
    main()
