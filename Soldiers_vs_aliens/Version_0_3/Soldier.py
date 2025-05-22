"""
Nombre: Equipo los Bugs
Fecha: 13 de mayo del 2025.

Descripción:

"""

import pygame
from pygame.sprite import Sprite

from Configurations import Configurations


class Soldiers(Sprite):
    """
    Clase que maneja la imagen del personaje.
    """

    def __init__(self, screen):
        #llame al constructor de la clase padre (Sprite)
        super().__init__()

        personaje_image_path = Configurations.get_personaje_image_path()
        self.image = pygame.image.load(personaje_image_path)

        #escalar la imagen para que coincida con el tamaño configurado
        soldado_size = Configurations.get_soldado_block_size()
        self.image = pygame.transform.scale(self.image, soldado_size)

        #el rect después de escalar la imagen
        self.rect = self.image.get_rect()

        #posicion el soldado
        screen_rect = screen.get_rect()
        self.rect.centery = screen_rect.centery
        self.rect.right = screen_rect.right
        #c self.rect.center = screen_rect.center
        """
        i
        self.rect.centery = screen_rect.centery
        self.rect.left = screen_rect.left

        """

    def blit(self, screen: pygame.surface.Surface):
        """
        Se utiliza para dibujar el soldado en pantalla.
        """
        screen.blit(self.image, self.rect)  #dibujo la imagen del soldado en la superficie de la pantalla.