# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import * 
from player import *
def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player1 = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    while True:
        """
        This will check if the user has closed the 
        window and exit the game loop if they do. 
        It will make the window's close button work.
        """
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                return
   
        screen.fill(color=000000) #fills the screen with black color
        player1.draw(screen)
        pygame.display.flip() #refreshes the screen
 

        #dt = clock.tick(60) /1000
        #print(f"FPS: {clock.get_fps():.2f}")


if __name__ == "__main__":
    main()