import pygame
from load_image_function import load_image, cell_size


class Player(pygame.sprite.Sprite):

    player_image = load_image("player.png")

    def __init__(self, x, y):
        super().__init__()
        self.image = Player.player_image
        self.rect = self.image.get_rect()
        self.rect.x = x * cell_size
        self.rect.y = y * cell_size
        self.health = 100

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy


player = Player(0, 0)
body_sprites = pygame.sprite.Group()
body_sprites.add(player)
