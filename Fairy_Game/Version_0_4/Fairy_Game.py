import pygame
from Configurations import Configurations
from Media import Background
from Game_functionalities import screen_refresh
from Piedras import Piedra

def run_game():
    pygame.init()

    # Se inicializa la pantalla.
    screen_size = (1280, 720)
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Fly Bird")

    background = Background()

    obstacles = []
    initial_x = 800
    for i in range(6):
        obstacles.append(Piedra(initial_x + i * 250, screen))

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        screen_refresh(screen, background)  # Solo dibuja fondo

        for obs in obstacles:
            obs.update()
            obs.draw()

        pygame.display.flip()  # Muestra el frame completo
        clock.tick(Configurations.get_fps())  # Controla FPS

    pygame.quit()
if __name__ == '__main__':
    run_game()