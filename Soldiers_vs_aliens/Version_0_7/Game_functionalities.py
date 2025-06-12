import pygame
from Configurations import Configurations
from Media import Background
from Soldier import Soldier
from Alien import Alien
from Shot import Shot



def game_events(soldier: Soldier, gunshots: pygame.sprite.Group) -> bool:
    """
    Administra los eventos del teclado y del sistema.
    :param soldier: Objeto del personaje principal.
    :param gunshots: Grupo de disparos activos en pantalla.
    :return: True si se debe terminar el juego, False en caso contrario.
    """
    game_over = False

    for event in pygame.event.get():
        # Evento de salida del juego
        if event.type == pygame.QUIT:
            game_over = True

        # Evento de presionar una tecla
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                soldier.is_moving_up = True
            elif event.key == pygame.K_DOWN:
                soldier.is_moving_down = True
            elif event.key == pygame.K_SPACE:
                new_shot = Shot(soldier)
                gunshots.add(new_shot)
                soldier.shoots()

        # Evento de soltar una tecla
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                soldier.is_moving_up = False
            elif event.key == pygame.K_DOWN:
                soldier.is_moving_down = False

    return game_over


def screen_refresh(screen: pygame.surface.Surface,
                   clock: pygame.time.Clock,
                   background: Background,
                   soldier: Soldier,
                   gunshots: pygame.sprite.Group,
                   aliens: pygame.sprite.Group) -> None:
    """
    Administra la actualización y dibujo de todos los elementos en pantalla.
    :param screen: Superficie principal de Pygame.
    :param clock: Objeto para controlar los FPS.
    :param background: Imagen de fondo.
    :param soldier: Personaje principal.
    :param gunshots: Grupo de disparos activos.
    :param aliens: Grupo de alienígenas activos.
    """
    # Fondo
    background.blit(screen)

    # Soldado
    soldier.update_position(screen)
    soldier.update_animation()
    soldier.blit(screen)

    # Disparos
    for shot in gunshots.sprites():
        shot.update_position()
        shot.update_animation()
        shot.blit(screen)

    # Alienígenas
    for alien in aliens.sprites():
        alien.update_position()
        alien.update_animation()
        alien.blit(screen)

    # Actualizar pantalla
    pygame.display.flip()

    # Limitar la velocidad de fotogramas
    clock.tick(Configurations.get_fps())
