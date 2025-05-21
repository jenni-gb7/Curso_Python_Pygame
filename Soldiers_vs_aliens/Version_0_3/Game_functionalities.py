import pygame
from Configurations import Configurations
from Media import Background
from Soldiers_vs_aliens.Version_0_3.Soldier import Soldier


def game_events()-> bool:
    """
    Función que administra los eventos del juego.
    :return: La bandera del fin del juego.
    """
    # Se declara la bandera del fin del juego.
    game_over = False

    # Se verifican los eventos (teclado y ratón) del huego.
    for event in pygame.event.get():
        # Un clic en cerrar el juego.
        if event.type == pygame.QUIT:
            game_over = True

    # Se regresa  la bandera.
    return game_over

def screen_refresh(screen: pygame.surface.Surface,clock: pygame.time.Clock,background: Background, soldier)-> None:
    """
    Función que administra los elementos visuales del juego.
    """
    # Se dibuja el fondo de la pantalla.

    background.blit(screen)

    soldier.draw(screen)

    # Se actualiza la pantalla.
    pygame.display.flip()

    # Se controla la velocidad de FPS
    clock.tick(Configurations.get_fps())