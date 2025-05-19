"""
Nombre: Jennifer Marlene Gutiérrez Beteta
Fecha: 18/05/2025
Juego: Gato
Versión: 0.1
"""

import pygame
from pygame.sprite import Group

from Configurations import Configurations
from Game_functionalities import screen_refresh, game_events, check_winner, game_over_screen
from Media import Background, TurnImage

def run_game() -> None:
    """
    Función principal del videojuego del Gato.
    Inicializa Pygame, configura la pantalla, carga los recursos y ejecuta el bucle principal.
    """
    # Inicializar Pygame
    pygame.init()

    # Configurar pantalla
    screen = pygame.display.set_mode(Configurations.get_screen_size())
    pygame.display.set_caption(Configurations.get_game_title())

    # Crear reloj
    clock = pygame.time.Clock()

    # Instanciar fondo e imagen de turno
    background = Background()
    turn_image = TurnImage()

    # Grupo de sprites para las marcas del tablero
    marks = Group()

    # Estado del juego
    game_over = False
    result = ""

    # Bucle principal
    while not game_over:
        # Manejo de eventos y colocación de marcas
        game_over = game_events(marks, turn_image)

        # Dibujar elementos en pantalla
        screen_refresh(screen, clock, background, marks, turn_image)

        # Verificar si hay ganador o empate
        winner_flag,result = check_winner(marks)


        # Mostrar pantalla de resultado si el juego terminó
        if winner_flag:
            game_over_screen(screen, clock, background, marks, turn_image, result)
            game_over = True
    # Salir del juego
    pygame.quit()

if __name__ == '__main__':
    run_game()
