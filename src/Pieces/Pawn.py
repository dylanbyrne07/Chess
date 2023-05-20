import pygame 
import os
from settings import tile_size
from pieces import Piece


class Pawn(Piece):
    def __init__(self, x, y, colour):
        if colour == 'white':
            self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', '..', 'resources', 'pawn-white-16x16.png' ))
        elif colour == 'black':
            self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', '..', 'resources', 'pawn-black-16x16.png' ))
        self.image = pygame.transform.scale(self.image, (tile_size, tile_size))

        self.colour = colour

        self.first_go = True
        super().__init__(x, y, self.image)
    
    def get_possible_moves(self, board):
        row = self.x//tile_size
        col = self.y//tile_size

        if self.first_go == True:
            if self.colour == 'white':
                possible_positions = [[row, col-1], [row, col-2]]
            elif self.colour == 'black':
                possible_positions = [[row, col+1], [row, col+2]]
        elif self.first_go == False:
            if self.colour == 'white':
                possible_positions = [[row, col-1]]
            elif self.colour == 'black':
                possible_positions = [[row, col+1]]
      #  position = board[row][col]
        #possible_positions = board[row-1][col]
        #possible_positions = [row, col-1]
        return possible_positions
       

