class Configurations:
    """
    Clase que contiene todas las configuraciones del juego.
    """
    # Configuraciones de la pantalla.
    _game_title = "Snake game en pygame"            # Título de la ventana.
    _screen_size = (1280, 720)                      # Resolución de la pantalla (ancho, alto).
    #_background = (234, 137, 154)                      # Fondo de la pantalla en formato RGB.
    _fps = 8                                        # Número máximo de FPS del videojuego.
    _game_over_screen_time =  1

    # Configuraciones de la serpiente.
    _snake_block_size = 80                          # Tamaño del bloque. Es muy recomendable que sea
                                                    # divisor común del largo y ancho de _screen_size.
    _snake_head_color = (255, 255, 255)             # Color de la cabeza de la serpiente.
    _snake_body_color = (0, 255, 0)                 # Color del cuerpo de la serpiente.

    """NUEVO."""
    # Configuraciones de la manzana.
    _apple_block_size = _snake_block_size           # Tamaño del bloque (igual que la el de la serpiente).
    _apple_color = (255, 0, 0)                      # Color de la manzana.

    # Las rutas de los archivos multimedia.
    _background_image_path = "../media/background_image.jpg"
    _apple_images_path = ["../media/apple1.png", "../media/apple2.png", "../media/apple3.png", "../media/apple4.png"]
    _snake_head_image_path = "../media/head1.png"
    _snake_body_images_path = ["../media/body1.png","../media/body2.png","../media/body3.png"]

    # Tiempo de animación para el cambio de imagen.
    _time_to_refresh = 200

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
    def get_snake_head_color(cls) ->  tuple[int, int, int]:
        """
        Getter para _snake_head_color.
        """
        return cls._snake_head_color

    @classmethod
    def get_game_over_screen_time(cls) -> int:
        """
        Getter para _game_over_screen_time
        """
        return cls._game_over_screen_time

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

    @classmethod
    def get_background_image_path(cls) -> str:
        """
        Getter para _background_image_path.
        """
        return cls._background_image_path

    @classmethod
    def get_apples_images_path(cls) -> list:
        """
        Getter para _apple_images_path.
        """
        return cls._apple_images_path

    @classmethod
    def get_snake_head_image_path(cls) -> str:
        """
        Getter _snake_head_image_path.
        """
        return cls._snake_head_image_path

    @classmethod
    def get_snake_body_images_path(cls) -> list:
        """
        Getter _snake_body_image_path.
        """
        return cls._snake_body_images_path

    @classmethod
    def get_time_to_refresh(cls) -> int:
        """
        Getter _time_to_refresh.
        """
        return cls._time_to_refresh