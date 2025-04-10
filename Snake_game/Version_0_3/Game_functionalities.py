import pygame
from Configurations import Configurations
from Snake  import  SnakeBlock

def game_event() -> bool:
    """
    Función que administra ñps eneventos del juego
    retrun: La bandera del fin del juego
    """

    #Se declara la bandera del fin del juego
    game_over = False

    #Se verifican los eventos de
    for event in pygame.event.get():
        #Un clic en cerrar el juego
        if event.type == pygame.QUIT:
            game_over = True

    #Se regresa la bandera
    return game_over
def screen_refresh(screen: pygame.surface.Surface, clock: pygame.time.Clock, snake_head: SnakeBlock) -> None:
    """
    Función que administrar los elementos visuales del juego
    """
    #Fondo de la pantaña
    screen.fill(Configurations.get_background())
    #Se dibuja la cabeza de la serpiente
    snake_head.blit(screen)
    pygame.display.flip()

    #Se controla la velocidad de FPS
    clock.tick(Configurations.get_fps())