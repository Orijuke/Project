import pygame

from level_generator import level_height
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

    def move(self, dy):
        self.rect.y += dy

class Enemy(pygame.sprite.Sprite):

    player_image = load_image("player.png")

    def __init__(self, x, y):
        super().__init__()
        self.image = Player.player_image
        self.rect = self.image.get_rect()
        self.rect.x = x * cell_size
        self.rect.y = y * cell_size
        self.health = 2000
        self.score = 100

    def move(self, dy):
        self.rect.y += dy


player = Player(width // cell_size // 2, level_height // 2)
body_sprites = pygame.sprite.Group()
body_sprites.add(player)
