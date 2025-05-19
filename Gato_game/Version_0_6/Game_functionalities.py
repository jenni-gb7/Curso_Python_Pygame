import pygame
from Configurations import Configurations
from Media import Background, TurnImage,ResultsImage,CreditsImage
from TikTacToe import TicTacToeMark

def game_events(marks_group,turn_image)-> bool:
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
                # Verificar si la celda está libre
                occupied = any(mark.cell_number == cell for mark in marks_group)
                if not occupied:
                    new_mark = TicTacToeMark(cell)
                    marks_group.add(new_mark)
                    turn_image.change_turn(TicTacToeMark.turno)
    # Se regresa  la bandera.
    return game_over

def screen_refresh(screen: pygame.surface.Surface,clock: pygame.time.Clock,background: Background,marks_group, turn_image: TurnImage)-> None:
    """
    Función que administra los elementos visuales del juego.
    """
    # Se dibuja el fondo de la pantalla.
    background.blit(screen)

    # Se dibujan las marcas
    marks_group.draw(screen)

    # Se dibujan los turnos.
    turn_image.blit(screen)

    # Se actualiza la pantalla.
    pygame.display.flip()

    # Se controla la velocidad de FPS
    clock.tick(Configurations.get_fps())


def check_winner(marks_group):
    # Diccionario con las marcas en cada celda
    board = {}  # {1: "X", 2: "O", ..., 9: "X"}

    for mark in marks_group:
        board[mark.cell_number] = mark.turno  # Usamos el atributo turn que tiene "X" u "O"

    # Posibles combinaciones ganadoras
    winning_combinations = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  # Horizontales
        (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Verticales
        (1, 5, 9), (3, 5, 7)  # Diagonales
    ]
    # Verificar si hay un ganador
    for combo in winning_combinations:
        a, b, c = combo
        if board.get(a) and board.get(a) == board.get(b) == board.get(c):
            return True, board[a]  # Ganó 'X' o 'O'

    # Si todas las celdas están llenas y no hay ganador, es empate
    if len(board) == 9:
        return True, "draw"

    # Si no hay ganador ni empate, el juego sigue
    return False, ""

def game_over_screen(screen, clock, background, marks_group, turn_image, result):
    result_image = ResultsImage(result)
    credits_image = CreditsImage()

    for _ in range(3):  # 3 ciclos de parpadeo (mostrar y ocultar)
        screen_refresh(screen, clock, background, marks_group, turn_image)
        result_image.blit(screen)
        pygame.display.flip()
        pygame.time.wait(500)

        screen_refresh(screen, clock, background, marks_group, turn_image)
        pygame.display.flip()
        pygame.time.wait(500)

    credits_image.blit(screen)
    pygame.display.flip()
    pygame.time.wait(2500)