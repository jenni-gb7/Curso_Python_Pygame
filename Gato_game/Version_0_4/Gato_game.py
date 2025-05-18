"""
Nombre: Jennifer Marlene Gutiérrez Beteta
Fecha: [Agrega la fecha aquí]
Juego: Gato
Versión: 0.1
"""

import pygame
from pygame.sprite import Group
from Configurations import Configurations
from Game_functionalities import screen_refresh, game_events
from Media import Background

def run_game() -> None:
    """
    Función principal del videojuego del gato.
    """
    pygame.init()

    screen = pygame.display.set_mode(Configurations.get_screen_size())
    pygame.display.set_caption(Configurations.get_game_title())
    clock = pygame.time.Clock()

    background = Background()
    marks = Group()

    game_over = False
    while not game_over:
        game_over = game_events(marks)
        screen_refresh(screen, clock, background, marks)

    pygame.quit()

if __name__ == '__main__':
    run_game()
