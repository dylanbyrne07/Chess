

import pygame 
import os
from settings import tile_size

class Piece(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x,y))
        self.x = x
        self.y = y
        self.width = self.rect.width
        self.height = self.rect.height
    
    def move(self):
        
        for event in pygame.event.get():
    
            if event.type == pygame.MOUSEBUTTONDOWN:           
                if self.rect.colliderect(pygame.mouse.get_pos()):
                    print("Mouse clicked on the Player")
    
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    print("Mouse released on the Player")
        # clicked_sprites = [s for s in sprites if s.rect.collidepoint(pos)]

                # do something with the clicked sprites...
    def get_row_col_from_mouse(self, pos):
        x, y = pos
        row = y // tile_size
        col = x // tile_size
        return row, col
    
    def get_self_row_col(self):

        row = self.y // tile_size
        col = self.x // tile_size
        return row, col

    def move_pieces(self):
        ev = pygame.event.get()

        for event in ev:

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                mouse_row, mouse_col = self.get_row_col_from_mouse(pos)
                self_row, self_col = self.get_self_row_col()
                print(self_row)
                print(self_col)
                print(mouse_row)
                print(mouse_col)

        
class King(Piece):
    def __init__(self, x, y, colour):
        if colour == 'white':
            self.image = pygame.image.load(os.path.join('resources', 'king-white-16x16.png'))
        elif colour == 'black':
            self.image = pygame.image.load(os.path.join('resources', 'king-black-16x16.png'))
        self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
        super().__init__(x, y, self.image)

class Queen(Piece):
    def __init__(self, x, y, colour):
        if colour == 'white':
            self.image = pygame.image.load(os.path.join('resources', 'queen-white-16x16.png'))
        elif colour == 'black':
            self.image = pygame.image.load(os.path.join('resources', 'queen-black-16x16.png'))
        self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
        super().__init__(x, y, self.image)


class Bishop(Piece):
    def __init__(self, x, y, colour):
        if colour == 'white':
            self.image = pygame.image.load(os.path.join('resources', 'bishop-white-16x16.png'))
        elif colour == 'black':
            self.image = pygame.image.load(os.path.join('resources', 'bishop-black-16x16.png'))
        self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
        super().__init__(x, y, self.image)

class Rook(Piece):
    def __init__(self, x, y, colour):
        if colour == 'white':
            self.image = pygame.image.load(os.path.join('resources', 'rook-white-16x16.png'))
        elif colour == 'black':
            self.image = pygame.image.load(os.path.join('resources', 'rook-black-16x16.png'))
        self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
        super().__init__(x, y, self.image)

class Knight(Piece):
    def __init__(self, x, y, colour):
        if colour == 'white':
            self.image = pygame.image.load(os.path.join('resources', 'knight-white-16x16.png'))
        elif colour == 'black':
            self.image = pygame.image.load(os.path.join('resources', 'knight-black-16x16.png'))
        self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
        super().__init__(x, y, self.image)

class Pawn(Piece):
    def __init__(self, x, y, colour):
        if colour == 'white':
            self.image = pygame.image.load(os.path.join('resources', 'pawn-white-16x16.png'))
        elif colour == 'black':
            self.image = pygame.image.load(os.path.join('resources', 'pawn-black-16x16.png'))
        self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
        super().__init__(x, y, self.image)

