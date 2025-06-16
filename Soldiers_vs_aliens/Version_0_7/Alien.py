import pygame
from pygame.sprite import Sprite
from Configurations import Configurations
from random import choice, uniform


class Alien(Sprite):
    """
    Clase que representa un alienígena enemigo.
    """

    def __init__(self,screen: pygame.surface.Surface):
        super().__init__()

        movement= [True,False]

        # Banderas de movimiento. Inicialmente, el personaje no se mueve.
        self._is_moving_up = choice(movement)
        self._is_moving_down = not self._is_moving_up

        # Cargar hoja de sprites del alien
        self._frames = []
        sheet_path = choice(Configurations.get_alien_sheet_path())
        alien_sheet = pygame.image.load(sheet_path)

        sheet_frames_per_row = Configurations.get_alien_frames_per_row()
        sheet_width = alien_sheet.get_width()
        sheet_height = alien_sheet.get_height()
        frame_width = sheet_width // sheet_frames_per_row
        frame_height = sheet_height
        alien_frame_size = Configurations.get_alien_size()

        for i in range(sheet_frames_per_row):
            x = i * frame_width
            subsurface_rect = (x, 0, frame_width, frame_height)
            frame = alien_sheet.subsurface(subsurface_rect)
            frame = pygame.transform.scale(frame, alien_frame_size)
            self._frames.append(frame)

        self._last_update_time = pygame.time.get_ticks()
        self._frame_index = 0

        self.image = self._frames[self._frame_index]
        self._frame_index = 1

        self.rect = self.image.get_rect()
        screen_rect = screen.get_rect()
        self.rect.right = screen_rect.right
        self.rect.left = screen_rect.left


        self._rect_x = float(self.rect.x)
        self._rect_y = float(self.rect.y)
        self._speed_x = Configurations.get_alien_speed_x()*uniform(8,1)
        self._speed_y = Configurations.get_alien_speed_y()*uniform(6,1)

    def update_position(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para actualizar la posición del soldado de acuerdo a las banderas de movimiento.
        :param screen: Pantalla en donde se verifican los límites.
        """
        # Se obtiene el rectángulo del borde de la pantalla
        screen_rect = screen.get_rect()
        self.rect.x = int(self._rect_x)

        # Se verifican los estados de la bandera para modificar la posición.
        if self._is_moving_up:
            self._rect_y -= self._speed_y

        elif self._is_moving_down:
            self._rect_y += self._speed_y

        # Se verifica que el personaje no sobrepase los bordes de la pantalla.
        if self._rect_y < float(screen_rect.top):
            self._rect_y = float(screen_rect.y)
            self._is_moving_down: True
            self._is_moving_up: False

        elif self._rect_y > (screen_rect.bottom - self.image.get_height()):
            self._rect_y = float(screen_rect.bottom - self.image.get_height())
            self._is_moving_down: False
            self._is_moving_up: True
        # Se actualiza la posición del rectángulo de acuerdo a la posición.
        self.rect.y = int(self._rect_y)

    def update_animation(self):
        # Se verifica si el tiempo transcurrido es mayor o igual al tiempo establecido para actualizar el frame.
        current_time = pygame.time.get_ticks()
        frame_delay = Configurations.get_alien_frame_delay()
        needs_refresh = (current_time - self._last_update_time) >= frame_delay

        if needs_refresh:
            # En caso verdadero, se actualiza el frame por el siguiente en la lista.
            # Además, se actualizan los atributos para resetear el tiempo y actualizar el índice.
            self.image = self._frames[self._frame_index]
            self._last_update_time = current_time
            self._frame_index += 1

            # Finalmente, se verica si el índice ha recorrido todos los frames para volver al inicio de la lista.
            if self._frame_index >= len(self._frames):
                self._frame_index = 0

    def blit(self, screen):
        screen.blit(self.image, self.rect)

        """ %%%%%%%     MÉTODOS DE ACCESO.    %%%%%%%%%%%%%%%%%%%%% """
        @property
        def is_moving_up(self) -> bool:
            """
            Getter para self._is_moving_up.
            """
            return self._is_moving_up

        @is_moving_up.setter
        def is_moving_up(self, value: bool) -> None:
            """
            Setter para self._is_moving_up
            """
            self._is_moving_up = value

        @property
        def is_moving_down(self) -> bool:
            """
            Getter para self._is_moving_down.
            """
            return self._is_moving_down

        @is_moving_down.setter
        def is_moving_down(self, value: bool) -> None:
            """
            Setter para self._is_moving_down
            """
            self._is_moving_down = value