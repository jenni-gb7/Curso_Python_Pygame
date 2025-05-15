import pygame
from Configurations import Configurations
from Snake import SnakeBlock
from Apple import Apple
import time
"""CAMBIO. Ahora también se importan las clases Scoreboard, GameOverImage y Credits."""
from Media import Background, Audio, Scoreboard, GameOverImage, Credits


def game_events() -> bool:
    """
    Función que administra los eventos del juego.
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


"""CAMBIO. Ahora también recibe el objeto con el marcador."""
def check_collisions(screen: pygame.surface.Surface, snake_body: pygame.sprite.Group,
                     apples: pygame.sprite.Group, audio: Audio, scoreboard: Scoreboard) -> bool:
    """
    Función que revisa las colisiones en el juego: cabeza de la serpiente - cuerpo de la serpiente,
    cabeza de la serpiente - borde de la pantalla, cabeza de la serpiente - manzana.
    :param screen: Objeto con la pantalla.
    :param snake_body: Grupo con el cuerpo de la serpiente.
    :param apples: Grupo de las manzanas.
    :param audio: Objeto con el audio del juego.
    :param scoreboard: Objeto con el marcador.
    :return: La bandera de fin del juego.
    """
    # Se declaran variables que se utilizan en la función.
    game_over = False                       # Bandera de fin del juego que se retorna.
    screen_rect = screen.get_rect()         # Se obtiene el rectángulo de la pantalla.
    head = snake_body.sprites()[0]          # La cabeza de la serpiente es el elemento [0] del grupo.

    # Lista de colisiones entre la cabeza de la serpiente - cuerpo de la serpiente.
    head_body_collisions = pygame.sprite.spritecollide(head, snake_body, dokill = False)

    # Lista de colisiones entre la cabeza de la serpiente - manzanas.
    # Nota: El 'dokill = True' indica que, si hay colisión, se va a remover la manzana del grupo.
    head_apples_collisions = pygame.sprite.spritecollide(head, apples, dokill = True)

    # Primero, se revisa que se tengan colisiones de la serpiente - cuerpo de la serpiente.
    # Nota: Debe ser mayor a 1 porque la cabeza forma parte del cuerpo y lo cuenta como colisión.
    if len(head_body_collisions) > 1:
        game_over = True

    # Se revisa la colisión entre la cabeza de la serpiente - bordes de la pantalla.
    elif (head.rect.right > screen_rect.right or head.rect.left < screen_rect.left
          or head.rect.top < screen_rect.top or head.rect.bottom > screen_rect.bottom):
        game_over = True

    # Se revisa la colisión entre la cabeza de la serpiente - manzana.
    elif len(head_apples_collisions) > 0:
        # Si hubo colisión, se crea un nuevo bloque de la serpiente y se coloca en la cola de la serpiente.
        new_snake_block = SnakeBlock()
        new_snake_block.rect.x = snake_body.sprites()[-1].rect.x
        new_snake_block.rect.y = snake_body.sprites()[-1].rect.y
        snake_body.add(new_snake_block)

        # Se agrega otra manzana en una ubicación aleatoria.
        new_apple = Apple()
        new_apple.random_position(snake_body)
        apples.add(new_apple)

        # Se reproduce el sonido de que la serpiente ha comido la manzana.
        audio.play_eats_apple_sound()

        """NUEVO."""
        # Se actualiza el marcador.
        scoreboard.update(new_score = Apple.get_no_apples() - 1)

    # Se regresa la bandera.
    return game_over


"""CAMBIO. Ahora también recibe el objeto con el marcador."""
def screen_refresh(screen: pygame.surface.Surface, clock: pygame.time.Clock,
                   snake_body: pygame.sprite.Group, apples: pygame.sprite.Group,
                   background: Background, scoreboard: Scoreboard) -> None:
    """
    Función que administra los elementos de la pantalla.
    :param screen: Objeto con la pantalla.
    :param clock: Objeto con el reloj del videojuego.
    :param snake_body: Grupo con el cuerpo de la serpiente.
    :param apples: Grupo de las manzanas.
    :param background: Objeto con el fondo de pantalla.
    :param scoreboard: Objeto con el marcador.
    """
    # Se dibujan los elementos en la pantalla.
    background.blit(screen)

    # Se anima la manzana.
    apples.sprites()[0].animate_apple()

    # Se dibujan las manzanas.
    apples.draw(screen)

    # Se anima la cabeza de la serpiente.
    snake_body.sprites()[0].animate_snake_head()

    # Se dibuja la serpiente, dibujando primero el último bloque y al último la cabeza de la serpiente.
    for snake_block in reversed(snake_body.sprites()):
        snake_block.blit(screen)

    """NUEVO."""
    # Se dibuja el marcador.
    scoreboard.blit(screen)

    # Se actualiza la pantalla, dando la impresión de movimiento.
    pygame.display.flip()

    # Se controla la velocidad de fotogramas (FPS) del videojuego.
    clock.tick(Configurations.get_fps())


"""CAMBIO. Ahora también recibe el objeto de la pantalla."""
def game_over_screen(screen: pygame.surface.Surface, audio: Audio) -> None:
    """
    Función con la pantalla del fin del juego.
    :param screen: Objeto con la pantalla.
    :param audio: Objeto con el audio del juego.
    """
    """NUEVO."""
    # Se crean los objetos con las imágenes del fin del juego y de los créditos.
    game_over_image = GameOverImage()
    credits_image = Credits()

    """"NUEVO."""
    # Se dibujan las imágenes del fin del juego y de los créditos.
    game_over_image.blit(screen)
    credits_image.blit(screen)

    """NUEVO."""
    # Se actualiza la pantalla.
    pygame.display.flip()

    # Se realiza un desvanecimiento de la música y se reproduce el sonido de fin del juego.
    audio.music_fadeout(time = Configurations.get_music_fadeout_time())
    audio.play_game_over_sound()

    # Se agrega una pausa para que el usuario se dé cuenta de que ha perdido.
    time.sleep(Configurations.get_game_over_screen_time())