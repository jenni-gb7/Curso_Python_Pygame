"""
Nombre: Jennifer Marlene Gutiérrez Beteta
Fecha: 08/04/2025
Version 05:
- Se agregaron banderas de movimiento como atributos de clase de SnakeBlock, ya que van a indicar el movimiento
  de la cabeza de la serpiente. De igual manera, se agregaron los getter y setters de esos atributos como
  métodos de clase.
- Las banderas se modifican de acuerdo a la tecla presionada (⬅️⬆️⬇️➡️) en la función game_events().
- Como la idea del juego es que la serpiente se encuentre en movimiento, entonces siempre se tiene una bandera
  como verdadera.
- Se agregó la función snake_movement() en el módulo Game_functionalities.py, que va a actualizar el movimiento
  de la serpiente. En esta versión, únicamente actualiza la cabeza de la serpiente.
- Como resultado, se tiene un cuadrado que se mueve por toda la pantalla y fuera de ella.

"""
# Se importan los módulos necesarios.
import pygame
from Configurations import Configurations
from Game_functionalities import game_events, screen_refresh, snake_movement
from Snake import SnakeBlock
from pygame.sprite import Group


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

    # Ciclo principal del videojuego.
    game_over = False
    while not game_over:
        # Función que administra los eventos del juego.
        game_over = game_events()

        """NUEVO."""
        # Función que administra el movimiento de la serpiente.
        snake_movement(snake_body)

        # Función que administra los elementos de la pantalla.
        screen_refresh(screen, clock, snake_body)

    # Cierra todos los recursos del módulo pygame.
    pygame.quit()



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == "__main__":
    run_game()