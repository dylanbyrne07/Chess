import os

import pygame

from chess_loop import Chess
from pieces import Queen
from settings import *
from tile import Tile

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
         #   if event.type == pygame.MOUSEBUTTONUP:
            #    pos = pygame.mouse.get_pos()

          #      clicked_sprites = [s for s in self.Pieces if s.rect.collidepoint(pos)]
           #     print(clicked_sprites)
           

        screen.fill((250, 250, 250))
 
        keys_pressed = pygame.key.get_pressed()
    
        
        
        level.run()
     
        pygame.display.flip()
        
    # close pygame
    pygame.quit()

if __name__ == "__main__":
    main()