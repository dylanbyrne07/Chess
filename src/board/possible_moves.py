import pygame

class Draw_possible_moves(pygame.sprite.Sprite):
    def __init__(self, x, y, size, color):
        super().__init__() 
        self.original_image = pygame.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.circle(self.original_image, color, (25, 25), 25)

    #    self.click_image = pygame.Surface((50, 50), pygame.SRCALPHA)
    #    pygame.draw.circle(self.click_image, color, (25, 25), 25)
     #   pygame.draw.circle(self.click_image, (255, 255, 255), (25, 25), 25, 4)

        self.image = self.original_image 
        self.rect = self.image.get_rect(center = (x, y))
        self.clicked = False


###
    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.clicked = not self.clicked

        self.image = self.click_image if self.clicked else self.original_image