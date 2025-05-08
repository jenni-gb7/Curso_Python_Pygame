"""
Nombre: Jennifer Marlene Gutiérrez Beteta.
Fecha: 08/04/2025
Versión 0.6:
- Se añadió que, con la tecla 'espacio', se agrega un objeto de la clase SnakeBlock al cuerpo de la serpiente.
  * Esto se realizó en la función game_events().
  * Este evento se va a reemplazar más adelante por la 'manzana' de la serpiente.
- Se modificó la función snake_movement() para que considere el movimiento de toda la serpiente, considerando que
  los bloques tienen que ocupar la posición del bloque previo, por ejemplo:
  * posición del bloque[3] ➡️ tiene que ubicarse en la posición del bloque[2],
  * posición del bloque[2] ➡️ tiene que ubicarse en la posición del bloque[1],
  * posición del bloque[1] ➡️ tiene que ubicarse en la posición del bloque[0],
  * posición del bloque[0] (cabeza) ➡️ moverse de acuerdo a la bandera.
"""
# Se importan los módulos necesarios.
import pygame
from Configurations import Configurations
from Game_functionalities import game_events, screen_refresh, snake_movement,check_colision, game_over_screen
from Snake import SnakeBlock
from pygame.sprite import Group
from Media import Background,Audio,Scoreboard,GameOverImage


"""NUEVO."""
from Apple import Apple


def run_game() -> None:
    """
    Función principal del videojuego.
    """
    # Se inicializa el módulo de pygame y se realizan las configuraciones iniciales.
    pygame.init()
    screen = pygame.display.set_mode(Configurations.get_screen_size())  # Resolución de la pantalla (ancho, alto).
    pygame.display.set_caption(Configurations.get_game_title())         # Se configura el título de la ventana.
    clock = pygame.time.Clock()                     #  Se usa para controlar la velocidad de fotogramas (FPS).

    # Se inicializa la pantalla.
    screen_size = (1280, 720)  # Resolución de la pantalla (ancho, alto)
    screen = pygame.display.set_mode(screen_size)

    # Se crea el bloque inicial de la serpiente (cabeza) y se inicializa en un lugar aleatorio de la pantalla.
    snake_head = SnakeBlock(is_head = True)
    snake_head.snake_head_init()

    # Se crea un grupo que va a almacenar el cuerpo de la serpiente, por lo que se agrega la cabeza de la serpiente.
    snake_body = Group()
    snake_body.add(snake_head)

    """NUEVO."""
    # Se crea una manzana en una posición inicial aleatoria en la pantalla.
    apple = Apple()
    apple.random_position(snake_body)

    # Se crea un grupo que va a almacenar las manzanas.
    apples = Group()
    apples.add(apple)

    # Ciclo principal del videojuego.

    # Se crea el objeto con el fondo del videojuego.
    background = Background()

    # Se crea el objeto con el sonido del juego y se reproduce la música y el sonido inicial del juego.
    audio = Audio()
    audio.play_music(volume=Configurations.get_music_volume())
    audio.play_star_sound()

    scoreboard = Scoreboard()

    # Ciclo principal del videojuego.
    game_over = False
    while not game_over:
        """CAMBIO. Ahora la función recibe el grupo de manzanas."""
        # Función que administra los eventos del juego.
        game_over =game_events()

        # Condición de que cerró la ventana.
        if game_over:
            break

        # Función que administra el movimiento de la serpiente.
        snake_movement(snake_body)

        # Se revisan las colisiones en el juego.
        game_over = check_colision(screen,snake_body,apples,audio)

        """CAMBIO. Ahora la función recibe el grupo de manzanas."""
        # Función que administra los elementos de la pantalla.
        screen_refresh(screen, clock, snake_body, apples,background,scoreboard)

        # Si se ha perdido el juego, se llama
        if game_over:
            game_over_screen(audio)

    # Cierra todos los recursos del módulo pygame.
    pygame.quit()


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == "__main__":
    run_game()