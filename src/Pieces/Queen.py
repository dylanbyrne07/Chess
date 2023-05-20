import pygame 
import os
from settings import tile_size
from pieces import Piece

class Queen(Piece):
    def __init__(self, x, y, colour):
        if colour == 'white':
            self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', '..', 'resources', 'queen-white-16x16.png' ))
        elif colour == 'black':
            self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', '..', 'resources', 'queen-black-16x16.png' ))
        self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
        super().__init__(x, y, self.image)

        self.colour = colour

    def possible_moves(self, board):
        pass