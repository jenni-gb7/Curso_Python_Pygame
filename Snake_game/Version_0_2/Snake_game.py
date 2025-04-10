"""
Nombre:
Fecha:
Versión 0.1:
"""


# Se importan los módulos del videojuego.
import pygame
from Configurations import Configurations
from Game_functionalities import game_events, screen_refresh

def run_game() -> None:
    """
    Función principal del videojuego.
    """
    # Se incializa el módulo de pygame.
    pygame.init()

    # Se inicializa la pantalla.
    screen = pygame.display.set_mode(Configurations.get_screen_size())

    # Se configura el título del juego.pip install setuptools
    pygame.display.set_caption(Configurations.get_game_title())

    # Ciclo principal del videojuego.
    game_over = False

    while not game_over:
        # Se verifican los eventos (teclado y ratón) del huego.
        game_over = game_events()

        screen_refresh(screen)

    #Se cierran los recurso de pygame.
    pygame.quit()

if __name__ == '__main__':
    run_game()