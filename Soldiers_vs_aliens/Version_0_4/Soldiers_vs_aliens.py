"""
Nombre: Alberto Martínez Barbosa.
Fecha:
Versión 0.4:

"""

# Se importan los módulos necesarios.
import pygame
from Configurations import Configurations
from Game_functionalities import game_events, screen_refresh
from Media import Background
from Soldier import Soldier


def run_game() -> None:
    """
    Función principal del videojuego.
    """
    # Se inicializa el módulo de pygame y se realizan las configuraciones iniciales.
    pygame.init()
    screen_size = Configurations.get_screen_size()
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()  # Se usa para controlar la velocidad de fotogramas (FPS).

    # Se configura el título de la ventana.
    game_title = Configurations.get_game_title()
    pygame.display.set_caption(game_title)

    # Se crea el objeto del fondo de pantalla.
    background = Background()

    # Se crea el objeto del soldado (personaje principal).
    soldier = Soldier(screen)

    # Ciclo principal del videojuego.
    game_over = False
    while not game_over:
        """CAMBIO. Ahora recibe el objeto del soldado."""
        # Función que administra los eventos del juego.
        game_over = game_events(soldier)

        # Función que administra los elementos de la pantalla.
        screen_refresh(screen, clock, background, soldier)

    # Cierra todos los recursos del módulo pygame.
    pygame.quit()



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == "__main__":
    run_game()