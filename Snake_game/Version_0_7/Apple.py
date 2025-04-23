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

        # Se crea una imagen para el sprite (superficie cuadrada del tamaño del bloque de la manzana),
        # rellenándola con el color correspondiente dado en las configuraciones.
        self.image = pygame.Surface((Configurations.get_apple_block_size(), Configurations.get_apple_block_size()))
        self.image.fill(Configurations.get_apple_color())

        # Se obtiene el rectángulo que representa la posición del sprite.
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


    @classmethod
    def get_no_apples(cls) -> int:
        """
        Getter de _no_apples.
        """
        return cls._no_apples