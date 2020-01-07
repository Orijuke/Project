from os import path
from random import randrange
import random
from level_generator import block_sprites
from player_class import player, body_sprites
import pygame

from block_class import Block
from load_image_function import load_image, cell_size, size, width, height
from camera import Camera

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 30
camera = Camera()


is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.KEYDOWN:
            x, y = player.rect.x, player.rect.y
            new_x = x
            new_y = y
            if event.key == pygame.K_LEFT:
                new_x, new_y = player.rect.x + 100, player.rect.y
            if event.key == pygame.K_RIGHT:
                new_x, new_y = player.rect.x - 100, player.rect.y
            if event.key == pygame.K_UP:
                new_x, new_y = player.rect.x, player.rect.y + 100
            if event.key == pygame.K_DOWN:
                new_x, new_y = player.rect.x, player.rect.y - 100
            dx = new_x - x
            dy = new_y - y
            player.move(dx, dy)
            camera.update(dx)
            for sprite in block_sprites:
                camera.apply(sprite)
            block_sprites.update(event)
    body_sprites.update(event)
    clock.tick(FPS)
    screen.fill(pygame.Color('lightskyblue'))

    # обновляем положение всех спрайтов

    block_sprites.draw(screen)
    pygame.display.flip()
