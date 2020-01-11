import pygame

from level_generator import level_map
from load_image_function import load_image, screen, cell_size
from player_class import player, enemy_sprites


def draw_minimap():
    for i in range(len(level_map)):
        for j in range(len(level_map[i])):
            color = 'lightskyblue'
            if level_map[i][j] == 0:
                color = 'sienna'
            if level_map[i][j] == 1:
                color = 'darkgreen'
            if level_map[i][j] == 2:
                color = 'deeppink'
            if level_map[i][j] == 3:
                color = 'blue'
            if level_map[i][j] == 4 or level_map[i][j] == 5:
                color = 'yellow'
            pygame.draw.rect(screen, pygame.Color(color), (20 + j * 2, 20 + i * 2, 2, 2))
    print(player.x, player.rect.x)
    pygame.draw.rect(screen, pygame.Color('red'), (20 + player.x * 2, 20 + player.y * 2 + 1, 2, 2))
    pygame.draw.rect(screen, pygame.Color('black'), (20 + player.x * 2, 10, 2, 6))
    for enemy in enemy_sprites:
        pygame.draw.rect(screen, pygame.Color('brown'), (20 + enemy.x * 2, 20 + enemy.y * 2, 2, 2))

def health_bar():
    f = pygame.font.SysFont('serif', 30)
    t = f.render('Health: ' + str(int(player.health)), 0, (0, 0, 0))
    screen.blit(t, (10, 240))

def score_bar():
    f = pygame.font.SysFont('serif', 30)
    t = f.render('Score: ' + str(int(player.score)), 0, (0, 0, 0))
    screen.blit(t, (10, 270))