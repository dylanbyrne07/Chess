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
    
  #  def possible_moves():
   #     print("hello")

    
