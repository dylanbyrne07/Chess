import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, colour):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(colour)
        self.rect = self.image.get_rect(topleft=pos)
        #self.y = self.rect.y
        
        self.bottom = self.rect.bottom
        self.top = self.rect.top
        self.right = self.rect.right
        self.left = self.rect.left
        self.colour = colour