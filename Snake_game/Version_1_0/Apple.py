from asyncio import current_task

import pygame
from pygame.sprite import Sprite
from Configurations import Configurations
from random import randint

class Apple(Sprite):

    """
    Clase que representa una manzana.
    Hereda de la clase Sprite para utilizar grupos de sprites y detectar colisiones entre sprites.
    Sus atributos son: image (apariencia), rect (posición y tamaño) y no_apples (contador).
    Sus métodos son: blit() (dibujar), random_position() (ubicación aleatoria en la pantalla) y el getter del
                     atributo de clases para la puntuación.
    """
    # Atributo de clase para la puntuación.
    _no_apples = 0

    def __init__(self):
        """
        Constructor de la manzana.
        """
        # Se llama al constructor de la clase padre.
        super().__init__()

        # Se incrementa el atributo de clase.
        Apple._no_apples += 1

        self._apple_frames = []
        apple_block_size = Configurations.get_apple_block_size()

        for i in range(len(Configurations.get_apples_images_path())):
            frame = pygame.image.load(Configurations.get_apples_images_path()[i])
            frame = pygame.transform.scale(frame,(apple_block_size,apple_block_size))
            self._apple_frames.append(frame)

        self._last_update_time = pygame.time.get_ticks()

        self._frame_index = 0


        #self.image = pygame.image.load(Configurations.get_apple_images_path()[0])
        #self.image = pygame.transform.scale(self.image,(apple_block_size,apple_block_size))

        # Se obtiene el rectángulo que representa la posición del sprite.

        self.image = self._apple_frames[self._frame_index]
        self._frame_index = 1
        self.rect = self.image.get_rect()


    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para dibujar la manzana en la pantalla.
        :param screen: Pantalla en donde se dibuja el bloque.
        """
        screen.blit(self.image, self.rect)


    def random_position(self,snake_body: pygame.sprite.Group) -> None:
        """
        Se utiliza para inicializar una ubicación aleatoria de la manzana, restringiendo a las ubicaciones
        en donde no se encuentre el cuerpo de la serpiente.
        :param snake_body: Grupo con el cuerpo de la serpiente.
        """
        # Nota: En este ciclo no considera el caso cuando toda la pantalla está ocupada.
        repeat = True
        while repeat:
            # Primero, se genera una posición aleatoria en (x, y) para la manzana.
            screen_width = Configurations.get_screen_size()[0]
            screen_height = Configurations.get_screen_size()[1]
            apple_block_size = Configurations.get_apple_block_size()

            self.rect.x = apple_block_size * randint(0, (screen_width // apple_block_size - 1))
            self.rect.y = apple_block_size* randint(0, (screen_height // apple_block_size - 1))

            # Después, se verifica que no sea la misma que cualquiera del cuerpo de la serpiente.
            # Si alguna se repite, entonces se vuelve a generar la posición aleatoria.
            for snake_block in snake_body.sprites():
                if self.rect == snake_block.rect:
                    repeat = True
                    break
                else:
                    repeat = False

    def animate_apple(self)-> None:
        """
        Se utiliza parta actualizar el frame visible de la manzana
        dando la impresioón de movimiento.
        """
        current_time = pygame.time.get_ticks()
        time_to_refresh = Configurations.get_time_to_refresh()

        needs_refresh = (current_time - self._last_update_time) >= time_to_refresh

        if needs_refresh:
            self.image = self._apple_frames[self._frame_index]

            self._last_update_time = current_time
            self._frame_index += 1
            if self._frame_index >= len(self._apple_frames):
                self._frame_index = 0

    @classmethod
    def get_no_apples(cls) -> int:
        """
        Getter de _no_apples.
        """
        return cls._no_apples