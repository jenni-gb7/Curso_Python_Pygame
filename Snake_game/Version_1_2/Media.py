import pygame
from Configurations import Configurations

""" %%%%%%%     Clase.    %%%%%%%%%%%%%%%%%%%%% """
class Background:
    """
    Clase que contiene el fondo de pantalla.
    Sus atributos son: image (apariencia) y rect (posición y tamaño).
    Sus métodos son: blit() (dibujar).
    """
    def __init__(self):
        # Se carga la imagen del fondo de pantalla.
        self.image = pygame.image.load(Configurations.get_background_image_path())

        # Se escala la imagen al tamaño de la pantalla.
        screen_size = Configurations.get_screen_size()
        self.image = pygame.transform.scale(self.image, screen_size)

        # Se obtiene el rectángulo que representa la posición del sprite.
        self.rect = self.image.get_rect()


    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para dibujar el fondo de pantalla en la pantalla.
        :param screen: Pantalla en donde se dibuja el fondo de pantalla.
        """
        screen.blit(self.image, self.rect)


""" %%%%%%%     Clase.    %%%%%%%%%%%%%%%%%%%%% """
class Audio:
    """
    Clase que contiene el audio del videojuego, incluyendo la música y los efectos de sonido.
    Sus atributos son: la música y los sonidos.
    Sus métodos son: para reproducir y controlar la música, así como los que reproducen los sonidos.
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
        pygame.mixer.music.play(loops=-1)   # Un -1 indica que la música se reproduce en bucle.
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



""" %%%%%%%     Clase.    %%%%%%%%%%%%%%%%%%%%% """
class Scoreboard:
    """
    Clase que contiene el marcador.
    Sus atributos son: la fuente (tipo, tamaño y color) del texto, image (apariencia) y rect (posición y tamaño).
    Sus métodos son: update_score() (actualizar los puntos del marcador) y blit() (dibujar).
    """
    def __init__(self):
        # Se obtienen las configuraciones del marcador.
        self._typeface = Configurations.get_scoreboard_typeface()
        self._font_size = Configurations.get_scoreboard_font_size()
        self._font_color = Configurations.get_scoreboard_font_color()

        # Se agrega una imagen con un score inicial de 0 puntos.
        self._font = pygame.font.SysFont(self._typeface, self._font_size)
        self.image = self._font.render("Puntos: 0", True, self._font_color)

        # Se obtiene el rectángulo que representa la posición del sprite.
        self.rect = self.image.get_rect()

        # Se ajusta la posición del marcador, dejando un 5 % del tamaño de la pantalla.
        self.rect.x = Configurations.get_screen_size()[0]* 0.05
        self.rect.y = Configurations.get_screen_size()[1]* 0.05


    def update(self, new_score: int) -> None:
        """
        Se utiliza para actualizar el marcador.
        :param new_score: Puntos que se van a mostrar en el marcador.
        """
        text = "Puntos: " + str(new_score)
        self.image = self._font.render(text, True, self._font_color)


    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para dibujar el marcador en la pantalla.
        :param screen: Pantalla en donde se dibuja el fondo de pantalla.
        """
        screen.blit(self.image, self.rect)


"""NUEVO."""
""" %%%%%%%     Clase.    %%%%%%%%%%%%%%%%%%%%% """
class GameOverImage:
    """
    Clase que contiene la imagen del game over.
    Sus atributos son: image (apariencia) y rect (posición y tamaño).
    Sus métodos son: blit() (dibujar).
    """
    def __init__(self):
        # Se carga la imagen del fondo de pantalla.
        self.image = pygame.image.load(Configurations.get_game_over_image_path())

        # Se obtiene el rectángulo que representa la posición del sprite.
        self.rect = self.image.get_rect()


    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para dibujar la imagen de game over en la pantalla.
        :param screen: Pantalla en donde se dibuja el fondo de pantalla.
        """
        # Se centra la imagen en la pantalla.
        self.rect.centerx = screen.get_rect().centerx
        self.rect.y = Configurations.get_snake_block_size()

        screen.blit(self.image, self.rect)


"""NUEVO."""
""" %%%%%%%     Clase.    %%%%%%%%%%%%%%%%%%%%% """
class Credits:
    """
    Clase que contiene la imagen de los créditos.
    Sus atributos son: image (apariencia) y rect (posición y tamaño).
    Sus métodos son: blit() (dibujar).
    """
    def __init__(self):
        # Se carga la imagen del fondo de pantalla.
        self.image = pygame.image.load(Configurations.get_credits_image_path())

        # Se obtiene el rectángulo que representa la posición del sprite.
        self.rect = self.image.get_rect()


    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para dibujar la imagen de game over en la pantalla.
        :param screen: Pantalla en donde se dibuja el fondo de pantalla.
        """
        # Se centra la imagen en la pantalla.
        self.rect.centerx = screen.get_rect().centerx
        self.rect.bottom = screen.get_rect().bottom - Configurations.get_snake_block_size()

        screen.blit(self.image, self.rect)