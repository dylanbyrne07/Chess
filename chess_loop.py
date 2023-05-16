import pygame
from tile import Tile

from pieces import *
from settings import *


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
                        king = King(x, y, 'black')
                    else:
                        king = King(x, y, 'white')
                    self.Pieces.add(king)
                if col == 'Q':
                    if y > (SCREEN_HEIGHT//2):
                        queen = Queen(x, y, 'black')
                    else:
                        queen = Queen(x, y, 'white')
                    self.Pieces.add(queen)
                if col == 'R':
                    if y > (SCREEN_HEIGHT//2):
                        rook = Rook(x, y, 'black')
                    else:
                        rook = Rook(x, y, 'white')
                    self.Pieces.add(rook)
                if col == 'N':
                    if y > (SCREEN_HEIGHT//2):
                        knight = Knight(x, y, 'black')
                    else:
                        knight = Knight(x, y, 'white')
                    self.Pieces.add(knight)
                if col == 'B':
                    if y > (SCREEN_HEIGHT//2):
                        bishop = Bishop(x, y, 'black')
                    else:
                        bishop = Bishop(x, y, 'white')
                    self.Pieces.add(bishop)
                if col == 'P':
                    if y > (SCREEN_HEIGHT//2):
                        pawn = Pawn(x, y, 'black')
                    else:
                        pawn = Pawn(x, y, 'white')
                    self.Pieces.add(pawn)
                
    def move_pieces(self):
        
        ev = pygame.event.get()

        for event in ev:

            if event.type == pygame.MOUSEBUTTONUP:
               
                pos = pygame.mouse.get_pos()
                mouse_row, mouse_col = self.Pieces[1].get_row_col_from_mouse(pos)
                print(mouse_col, mouse_row)
            #    print(self_row)
            #    print(self_col)
              #  print(mouse_row)
              #  print(mouse_col)
        
        #SETUP PIECES-----------------------------------------------------------
    
    def run(self):
        
        #Tiles---------------------------------------------------------------------------------------------
        self.tiles.draw(self.display_surface)
        
        #Player--------------------------------------------------------------------------------------------
        
      #  self.move_pieces()
        self.Pieces.draw(self.display_surface)
        self.move_pieces()
      #  self.move_pieces()
       # if pygame.sprite.spritecollideany(self.player_sprite, self.tiles):
          #  self.player_sprite.collision_done()