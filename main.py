import pygame
from constants import *
from logger import log_state
from player import Player

def main():
    print("Starting Asteroids with pygame version: 2.6.1")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    pygame.init()
    display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        display.fill("black")
        dt = clock.tick(60) / 1000.0
        for updatable_object in updatable:
            updatable_object.update(dt)
        for drawable_object in drawable:
            drawable_object.draw(display)
        pygame.display.flip()

if __name__ == "__main__":
    main()
