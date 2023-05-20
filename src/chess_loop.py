import pygame
from board.tile import Tile
from board.possible_moves import Draw_possible_moves

from pieces import *
from settings import *

from Pieces.King import King
from Pieces.Queen import Queen
from Pieces.Rook import Rook
from Pieces.Knight import Knight
from Pieces.Bishop import Bishop
from Pieces.Pawn import Pawn

from FEN_engine.parseFen import *
#from FEN_engine.create_Fen import 


class Chess:
    def __init__(self, surface):
        self.display_surface = surface
        self.setup_board()
        self.players_go = 'white'

    def setup_board(self):
        # SETUP LEVEL_____________________________________________
        self.tiles = pygame.sprite.Group()
        self.Pieces = pygame.sprite.Group()
        self.possible_moves = pygame.sprite.Group()
        self.tile_rects = []
        pos_num = -1

        fen =  '8/8/8/4p1K1/2k1P3/8/8/8'
        self.board = parse_FEN(eg)
        print(self.board)
        for row_index, row in enumerate(self.board):
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
    

    def movement(self, mousepos):
        
        for piece in self.Pieces:
            #if piece.colour == players_go:
                if piece.rect.collidepoint(mousepos):
                    print(piece)
                    print(piece.x)
                #  self.Pieces.remove(piece)
                    possible_moves = piece.get_possible_moves(self.board)

                    for move in possible_moves:
                        print(move)
                        pm = Draw_possible_moves(move[0]*tile_size + tile_size//2, move[1]*tile_size +  tile_size//2, tile_size//2, 'red')
                        self.possible_moves.add(pm)
                    
                #show possible moves
                #position = board[piece.x//tile_size][piece.y//tile_size]
        #SETUP PIECES-----------------------------------------------------------
    
   # def update(self, event_list):
   #     for event in event_list:
     #       if event.type == pygame.MOUSEBUTTONDOWN:
         #       pos=pygame.mouse.get_pos()
        #        self.movement(pos, self.players_go)

     
    def run(self):
        
        #Tiles---------------------------------------------------------------------------------------------
        self.tiles.draw(self.display_surface)
        
        #Player--------------------------------------------------------------------------------------------
        
      #  self.move_pieces()
        self.Pieces.draw(self.display_surface)
        self.possible_moves.draw(self.display_surface)
    