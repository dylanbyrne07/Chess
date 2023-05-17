import pygame
from board.tile import Tile

from pieces import *
from settings import *


from Pieces.King import King
from Pieces.Queen import Queen
from Pieces.Rook import Rook
from Pieces.Knight import Knight
from Pieces.Bishop import Bishop
from Pieces.Pawn import Pawn



class Chess:
    def __init__(self, surface):
        self.display_surface = surface
        self.setup_level()
        

    def setup_level(self):
        # SETUP LEVEL_____________________________________________
        self.tiles = pygame.sprite.Group()
        self.Pieces = pygame.sprite.Group()
        self.tile_rects = []
        pos_num = -1
        for row_index, row in enumerate(board):
            pos_num += 1
            for col_index, col in enumerate(row):
                pos_num += 1
            
                x = col_index*tile_size
                y = row_index*tile_size
                
                if pos_num % 2:
                    tile = Tile((x, y), tile_size, dark)
                    self.tiles.add(tile)
                else:
                    tile = Tile((x, y), tile_size, light)
                    self.tiles.add(tile)
                #CAN POSITION PIECES AT ANY POINT ON THE BOARD
                if col == 'K':
                    if y > (SCREEN_HEIGHT//2):
                        king = King(x, y, 'white')
                    else:
                        king = King(x, y, 'black')
                    self.Pieces.add(king)
                if col == 'Q':
                    if y > (SCREEN_HEIGHT//2):
                        queen = Queen(x, y, 'white')
                    else:
                        queen = Queen(x, y, 'black')
                    self.Pieces.add(queen)
                if col == 'R':
                    if y > (SCREEN_HEIGHT//2):
                        rook = Rook(x, y, 'white')
                    else:
                        rook = Rook(x, y, 'black')
                    self.Pieces.add(rook)
                if col == 'N':
                    if y > (SCREEN_HEIGHT//2):
                        knight = Knight(x, y, 'white')
                    else:
                        knight = Knight(x, y, 'black')
                    self.Pieces.add(knight)
                if col == 'B':
                    if y > (SCREEN_HEIGHT//2):
                        bishop = Bishop(x, y, 'white')
                    else:
                        bishop = Bishop(x, y, 'black')
                    self.Pieces.add(bishop)
                if col == 'P':
                    if y > (SCREEN_HEIGHT//2):
                        pawn = Pawn(x, y, 'white')
                    else:
                        pawn = Pawn(x, y, 'black')
                    self.Pieces.add(pawn)
                
    
        #SETUP PIECES-----------------------------------------------------------
    
    def run(self):
        
        #Tiles---------------------------------------------------------------------------------------------
        self.tiles.draw(self.display_surface)
        
        #Player--------------------------------------------------------------------------------------------
        
      #  self.move_pieces()
        self.Pieces.draw(self.display_surface)
        
