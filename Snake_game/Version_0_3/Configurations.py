class Configurations:
    """
    Clase que contine todas las configuraciones del juego
    """
    #Configuraciones de la pantala
    _screen_size = (1280, 720)
    _game_title = "Snake game en pygame"
    _background = (234, 137, 154)
    _fps = 8 #fps del juego

    #Configuraciones de la serpiente
    #Que sea un divisor común con eñ screen size ⬇️
    _snake_block_size = 45 #Tamaño del bloque de la serpiente
    _snake_head_color = (255, 233, 34)
    _snake_body_color = (0, 255, 0)

    @classmethod
    def get_screen_size(cls) -> tuple[int, int]:
        """
        Getter para screen_size
        """
        return cls._screen_size

    @classmethod
    def get_game_title(cls) -> str:
        """
        Getter para get_game_title
        """
        return cls._game_title

    @classmethod
    def get_background(cls) -> tuple[int,int, int]:
        return cls._background

    @classmethod
    def get_fps(cls) -> int:
        """
        Getter para _fps
        :return:
        """
        return cls._fps
    @classmethod
    def get_snake_block_size(cls) -> int:
        return cls._snake_block_size

    @classmethod
    def get_snake_head_color(cls) -> tuple[int, int, int]:
        return cls._snake_head_color

    @classmethod
    def get_snake_body_color(cls) -> tuple[int, int, int]:
        return cls._snake_body_color