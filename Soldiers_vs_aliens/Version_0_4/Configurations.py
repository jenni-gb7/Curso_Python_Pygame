class Configurations:
    """
    Clase que contiene todas las configuraciones del juego.
    """
    # Configuraciones de la pantalla.
    _game_title = "Soldados vs aliens"              # Título de la ventana.
    _screen_size = (1280, 720)                      # Resolución de la pantalla (ancho, alto).
    _fps = 30                                       # Número máximo de FPS del videojuego.

    # Configuraciones del soldado.
    _soldier_size = (142, 76)                       # Escala del soldado (ancho, alto).
    """NUEVO."""
    _frames_per_row = 4                             # Número de frames que contiene cada fila de la hoja de frames.
    _soldier_frame_delay = 300                      # Tiempo de cada frame del personaje (en ms).
    _soldier_speed = 12.5                           # Velocidad (en píxeles) del personaje.

    """CAMBIO. La propiedad _soldier_image_path se modificó por _soldier_sheet_path, que contiene los frames.
               Además, se cambió la ruta de la imagen png."""
    # Rutas de las imágenes utilizadas.
    _background_image_path = "../media/background_image.jpg"
    _soldier_sheet_path = "../media/soldier-idle-sheet.png"


    """ %%%%%%%     MÉTODOS DE ACCESO.    %%%%%%%%%%%%%%%%%%%%% """
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
    def get_soldier_size(cls) -> tuple[int, int]:
        """
        Getter para _soldier_size.
        """
        return cls._soldier_size

    """NUEVO."""
    @classmethod
    def get_frames_per_row(cls) -> int:
        """
        Getter para _soldier_frames_per_row.
        """
        return cls._frames_per_row

    """NUEVO."""
    @classmethod
    def get_soldier_frame_delay(cls) -> int:
        """
        Getter para _soldier_frame_delay.
        """
        return cls._soldier_frame_delay

    """NUEVO."""
    @classmethod
    def get_soldier_speed(cls) -> float:
        """
        Getter para _soldier_speed.
        """
        return cls._soldier_speed

    @classmethod
    def get_background_image_path(cls) -> str:
        """
        Getter para _background_image_path.
        """
        return cls._background_image_path

    """CAMBIO. El método de acceso cambió de acuerdo al cambio del parámetro utilizado."""
    @classmethod
    def get_soldier_sheet_path(cls) -> str:
        """
        Getter para _soldier_sheet_path.
        """
        return cls._soldier_sheet_path