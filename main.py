from os import path
from random import randrange
import random
from level_generator import block_sprites
import pygame

from block_class import Block
from load_image_function import load_image, cell_size, size, width, height
from camera import Camera

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 30
camera = Camera()


class Player(pygame.sprite.Sprite):
    player_image = load_image("player.png")

    def __init__(self, x, y):
        super().__init__()
        self.image = Player.player_image
        self.rect = self.image.get_rect()
        self.rect.x = x * cell_size
        self.rect.y = y * cell_size
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y
        self.rect.x = x * cell_size + (cell_size - self.rect.width) // 2
        self.rect.y = y * cell_size + (cell_size - self.rect.height) // 2


player = Player(3, 4)
body_sprites = pygame.sprite.Group()

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.KEYDOWN:
            x, y = player.x, player.y
            new_x = x
            new_y = y
            dx = new_x - x
            dy = new_y - y
            if event.key == pygame.K_LEFT:
                new_x, new_y = player.x - 1, player.y
            if event.key == pygame.K_RIGHT:
                new_x, new_y = player.x + 1, player.y
            if event.key == pygame.K_UP:
                new_x, new_y = player.x, player.y - 1
            if event.key == pygame.K_DOWN:
                new_x, new_y = player.x, player.y + 1
            player.move(new_x, new_y)
            camera.update(dx, dy)
            for sprite in block_sprites:
                camera.apply(sprite)
            body_sprites.update(event)
            block_sprites.update(event)
            print(camera.dx, camera.dy)
    clock.tick(FPS)
    screen.fill(pygame.Color('lightskyblue'))

    # обновляем положение всех спрайтов

    block_sprites.draw(screen)
    pygame.display.flip()
