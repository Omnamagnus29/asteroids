import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player




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

    Player.containers = (updatable, drawable)

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        
        updatable.update(dt)

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
