import pygame
from pygame.sprite import Sprite
from Configurations import Configurations
from random import randint,choice

class SnakeBlock(Sprite):
    """
    Clase que representa un bloque del cuerpo de la serpiente.
    Hereda de la clase Sprite para utilizar grupos de sprites y detectar colisiones entre sprites.
    Sus atributos son: image (apariencia) y rect (posición y tamaño), banderas de movimiento.
    Sus métodos son: blit() (dibujar), snake_head_init() (inicializa en una posición aleatoria), getter y
                     setter de las banderas de movimiento.
    """
    # Atributos de clase (banderas de movimiento de la serpiente).
    _is_moving_right = False
    _is_moving_left = False
    _is_moving_up = False
    _is_moving_down = False


    def __init__(self, is_head: bool = False):
        """
        Constructor de la serpiente, en donde se llama al constructor padre de Sprite.
        :param is_head: Indica si el bloque es o no la cabeza de la serpiente.
        """
        # Se llama al constructor de la clase padre.
        super().__init__()

        # Se selecciona el color dependiendo de si es o no la cabeza de la serpiente.
        if is_head:
            color = Configurations.get_snake_head_color()
            self.image = pygame.image.load(Configurations.get_snake_head_image_path())
        else:
            #color = Configurations.get_snake_body_color()
            body_images_path = Configurations.get_snake_body_images_path()
            path = choice(body_images_path)
            self.image = pygame.image.load(path)


        snake_block_size = Configurations.get_snake_block_size()

        # Se crea una imagen para el sprite (superficie cuadrada del tamaño del bloque de la serpiente),
        # rellenándola con el color correspondiente a si es la parte de la cabeza o del cuerpo.
        #self.image = pygame.Surface((Configurations.get_snake_block_size(), Configurations.get_snake_block_size()))
        #self.image.fill(color)
        self.image = pygame.transform.scale(self.image,(snake_block_size,snake_block_size))

        # Se obtiene el rectángulo que representa la posición del sprite.
        self.rect = self.image.get_rect()


    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para dibujar el bloque de la serpiente en la pantalla.
        :param screen: Pantalla en donde se dibuja el bloque.
        """
        angle = 0
        if SnakeBlock.get_is_moving_up():
            angle = 90
        elif SnakeBlock.get_is_moving_left():
            angle = 180
        elif SnakeBlock.get_is_moving_down():
            angle = 270

        image_flip = pygame.transform.rotate(self.image,angle)
        screen.blit(image_flip, self.rect)


    def snake_head_init(self) -> None:
        """
        Se utiliza para inicializar una ubicación aleatoria de la cabeza de la serpiente.
        """
        screen_width = Configurations.get_screen_size()[0]
        screen_height = Configurations.get_screen_size()[1]
        snake_block_size = Configurations.get_snake_block_size()
        self.rect.x = snake_block_size * randint(0, (screen_width // snake_block_size - 1))
        self.rect.y = snake_block_size * randint(0, (screen_height // snake_block_size - 1))


    @classmethod
    def get_is_moving_right(cls) -> bool:
        """
        Getter para la bandera _is_moving_right.
        """
        return cls._is_moving_right


    @classmethod
    def set_is_moving_right(cls, value: bool) -> None:
        """
        Setter para la bandera _is_moving_right.
        """
        cls._is_moving_right = value


    @classmethod
    def get_is_moving_left(cls) -> bool:
        """
        Getter para la bandera _is_moving_left.
        """
        return cls._is_moving_left


    @classmethod
    def set_is_moving_left(cls, value: bool) -> None:
        """
        Setter para la bandera _is_moving_left.
        """
        cls._is_moving_left = value


    @classmethod
    def get_is_moving_up(cls) -> bool:
        """
        Getter para la bandera _is_moving_up.
        """
        return cls._is_moving_up


    @classmethod
    def set_is_moving_up(cls, value: bool) -> None:
        """
        Setter para la bandera _is_moving_up.
        """
        cls._is_moving_up = value


    @classmethod
    def get_is_moving_down(cls) -> bool:
        """
        Getter para la bandera _is_moving_down.
        """
        return cls._is_moving_down


    @classmethod
    def set_is_moving_down(cls, value: bool) -> None:
        """
        Setter para la bandera _is_moving_down.
        """
        cls._is_moving_down = value
