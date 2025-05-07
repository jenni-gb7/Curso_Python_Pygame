import pygame
from Configurations import Configurations

#-----------------------CLASE---------------
class Background:
    """
    Clase que contiene el fondo de pantalla.
    """

    def __init__(self):
        background_image_path = Configurations.get_background_image_path()
        self.image = pygame.image.load(background_image_path)

        # Se escala la imagen al tamaño de pantalla.
        screen_size = Configurations.get_screen_size()
        self.image = pygame.transform.scale(self.image,screen_size)

        self.rect = self.image.get_rect()


    def blit(self,screen: pygame.surface.Surface):
        """
        Se utiliza para dibujar el fondo de pantalla.
        """
        screen.blit(self.image, self.rect)

#------------------CLASE--------------------------
class Audio:
    """
    Clase que contiene la música del videojuego
    """

    def __init__(self):
        # Se carga la música del videojuego.
        pygame.mixer.music.load(Configurations.get_music_path())

        # Se carga el sonido de inicio.
        self._start_sound = pygame.mixer.Sound(Configurations.get_start_sound_path())

        # Se carga el sonido cuando la serpiente come una manzana.
        self._eats_apple_sound = pygame.mixer.Sound(Configurations.get_eats_apple_sound_path())

        # Se carga el sonido cuando el jugador ha perdido.
        self._game_over_sound = pygame.mixer.Sound(Configurations.get_game_over_sound_path())

    @classmethod
    def play_music(cls, volume) -> None:
        """
        Se utiliza para reproducir la música en bucle.
        """
        pygame.mixer.music.play(loops=-1)  # Un -1 indica que la música se reproduce en bucle.
        pygame.mixer.music.set_volume(volume)

    @classmethod
    def music_fadeout(cls, time) -> None:
        """
        Se utiliza para realizar un desvanecimiento de la música del juego hasta parar.
        :param time: Tiempo de desvanecimiento de la música (en ms).
        """
        pygame.mixer.music.fadeout(time)

    def play_star_sound(self) -> None:
        """
        Se utiliza para reproducir el sonido de inicio del juego.
        """
        self._start_sound.play()

    def play_eats_apple_sound(self) -> None:
        """
        Se utiliza para reproducir el sonido cuando la serpiente come la manzana.
        """
        self._eats_apple_sound.play()

    def play_game_over_sound(self) -> None:
        """
        Se utiliza para reproducir el sonido cuando el jugador ha perdido.
        """
        self._game_over_sound.play()