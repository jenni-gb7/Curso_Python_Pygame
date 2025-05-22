"""
Nombre: Equipo los Bugs
Fecha: 13 de mayo del 2025.

Descripción:
"""

import pygame
from Configurations import Configurations


class Background:
    """
    Clase que contiene el fondo de pantalla.
    """

    def __init__(self):
        background_image_path = Configurations.get_background_image_path()  # Obtenemos la ruta de la imagen de fondo.
        self.image = pygame.image.load(background_image_path)

        # Escalamos la imagen para que coincida con el tamaño de la pantalla.
        screen_size = Configurations.get_screen_size()
        self.image = pygame.transform.scale(self.image, screen_size)

        self.rect = self.image.get_rect()

    def blit(self, screen: pygame.surface.Surface):
        """
        Se utiliza para dibujar el fondo de pantalla.
        """
        screen.blit(self.image, self.rect)  # Dibujamos la imagen del fondo en la superficie de la pantalla.