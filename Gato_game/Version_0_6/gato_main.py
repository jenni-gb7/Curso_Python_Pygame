"""
Nombre: Jennifer Marlene Gutiérrez Beteta
Fecha: 18/05/2025
Juego: Gato
Versión: 0.1
"""

import pygame
from pygame.sprite import Group
from Configurations import Configurations
from Game_functionalities import screen_refresh, game_events,check_winner,game_over_screen
from media import Background,TurnImage

def run_game() -> None:
    """
    Función principal del videojuego del gato.
    """
    pygame.init()

    screen = pygame.display.set_mode(Configurations.get_screen_size())
    pygame.display.set_caption(Configurations.get_game_title())
    clock = pygame.time.Clock()

    #Imagen de fondo
    background = Background()
    #imagen de turno.
    turn_image=TurnImage()
    #Grupo para las marcas
    marks = Group()

    game_over = False
    resultado= " "
    while not game_over:
        #procesa eventos teclado y ratom
        game_over = game_events(marks, turn_image)
        #dibuja los elementos
        screen_refresh(screen, clock, background, marks, turn_image)

        winner_flag,resultado=check_winner(marks)
        if winner_flag:
            game_over_screen(screen, clock, background, marks, turn_image, resultado)
            game_over=True
    pygame.quit()

if __name__ == '__main__':
    run_game()