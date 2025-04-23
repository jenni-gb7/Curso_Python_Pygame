class Configurations:
    """
    Clase que contiene todas las configuraciones del juego.
    """
    # Configuraciones de la pantalla.
    _game_title = "Snake game en pygame"            # Título de la ventana.
    _screen_size = (1280, 720)                      # Resolución de la pantalla (ancho, alto).
    _background = (234, 137, 154)                      # Fondo de la pantalla en formato RGB.
    _fps = 8                                        # Número máximo de FPS del videojuego.

    # Configuraciones de la serpiente.
    _snake_block_size = 80                          # Tamaño del bloque. Es muy recomendable que sea
                                                    # divisor común del largo y ancho de _screen_size.
    _snake_head_color = (255, 255, 255)             # Color de la cabeza de la serpiente.
    _snake_body_color = (0, 255, 0)                 # Color del cuerpo de la serpiente.

    """NUEVO."""
    # Configuraciones de la manzana.
    _apple_block_size = _snake_block_size           # Tamaño del bloque (igual que la el de la serpiente).
    _apple_color = (255, 0, 0)                      # Color de la manzana.


    @classmethod
    def get_game_title(cls) -> str:
        """
        Getter para _game_title.
        """
        return cls._game_title

    @classmethod
    def get_screen_size(cls) -> tuple[int, int]:
        """
        Getter para _screen_size.
        """
        return cls._screen_size

    @classmethod
    def get_background(cls) -> tuple[int, int, int]:
        """
        Getter para _background.
        """
        return cls._background

    @classmethod
    def get_fps(cls) -> int:
        """
        Getter para _fps.
        """
        return cls._fps

    @classmethod
    def get_snake_block_size(cls) -> int:
        """
        Getter para _snake_block_size.
        """
        return cls._snake_block_size

    @classmethod
    def get_snake_head_color(cls) -> tuple[int, int, int]:
        """
        Getter para _snake_head_color.
        """
        return cls._snake_head_color

    @classmethod
    def get_snake_body_color(cls) -> tuple[int, int, int]:
        """
        Getter para _snake_body_color.
        """
        return cls._snake_body_color

    """NUEVO."""
    @classmethod
    def get_apple_block_size(cls) -> int:
        """
        Getter para _apple_block_size.
        """
        return cls._apple_block_size

    @classmethod
    def get_apple_color(cls) -> tuple[int, int, int]:
        """
        Getter para _snake_body_color.
        """
        return cls._apple_color