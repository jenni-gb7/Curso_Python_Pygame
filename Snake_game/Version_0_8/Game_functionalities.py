import pygame
from Configurations import Configurations
from Snake import SnakeBlock
"""NUEVO."""
from Apple import Apple


"""CAMBIO. Ahora la función recibe el grupo de manzanas."""
def game_events(snake_body: pygame.sprite.Group, apples: pygame.sprite.Group) -> bool:
    """
    Función que administra los eventos del juego.
    :param snake_body: Grupo con el cuerpo de la serpiente.
    :param apples: Grupo de las manzanas.
    :return: La bandera de fin del juego.
    """
    # Se declara la bandera de fin del juego que se retorna.
    game_over = False

    # Se verifican los eventos (teclado y ratón) del juego.
    for event in pygame.event.get():
        # El evento es un clic para cerrar el juego.
        if event.type == pygame.QUIT:
            game_over = True

        # El evento es presionar una tecla (KEYDOWN).
        elif event.type == pygame.KEYDOWN:
            # Movimiento hacia la derecha.
            if event.key == pygame.K_RIGHT:
                SnakeBlock.set_is_moving_right(True)
                SnakeBlock.set_is_moving_left(False)
                SnakeBlock.set_is_moving_up(False)
                SnakeBlock.set_is_moving_down(False)

            # Movimiento hacia la izquierda.
            if event.key == pygame.K_LEFT:
                SnakeBlock.set_is_moving_right(False)
                SnakeBlock.set_is_moving_left(True)
                SnakeBlock.set_is_moving_up(False)
                SnakeBlock.set_is_moving_down(False)

            # Movimiento hacia arriba.
            if event.key == pygame.K_UP:
                SnakeBlock.set_is_moving_right(False)
                SnakeBlock.set_is_moving_left(False)
                SnakeBlock.set_is_moving_up(True)
                SnakeBlock.set_is_moving_down(False)

            # Movimiento hacia abajo.
            if event.key == pygame.K_DOWN:
                SnakeBlock.set_is_moving_right(False)
                SnakeBlock.set_is_moving_left(False)
                SnakeBlock.set_is_moving_up(False)
                SnakeBlock.set_is_moving_down(True)

            """CAMBIO. Ahora se agregan una nueva manzana al grupo y se elimina la anterior."""
            # Se agrega un nuevo bloque al cuerpo de la serpiente.
            if event.key == pygame.K_SPACE:
                new_snake_block = SnakeBlock()
                snake_body.add(new_snake_block)

                new_apple = Apple()
                new_apple.random_position(snake_body)
                print(Apple.get_no_apples())

                apples.remove(apples.sprites()[0])
                # Forma diferente.
                #apples.empty
                apples.add(new_apple)

    # Se regresa la bandera.
    return game_over


def snake_movement(snake_body: pygame.sprite.Group) -> None:
    """
    Función que gestiona los movimientos de los bloques que componen el cuerpo de la serpiente.
    :param snake_body: Grupo con el cuerpo de la serpiente.
    """
    # Para el movimiento de cada bloque de la serpiente, se debe asignar la posición de su bloque predecesor.
    body_size = len(snake_body.sprites()) - 1
    for i in range(body_size, 0, -1):
        snake_body.sprites()[i].rect.x = snake_body.sprites()[i - 1].rect.x
        snake_body.sprites()[i].rect.y = snake_body.sprites()[i - 1].rect.y

    # El movimiento de la cabeza de la serpiente depende de las banderas de movimiento.
    head = snake_body.sprites()[0]          # La cabeza de la serpiente es el elemento [0] del grupo.

    if SnakeBlock.get_is_moving_right():
        head.rect.x += Configurations.get_snake_block_size()

    elif SnakeBlock.get_is_moving_left():
        head.rect.x -= Configurations.get_snake_block_size()

    elif SnakeBlock.get_is_moving_up():
        head.rect.y -= Configurations.get_snake_block_size()

    elif SnakeBlock.get_is_moving_down():
        head.rect.y += Configurations.get_snake_block_size()

def check_colision(screen: pygame.surface.Surface,snake_body: pygame.sprite.Group,apples: pygame.sprite.Group)-> bool:
    """
    Función que revisa ñas collisiones del juegi:
    * Cabeza de la serpiente con el cuerpo.}
    *Cabeza de la serpiente con el borde de la pantalla.
    *Cabeza de la serpiente con la manzana.
    :param screen: Pantalla.
    :param snake_body: cuerpo de la serpiente.
    :param apples: Grupo con las manzanas.
    :return: La bandera de fin de juego.
    """
    # Se declara la bandera de fin de juego.
    game_over = False

    # Se obtiene la cabeza de la serpiente.
    head = snake_body.sprites()[0]

    # Se revisa la condición de la cabeza de la serpiente.
    screen_rect = screen.get_rect()

    # Condición para el fin del juego, al salir de la pantalla.
    if head.rect.right > screen_rect.right or head.rect.left < screen_rect.left or head.rect.bottom > screen_rect.bottom or head.rect.top < screen_rect.top :
        game_over = True
    return game_over


"""CAMBIO. Ahora la función recibe el grupo de manzanas."""
def screen_refresh(screen: pygame.surface.Surface, clock: pygame.time.Clock,
                   snake_body: pygame.sprite.Group, apples: pygame.sprite.Group) -> None:
    """
    Función que administra los elementos de la pantalla.
    :param screen: Objeto con la pantalla.
    :param clock: Objeto con el reloj del videojuego.
    :param snake_body: Grupo con el cuerpo de la serpiente.
    :param apples: Grupo de las manzanas.
    """
    # Se dibujan los elementos en la pantalla.
    screen.fill(Configurations.get_background())    # Fondo de la pantalla en formato RGB.

    """NUEVO."""
    # Se dibujan las manzanas.
    apples.draw(screen)

    # Se dibuja la serpiente, dibujando primero el último bloque y al último la cabeza de la serpiente.
    for snake_block in reversed(snake_body.sprites()):
        snake_block.blit(screen)

    # Se actualiza la pantalla, dando la impresión de movimiento.
    pygame.display.flip()

    # Se controla la velocidad de fotogramas (FPS) del videojuego.
    clock.tick(Configurations.get_fps())