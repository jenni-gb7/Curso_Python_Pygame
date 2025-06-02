import pygame
from pygame.sprite import Sprite
from Configurations import Configurations

class Shot(Sprite):
    def __init__(self,screen: pygame.surface.Surface):
        # Se llama al constructor de la clase padre.
        super().__init__()

        # Lista que almacena los frames del soldado.
        self._frames = []

        """CAMBIO. Ahora se carga la hoja, en lugar de una única imagen."""
        # Se carga la hoja que contiene los frames del soldado.
        sheet_path = Configurations.get_shot_sheet_path()
        shot_sheet = pygame.image.load(sheet_path)

        """NUEVO."""
        # Se obtienen los datos para "recortar" cada sprite de la hoja de sprites.
        sheet_frames_per_row = Configurations.get_frames_per_row()
        sheet_width = shot_sheet.get_width()
        sheet_height = shot_sheet.get_height()
        shot_frame_width = sheet_width // sheet_frames_per_row
        shot_frame_height = sheet_height

        """NUEVO."""
        # Se obtiene el tamaño para escalar cada frame.
        shot_frame_size = Configurations.get_shot_size()

        """NUEVO."""
        # Se recortan los sprites de la hoja, se escalan y se guardan en la lista de sprites.
        for i in range(sheet_frames_per_row):
            x = i * shot_frame_width
            y = 0
            subsurface_rect = (x, y, shot_frame_width, shot_frame_height)
            frame = shot_sheet.subsurface(subsurface_rect)

            frame = pygame.transform.scale(frame, shot_frame_size)

            self._frames.append(frame)

        """NUEVO."""
        # Se incluyen los atributos para la animación.
        self._last_update_time = pygame.time.get_ticks()  # Se relaciona con el tiempo de actualización de cada frame.
        self._frame_index = 0  # Índice de la lista.

        """NUEVO."""
        # Se selecciona la primera imagen a mostrar.
        self.image = self._frames[self._frame_index]
        self._frame_index = 1

        # Se obtiene el rectángulo que representa la posición del sprite.
        self.rect = self.image.get_rect()

        # Se inicializa la posición inicial, en este caso, a la derecha de la pantalla.
        screen_rect = screen.get_rect()
        self.rect.right = screen_rect.right
        self.rect.centery = screen_rect.centery

        """NUEVO."""
        # Se incluyen los atributos para el movimiento.
        self._rect_y = float(self.rect.y)
        self._speed = Configurations.get_shot_speed()


