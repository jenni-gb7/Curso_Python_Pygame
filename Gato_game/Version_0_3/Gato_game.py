"""
Nombre: jennifer Marlene  Gutierrez Beteta
Fecha:
Juego gato
Versión 0.1
"""

# Se importan los módulos del videojuego.
import pygame
from Game_functionalities import screen_refresh
from Media import Background


def run_game() -> None:
    """
    Función principal del videojuego.
    """
    # Se incializa el módulo de pygame.
    pygame.init()

    # Se inicializa la pantalla.
    screen_size = (1280,720)    # Resolución de la pantalla (ancho, alto).
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()  # Se usa para controlar la velocidad de fotogramas (FPS).

    # Se configura el título del juego.
    game_title = "Juego del gato"
    pygame.display.set_caption(game_title)

    # Se crea el objeto con el fondo del videojuego.
    background = Background()

    # Ciclo principal del videojuego.
    game_over = False

    while not game_over:
        # Se verifican los eventos (teclado y ratón) del huego.
        for event in pygame.event.get():
            # Un clic en cerrar el juego.
            if event.type == pygame.QUIT:
                game_over = True

                # Función que administra los elementos de la pantalla.
        screen_refresh(screen, clock,background)
        pygame.display.flip()

    #Se cierran los recurso de pygame.
    pygame.quit()

if __name__ == '__main__':
    run_game()