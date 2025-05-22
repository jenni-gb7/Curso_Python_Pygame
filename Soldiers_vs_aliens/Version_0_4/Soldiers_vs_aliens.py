"""
Nombre: Equipo los Bugs.
Fecha: 13 de mayo del 2025.

Descripción:
"""
import pygame
from Configurations import Configurations
from Game_functionalities import game_event, screen_refresh
from Media import Background
from Soldier import Soldiers


def run_game() -> None:
    """
    Función principal del videojuego.
    """
    # Inicialización de pygame.
    pygame.init()

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode(Configurations.get_screen_size())

    pygame.display.set_caption(Configurations.get_game_title())

    game_over = False
    background = Background()
    personaje = Soldiers(screen)

    while not game_over:
        game_over = game_event(personaje)  # Verificación del cierre del juego.
        screen_refresh(screen, clock, background, personaje)  #Actualizamos la pantalla.


if __name__ == '__main__':
    run_game()