import pygame
from pygame.sprite import Sprite
from Configurations import Configurations

class TicTacToeMark(Sprite):
    """
    Clase que representa una marca X u O en el tablero del juego del gato.
    Hereda de Sprite para poder ser manejada como imagen con posición.

    Atributos de clase:
        turno: indica si se debe colocar una X o una O.
        marks: grupo de todas las marcas colocadas.
    """

    turno = "X"

    def __init__(self, cell_number: int):
        """
        Constructor de la marca en la celda especificada.

        :param cell_number: número de la celda (1 al 9)
        """
        super().__init__()

        if TicTacToeMark.turno == 'X':
            #markX_image_path = Configurations.get_markX_image_path()
            self.image = pygame.image.load("../media/markX.png")
            TicTacToeMark.turno = 'O'
        else:
            #markO_image_path= Configurations.get_markO_image_path()
            self.image = pygame.image.load("../media/markO.png")
            TicTacToeMark.turno = 'X'
        self.image = pygame.transform.scale(self.image, (80, 80))  # ajusta al tamaño adecuado
        self.rect = self.image.get_rect()  # luego calculamos rect
        self.rect.center = Configurations.get_position(cell_number)

    def blit(self,screen: pygame.surface.Surface):
        """
        Se utiliza para dibujar el fondo de pantalla.
        """
        screen.blit(self.image, self.rect)