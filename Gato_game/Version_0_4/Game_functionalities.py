import pygame
from Configurations import Configurations
from Media import Background
from TikTacToe import TicTacToeMark

def game_events(marks_group)-> bool:
    """
    Función que administra los eventos del juego.
    :return: La bandera del fin del juego.
    """
    # Se declara la bandera del fin del juego.
    game_over = False
    key_map = Configurations.get_key_to_cell()
    # Se verifican los eventos (teclado y ratón) del huego.
    for event in pygame.event.get():
        # Un clic en cerrar el juego.
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            cell = key_map.get(event.key)
            if cell:
                mark = TicTacToeMark(cell)
                marks_group.add(mark)

    # Se regresa  la bandera.
    return game_over

def screen_refresh(screen: pygame.surface.Surface,clock: pygame.time.Clock,background: Background,marks_group)-> None:
    """
    Función que administra los elementos visuales del juego.
    """
    # Se dibuja el fondo de la pantalla.

    background.blit(screen)
    # Se dibujan las marcas
    marks_group.draw(screen)

    # Se actualiza la pantalla.
    pygame.display.flip()

    # Se controla la velocidad de FPS
    clock.tick(Configurations.get_fps())
