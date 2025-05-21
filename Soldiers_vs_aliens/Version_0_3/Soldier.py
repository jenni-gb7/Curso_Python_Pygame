import pygame
from pygame.sprite import Sprite
from Configurations import Configurations

class Soldier(Sprite):
    def __init__(self, screen: pygame.surface.Surface):

        super().__init__()

        personaje = Configurations.get_personaje()
        _soldier_block_size = Configurations.get_soldier_block_size()
        self.rect = self.image.get_rect()

        snake_block_size = Configurations.get_snake_block_size()
        self.image = pygame.Surface((snake_block_size, snake_block_size))

        self.rect = self.image.get_rect()
    def blit(self, screen: pygame.surface.Surface):
        """
        Se utiliza para dibujar el fondo de pantalla.
        """
        screen.blit(self.image, self.rect)