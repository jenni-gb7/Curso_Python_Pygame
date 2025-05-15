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
from Game_functionalities import game_events, screen_refresh, snake_movement, check_collisions, game_over_screen
from Snake import SnakeBlock
from pygame.sprite import Group
from Apple import Apple
"""CAMBIO. Ahora también se importa la clase Scoreboard."""
from Media import Background, Audio, Scoreboard


def run_game() -> None:
    """
    Función principal del videojuego.
    """
    # Se inicializa el módulo de pygame y se realizan las configuraciones iniciales.
    pygame.init()
    screen = pygame.display.set_mode(Configurations.get_screen_size())  # Resolución de la pantalla (ancho, alto).
    pygame.display.set_caption(Configurations.get_game_title())         # Se configura el título de la ventana.
    clock = pygame.time.Clock()                     #  Se usa para controlar la velocidad de fotogramas (FPS).

    # Se crea el bloque inicial de la serpiente (cabeza) y se inicializa en un lugar aleatorio de la pantalla.
    snake_head = SnakeBlock(is_head = True)
    snake_head.snake_head_init()

    # Se crea un grupo que va a almacenar el cuerpo de la serpiente, por lo que se agrega la cabeza de la serpiente.
    snake_body = Group()
    snake_body.add(snake_head)

    # Se crea una manzana en una posición inicial aleatoria en la pantalla.
    apple = Apple()
    apple.random_position(snake_body)

    # Se crea un grupo que va a almacenar las manzanas.
    apples = Group()
    apples.add(apple)

    # Se crea el objeto del fondo de pantalla.
    background = Background()

    # Se crea el objeto con el sonido del juego y se reproduce la música y el sonido inicial del juego.
    audio = Audio()
    audio.play_music(volume = Configurations.get_music_volume())
    audio.play_star_sound()

    """NUEVO."""
    # Se crea el objeto con el marcador del juego.
    scoreboard = Scoreboard()

    # Ciclo principal del videojuego.
    game_over = False
    while not game_over:
        # Función que administra los eventos del juego.
        game_over = game_events()

        # Si el usuario ha cerrado la ventana, entonces se termina el ciclo inmediatamente para cerrar la ventana.
        if game_over:
            break

        # Función que administra el movimiento de la serpiente.
        snake_movement(snake_body)

        """CAMBIO. Ahora también recibe el objeto con el marcador."""
        # Función que revisa las colisiones en el juego.
        game_over = check_collisions(screen, snake_body, apples, audio, scoreboard)

        """CAMBIO. Ahora también recibe el objeto con el marcador."""
        # Función que administra los elementos de la pantalla.
        screen_refresh(screen, clock, snake_body, apples, background, scoreboard)

        # Si el usuario ha perdido la partida, entonces se llama a la función que muestra la pantalla
        # del fin del juego.
        if game_over:
            """CAMBIO. Ahora también recibe el objeto de la pantalla."""
            game_over_screen(screen, audio)

    # Cierra todos los recursos del módulo pygame.
    pygame.quit()



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == "__main__":
    run_game()