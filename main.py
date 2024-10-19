# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import * 
from player import *
from asteroid import *
from asteroidfield import *
def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player1 = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()


    while True:
        """
        This will check if the user has closed the 
        window and exit the game loop if they do. 
        It will make the window's close button work.
        """
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        screen.fill("black") #fills the screen with black color

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip() #refreshes the screen
        
        dt = clock.tick(60) /1000 #limits the FPS to 60 (if computer-power allows)
        #print(f"FPS: {clock.get_fps():.2f}")


if __name__ == "__main__":
    main()