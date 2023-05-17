import os

import pygame

from chess_loop import Chess
from settings import *
from board.tile import Tile

##Variables
clock = pygame.time.Clock()

# Initialise pygame
pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])


level = Chess( screen)

def main():
    running = True
    shoot = False
    while running:

        # Check events
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
         

        screen.fill((250, 250, 250))
 
        keys_pressed = pygame.key.get_pressed()
    
        
        
        level.run()
     
        pygame.display.flip()
        
    # close pygame
    pygame.quit()

if __name__ == "__main__":
    main()