import pygame
from pygame.sprite import Sprite
from Configurations import Configurations
from random import choice

class Alien(Sprite):
    """
    Clase que representa un alienígena enemigo.
    """

    def __init__(self,screen):
        super().__init__()

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
        self._speed = Configurations.get_alien_speed()

    def update_position(self) -> None:
        """
        Se utiliza para actualizar la posición del soldado de acuerdo a las banderas de movimiento.
        """
        # Se actualiza la posición del valor flotante de la posición.
        self._rect_x += self._speed

        # Se actualiza la posición del rectángulo de acuerdo a la posición.
        self.rect.x = int(self._rect_x)

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
