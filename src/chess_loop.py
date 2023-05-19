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

from FEN_engine import *


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

        fen =  'r1b1k1nr/p2p1pNp/n2B4/1p1NP2P/6P1/3P1Q2/P1P1K3/q5b1'
        board = parse_FEN(fen)
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
                    king = King(x, y, 'white')
                    self.Pieces.add(king)
                elif col == 'k':
                    king = King(x, y, 'black')
                    self.Pieces.add(king)
                if col == 'Q':
                    queen = Queen(x, y, 'white')
                    self.Pieces.add(queen)
                elif col == 'q':
                    queen = Queen(x, y, 'black')
                    self.Pieces.add(queen)

                if col == 'R':
                    rook = Rook(x, y, 'white')
                    self.Pieces.add(rook)
                elif col == 'r':
                    rook = Rook(x, y, 'black')
                    self.Pieces.add(rook)

                if col == 'B':
                    bishop = Bishop(x, y, 'white')
                    self.Pieces.add(bishop)
                elif col == 'b':
                    bishop = Bishop(x, y, 'black')
                    self.Pieces.add(bishop)

                if col == 'N':
                    knight = Knight(x, y, 'white')
                    self.Pieces.add(knight)
                elif col == 'n':
                    knight = Knight(x, y, 'black')
                    self.Pieces.add(knight)

                if col == 'P':
                    pawn = Pawn(x, y, 'white')
                    self.Pieces.add(pawn)
                elif col == 'p':
                    pawn = Pawn(x, y, 'black')
                    self.Pieces.add(pawn)
    
        #SETUP PIECES-----------------------------------------------------------
    
    def run(self):
        
        #Tiles---------------------------------------------------------------------------------------------
        self.tiles.draw(self.display_surface)
        
        #Player--------------------------------------------------------------------------------------------
        
      #  self.move_pieces()
        self.Pieces.draw(self.display_surface)
        
