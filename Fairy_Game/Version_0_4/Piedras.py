import pygame
import random
from pygame.sprite import Sprite

class Piedra(Sprite):
    def __init__(self, x: int, screen: pygame.surface.Surface):
        super().__init__()
        self.screen = screen

        # Dimensiones del rectángulo (puedes ajustar)
        self.width = 80
        self.height = 400

        # Color verde
        self.color = (0, 255, 0)

        # Posición inicial
        self.x = x
        self.gap = 200
        self.y_top = random.randint(-300, -100)  # solo se asigna aquí, al inicio
        self.speed = 3

    def update_position(self):
        self.x -= self.speed

        if self.x < -self.width:
            self.x = 1280 + random.randint(0, 100)
            # No cambiamos y_top aquí para evitar que tiemblen
            # self.y_top = random.randint(-300, -100)  <-- línea eliminada

    def draw(self):
        # Dibuja el rectángulo superior
        rect_top = pygame.Rect(self.x, self.y_top, self.width, self.height)
        pygame.draw.rect(self.screen, self.color, rect_top)

        # Dibuja el rectángulo inferior (abajo separado por el gap)
        rect_bottom = pygame.Rect(self.x, self.y_top + self.height + self.gap, self.width, self.height)
        pygame.draw.rect(self.screen, self.color, rect_bottom)

    def update(self):
        self.update_position()
