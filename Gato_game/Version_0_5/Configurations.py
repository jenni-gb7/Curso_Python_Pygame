import pygame

class Configurations:
    """
    Clase que contiene las configuraciones del juego.
    """

    _screen_size = (1280,720)
    _game_title = "Juego del gato"
    _background = (20, 30, 50)
    _fps = 8

    _background_image_path = "../media/background_image.png"
    #_markO_image_path = "../media/markO.png"
    #_markX_image_path = "../media/markX.png"
    _turnO_image = "../media/turnO.png"
    _turnX_image = "../media/turnX.png"

    # Posixiones de acuerdo a las teclas.
    _key_to_cell = {
        pygame.K_q: 1, pygame.K_w: 2, pygame.K_e: 3,
        pygame.K_a: 4, pygame.K_s: 5, pygame.K_d: 6,
        pygame.K_z: 7, pygame.K_x: 8, pygame.K_c: 9
    }

    # Posiciones de las marcas en el tablero.
    _cell_positions = {
        1: (500, 330), 2: (640, 330), 3: (780, 330),
        4: (500, 450), 5: (640, 450), 6: (780, 450),
        7: (500, 580), 8: (640, 580), 9: (780, 580),
    }


#---------------------MÉTODOS DE ACCESO
    @classmethod
    def get_screen_size(cls) -> tuple[int, int]:
        return cls._screen_size

    @classmethod
    def get_game_title(cls) -> str:
        return cls._game_title

    @classmethod
    def get_background(cls) -> tuple[int, int, int]:
        return cls._background

    @classmethod
    def get_fps(cls) -> int:
        return cls._fps

    @classmethod
    def get_background_image_path(cls) -> str:
        return cls._background_image_path
#------------------------------------------------------
    @classmethod
    def get_key_to_cell(cls) -> dict:
        """
        Retorna el diccionario que relaciona teclas con casillas del tablero.
        """
        return cls._key_to_cell

    @classmethod
    def get_position(cls, cell: int) -> tuple[int, int]:
        """
        Retorna la posición (x, y) de la casilla en pantalla, según el número de celda.

        :param cell: número de la celda (1 a 9)
        :return: coordenadas (x, y) de la celda
        """
        return cls._cell_positions.get(cell, (0, 0))






