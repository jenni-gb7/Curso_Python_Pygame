from Piedras import Piedra
import pygame
from Game_functionalities import screen_refresh
from Media import Background

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Fly Bird")

    background = Background()

    # Crear muchas piedras separadas por 300 px
    obstacles = []
    initial_x = 800
    for i in range(6):  # crea 6 obstáculos espaciados
        obstacles.append(Piedra(initial_x + i * 300))

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        screen_refresh(screen, clock, background)

        obstacles = []
        for i in range(6):
            obstacles.append(Piedra(800 + i * 300, screen))

        # En el bucle principal:
        for obs in obstacles:
            obs.update_position()
            obs.blit(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
if __name__ == '__main__':
    run_game()
