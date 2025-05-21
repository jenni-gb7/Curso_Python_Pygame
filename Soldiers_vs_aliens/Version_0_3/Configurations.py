class Configurations:
    """
    Clase que contiene las configuraciones del juego.
    """
    # Configuraciones de la pantalla.
    _screen_size = (1280,720)           # Resolucion de la pantalla (ancho y largo)
    _game_title = "Solders vs aliens"      # Titulo del juego.
    _background = (20,30,50)            # Fondo de pantalla en formato RGB.
    _fps = 8  # fps del juego

    _soldier_block_size = 45  # Tamaño del bloque de la serpiente
    # Las rutas de los archivos multimedia.
    _background_image_path = "../media/R.jpg"
    _personaje = "../media/OIP.jpg"
    #-------------MÉTODOS DE ACCESO_____________
    @classmethod
    def get_screen_size(cls)-> tuple [int,int]:
        """
        Getter para _screen_size.
        """
        return cls._screen_size

    @classmethod
    def get_game_title(cls)-> str:
        """
        Getter para _screen_size.
        """
        return cls._game_title

    @classmethod
    def get_background(cls)-> tuple [int,int]:
        """
        Getter para _background.
        """

    @classmethod
    def get_fps(cls) -> int:
        """
        Getter para _fps
        :return:
        """
        return cls._fps

    @classmethod
    def get_background_image_path(cls) -> str:
        """
        Getter para _background_image_path.
        """
        return cls._background_image_path

    @classmethod
    def get_soldier_block_size(cls) -> int:
        return cls._soldier_block_size

    @classmethod
    def get_personaje(cls) -> str:
        """
        Getter para _background_image_path.
        """
        return cls._personaje