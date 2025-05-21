class Configurations:
    """
    Clase que contiene las configuraciones del juego.
    """
    # Configuraciones de la pantalla.
    _screen_size = (1280,720)           # Resolucion de la pantalla (ancho y largo)
    _game_title = "Juego del gato"      # Titulo del juego.
    _background = (20,30,50)            # Fondo de pantalla en formato RGB.


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
