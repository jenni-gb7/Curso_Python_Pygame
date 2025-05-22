"""
Nombre: Equipo los Bugs
Fecha: 13 de mayo del 2025.

Descripción:

"""

import pygame
from Configurations import Configurations
from Media import Background
from Soldier import Soldiers


def game_event(personaje: Soldiers ) -> bool:
    """
    Función que administra los eventos del juego.
    Recibe al objeto y su clase.
    return: La bandera del fin del juego.
    """

    game_over = False

    #Revisamos todos los eventos generados por el usuario.
    for event in pygame.event.get():
        #Si el usuario cierra la ventana, terminamos el juego.
        if event.type == pygame.QUIT:
            game_over = True
        # El evento es presionar una tecla.
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                personaje.is_moving_up = True
            if event.key == pygame.K_DOWN:
                personaje.is_moving_down = True
        # El evento al soltar una tecla.
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                personaje.is_moving_up = False
            if event.key == pygame.K_DOWN:
                personaje.is_moving_down = False

    return game_over


def screen_refresh(screen: pygame.surface.Surface,
                   clock: pygame.time.Clock, background: Background,
                   personaje: Soldiers) -> None:
    """
    Función que administra los elementos visuales del juego.
    """
    #Dibujamos la imagen de fondo en la pantalla.
    background.blit(screen)
    # Llama a la función de la posici+on del soldado.
    personaje.update_position()
    personaje.blit(screen)

    pygame.display.flip()  #Actualizamos el contenido de la ventana.

    clock.tick(Configurations.get_fps())