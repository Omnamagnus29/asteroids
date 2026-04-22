import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys



def main():
    pygame.init()
    print("Starting Asteroids with pygame version: VERSION")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 17 / 1000

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    asteroid_field_object = AsteroidField()

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        
        updatable.update(dt)

        for asteroid_object in asteroids:
            if asteroid_object.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        
        for asteroid_objects in asteroids:
            for shot_attack in shots:
                if asteroid_objects.collides_with(shot_attack):
                    log_event("asteroid_shot")
                    asteroid_objects.kill()
                    shot_attack.kill()


        for character in drawable:
            character.draw(screen)

    
    
        # player.draw(screen)

        pygame.display.flip()

        clock.tick(60)

# def main():
#     pygame.init()
#     screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#     clock = pygame.time.Clock()

#     updatable = pygame.sprite.Group()
#     drawable = pygame.sprite.Group()

#     Player.containers = (updatable, drawable)

#     player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
#     dt = 0

#     while True:
#         log_state()
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 return
#         screen.fill("black")
#         for obj in drawable:
#             obj.draw(screen)
#         pygame.display.flip()
#         dt = clock.tick(60) / 1000
      

if __name__ == "__main__":
    main()
