class Configurations:
    """
    Clase que contiene todas las configuraciones del juego.
    """
    # Configuraciones de la pantalla.
    _game_title = "Snake game en pygame"            # Título de la ventana.
    _screen_size = (1280, 720)                      # Resolución de la pantalla (ancho, alto).
    _fps = 8                                        # Número máximo de FPS del videojuego.
    _game_over_screen_time = 5                      # Tiempo de pausa (en seg) para que el jugador note que perdió.

    # Configuraciones de la serpiente.
    _snake_block_size = 80                          # Tamaño del bloque. Es muy recomendable que sea
                                                    # divisor común del largo y ancho de _screen_size.
    _time_to_refresh_head_snake_frames = 300        # Tiempo de animación, en ms, de los frames.

    # Configuraciones de la manzana.
    _apple_block_size = _snake_block_size           # Tamaño del bloque (igual que la el de la serpiente).
    _time_to_refresh_apple_frames = 500             # Tiempo de animación, en ms, de los frames de la manzana.

    # Rutas de las imágenes utilizadas para las clases Background, SnakeBlock y Apple.
    _background_image_path = "../media/background_image.jpg"
    _snake_head_frames_path = ["../media/head1.png", "../media/head2.png", "../media/head3.png",
                               "../media/head4.png", "../media/head5.png", "../media/head6.png",
                               "../media/head7.png", "../media/head8.png"]
    _snake_body_images_path = ["../media/body1.png", "../media/body2.png", "../media/body3.png"]
    _apple_frames_path = ["../media/apple1.png", "../media/apple2.png", "../media/apple3.png", "../media/apple4.png"]

    # Configuraciones de la música del juego.
    _music_volume = 0.25                            # Volúmen de la música de fondo (valor entre 0 y 1).
    _music_fadeout_time = _game_over_screen_time * 1000  # Duración del desvanecimiento de la música (en ms).

    # Rutas de los audios utilizados en la clase Audio.
    _music_path = "../media/music.mp3"
    _start_sound_path = "../media/start_sound.wav"
    _eats_apple_sound_path = "../media/eats_apple_sound.wav"
    _game_over_sound_path = "../media/game_over_sound.wav"

    """NUEVO."""
    # Configuraciones del marcador.
    _scoreboard_font_color = (171, 250, 10)         # Color del texto en formato RGB.
    _scoreboard_typeface = "kimono"                 # Tipo de fuente.
    _scoreboard_font_size = 40                      # Tamaño de la fuente.

    """NUEVO."""
    # Rutas de las imágenes utilizadas para la pantalla del fin del juego de las clases GameOverImage y Credits.
    _game_over_image_path = "../media/game_over_image.png"
    _credits_image_path = "../media/credits_image.png"


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
    def get_game_over_screen_time(cls) -> int:
        """
        Getter para _game_over_screen_time.
        """
        return cls._game_over_screen_time

    @classmethod
    def get_snake_block_size(cls) -> int:
        """
        Getter para _snake_block_size.
        """
        return cls._snake_block_size

    @classmethod
    def get_time_to_refresh_head_snake_frames(cls) -> float:
        """
        Getter para _time_to_refresh_head_snake_frames.
        """
        return cls._time_to_refresh_head_snake_frames

    @classmethod
    def get_apple_block_size(cls) -> int:
        """
        Getter para _apple_block_size.
        """
        return cls._apple_block_size

    @classmethod
    def get_time_to_refresh_apple_frames(cls) -> float:
        """
        Getter para _time_to_refresh_apple_frames.
        """
        return cls._time_to_refresh_apple_frames

    @classmethod
    def get_background_image_path(cls) -> str:
        """
        Getter para _background_image_path.
        """
        return cls._background_image_path

    @classmethod
    def get_snake_head_frames_path(cls) -> list:
        """
        Getter para _snake_head_frames_path.
        """
        return cls._snake_head_frames_path

    @classmethod
    def get_snake_body_images_path(cls) -> list:
        """
        Getter para _snake_body_images_path.
        """
        return cls._snake_body_images_path

    @classmethod
    def get_apple_frames_path(cls) -> list:
        """
        Getter para _apple_frames_path.
        """
        return cls._apple_frames_path

    @classmethod
    def get_music_volume(cls) -> float:
        """
        Getter para _music_volume.
        """
        return cls._music_volume

    @classmethod
    def get_music_fadeout_time(cls) -> int:
        """
        Getter para _music_fadeout_time.
        """
        return cls._music_fadeout_time

    @classmethod
    def get_music_path(cls) -> str:
        """
        Getter para _music_path.
        """
        return cls._music_path

    @classmethod
    def get_start_sound_path(cls) -> str:
        """
        Getter para _start_sound_path.
        """
        return cls._start_sound_path

    @classmethod
    def get_eats_apple_sound_path(cls) -> str:
        """
        Getter para _eats_apple_sound_path.
        """
        return cls._eats_apple_sound_path

    @classmethod
    def get_game_over_sound_path(cls) -> str:
        """
        Getter para _game_over_sound_path.
        """
        return cls._game_over_sound_path

    """NUEVO. Se agregaron los métodos de acceso."""
    @classmethod
    def get_scoreboard_font_color(cls) -> tuple[int,int,int]:
        """
        Getter para _scoreboard_font_color.
        """
        return cls._scoreboard_font_color

    @classmethod
    def get_scoreboard_typeface(cls) -> str:
        """
        Getter para _scoreboard_typeface.
        """
        return cls._scoreboard_typeface

    @classmethod
    def get_scoreboard_font_size(cls) -> int:
        """
        Getter para _scoreboard_font_size.
        """
        return cls._scoreboard_font_size

    @classmethod
    def get_game_over_image_path(cls) -> str:
        """
        Getter para _game_over_image_path.
        """
        return cls._game_over_image_path

    @classmethod
    def get_credits_image_path(cls) -> str:
        """
        Getter para _credits_image_path.
        """
        return cls._credits_image_path