import pygame
from pygame.sprite import Sprite

# Concepto de herencia.
class SnakeBlock(Sprite):

    def __init__(self):
        """
        Constructor de la clase.
        """
        super().__init__()
        color = (255,0,0)

        # Un cuadro de 40 * 40.
        self.image = pygame.Surface((40,40))
        # Relleno de color.
        self.image.fill(color)

        self.rect = self.image.get_rect()

    def blit(self,screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para dibujar el bloque de la serpiente.
        :param screen: Pantlla en donde se dibuja.
        """

        screen.blit(self.image, self.rect)