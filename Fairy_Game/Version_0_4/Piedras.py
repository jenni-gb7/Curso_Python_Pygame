import pygame
import random
from pygame.sprite import Sprite

class Piedra(Sprite):
    def __init__(self, x: int, screen: pygame.surface.Surface):
        super().__init__()

        # Cargar la hoja de sprites
        self.sheet = pygame.image.load("../media/piedras.png").convert_alpha()

        # Datos de la hoja de sprites
        self.sheet_columns = 3
        self.sprite_width = self.sheet.get_width() // self.sheet_columns
        self.sprite_height = self.sheet.get_height()

        # Escalado deseado
        self.scaled_width = 80
        self.scaled_height = 400

        # Lista de frames (una piedra normal y una invertida)
        self.frames = []
        for i in range(self.sheet_columns):
            rect = pygame.Rect(i * self.sprite_width, 0, self.sprite_width, self.sprite_height)
            image = self.sheet.subsurface(rect)
            image = pygame.transform.scale(image, (self.scaled_width, self.scaled_height))
            self.frames.append(image)

        # Elegir un frame aleatorio
        self._frame_index = random.randint(0, self.sheet_columns - 1)
        self.image = self.frames[self._frame_index]
        self.image_top = pygame.transform.flip(self.image, False, True)

        # Rectángulo de posición
        self.rect = self.image.get_rect()
        self.x = x
        self.gap = 200
        self.y_top = random.randint(-300, -100)
        self.speed = 3

        # Para calcular posición
        self.screen = screen
        self._rect_y = float(self.y_top)

    def update_position(self):
        self.x -= self.speed

        if self.x < -self.scaled_width:
            self.x = 1280 + random.randint(0, 100)
            self.y_top = random.randint(-300, -100)
            self._frame_index = random.randint(0, len(self.frames) - 1)
            self.image = self.frames[self._frame_index]
            self.image_top = pygame.transform.flip(self.image, False, True)

    def blit(self, screen: pygame.surface.Surface):
        screen.blit(self.image_top, (self.x, self.y_top))
        screen.blit(self.image, (self.x, self.y_top + self.image.get_height() + self.gap))
