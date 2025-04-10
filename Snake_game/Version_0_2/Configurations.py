class Configurations:
    """
    Clase que contiene todas las configuraciones del juego.
    """
    # Configuraciones de la pantalla.
    _screen_size = (1280, 720)               # Resolución de la pantalla (ancho, alto).
    _game_title = "Snake game en pygame"     #   Título del juego.
    _background = (20, 30, 50)               # Fondo de pantalla en formato RGB.

    @classmethod
    def get_screen_size(cls) -> tuple[int, int]:
        """
        Getter para _screen_size.
        """
        return cls._screen_size

    @classmethod
    def get_game_title(cls) -> str:
        """
        Getter para game_title.
        """
        return cls._game_title

    @classmethod
    def get_background(cls) ->tuple[int, int,int]:
        """
        Getter para _background.
        """
        return cls._background