"""
Nombre:
Fecha:
Versión 0.1:
"""


# Se importan los módulos del videojuego.
import pygame

def runn_game() -> None:
    """
    Función principal del videojuego.
    """
    # Se incializa el módulo de pygame.
    pygame.init()

    # Se inicializa la pantalla.
    screen_size = (1280,720)    # Resolución de la pantalla (ancho, alto).
    screen = pygame.display.set_mode(screen_size)

    # Se configura el título del juego.
    game_title = "Snake game en pygame"
    pygame.display.set_caption(game_title)

    # Ciclo principal del videojuego.
    game_over = False

    while not game_over:
        # Se verifican los eventos (teclado y ratón) del huego.
        for event in pygame.event.get():
            # Un clic en cerrar el juego.
            if event.type == pygame.QUIT:
                game_over = True

        # Se dibujan los elementos gráficos en la pantalla.
        background = (20,30,50)     # Fondo de pantalla en formato RGB.
        screen.fill(background)

        # Se actualiza la pantalla.
        pygame.display.flip()

    #Se cierran los recurso de pygame.
    pygame.quit()

if __name__ == '__main__':
    runn_game()