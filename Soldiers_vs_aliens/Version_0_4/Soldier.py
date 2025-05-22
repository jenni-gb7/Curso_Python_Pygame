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
        #Llamasa al constructor de la clase padre (Sprite)
        super().__init__()

        # Imagenes atraves de su método de acceso.
        personaje_image_path = Configurations.get_personaje_image_path()
        self.image = pygame.image.load(personaje_image_path)

        # Escala de la imagen.
        soldado_size = Configurations.get_soldado_block_size()
        self.image = pygame.transform.scale(self.image, soldado_size)

        self.rect = self.image.get_rect()

        #Posicion el soldado
        screen_rect = screen.get_rect()
        self.rect.center = screen_rect.center
        self.rect.right = screen_rect.right

        # Banderas de instancia para el movimiento del personaje.
        self._is_moving_up = False
        self._is_moving_down = False

    def blit(self, screen: pygame.surface.Surface):
        """
        Se utiliza para dibujar el soldado en pantalla.
        """
        screen.blit(self.image, self.rect)  #dibujo la imagen del soldado en la superficie de la pantalla.

    def update_position(self):
        """
        Se utiliza para el movimiento del soldado (arriba y abajo).
        """
        if self._is_moving_up:
            self.rect.y -= 10
        if self._is_moving_down:
            self.rect.y += 10

    # -------------------Metodos de acceso
    #movinj up y down, update. getter y setter

    #getter
    @property
    def is_moving_up(self) -> int:
        return self._is_moving_up

    @is_moving_up.setter
    def is_moving_up(self, is_moving_upt: int) -> None:
        self._is_moving_up= is_moving_upt

    @property
    def is_moving_down(self) -> int:
        return self._is_moving_down

    @is_moving_down.setter
    def is_moving_down(self, is_moving_downt: int) -> None:
        self._is_moving_down = is_moving_downt



