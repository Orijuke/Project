import pygame
import random

from level_generator import level_height, level_length
from load_image_function import load_image, cell_size, width, height


class Player(pygame.sprite.Sprite):

    player_image = load_image("player.png")

    def __init__(self, x, y):
        super().__init__()
        self.image = Player.player_image
        self.rect = self.image.get_rect()
        self.rect.x = x * cell_size
        self.rect.y = y * cell_size
        self.health = 2000
        self.score = 100
        self.x = x
        self.y = y


class Enemy(pygame.sprite.Sprite):

    enemy_image = load_image("enemy.png")

    def __init__(self, x, y):
        super().__init__()
        self.image = Enemy.enemy_image
        self.rect = self.image.get_rect()
        self.rect.x = x * cell_size
        self.rect.y = y * cell_size
        self.health = 2000
        self.x = x
        self.y = y


player = Player(width // cell_size // 2, 0)
body_sprites = pygame.sprite.Group()
body_sprites.add(player)
enemy_sprites = pygame.sprite.Group()
for n in range(20):
    enemy = Enemy(random.randrange(width // cell_size, level_length - width // cell_size), 0)
    enemy_sprites.add(enemy)
