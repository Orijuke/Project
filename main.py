from os import path
from random import randrange
import random
from level_generator import block_sprites, spike_sprites, kit_sprites
from player_class import player, body_sprites
import pygame

from block_class import Block
from load_image_function import load_image, cell_size, size, width, height
from camera import Camera

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 30
g = 10
camera = Camera()


step = 2

step_dict = {
                pygame.K_RIGHT: (step, 0),
                pygame.K_LEFT: (-step, 0),
                pygame.K_UP: (0, -step),
                pygame.K_DOWN: (0, step)
            }
is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    clock.tick(FPS)
    pressed = pygame.key.get_pressed()
    for key, shift in step_dict.items():
        if pressed[key]:
            player.rect.y += shift[1]
            camera.update(shift[0])
            for sprite in block_sprites:
                camera.apply(sprite)
            for sprite in spike_sprites:
                camera.apply(sprite)
            for sprite in kit_sprites:
                camera.apply(sprite)
            block_sprites.update(event)
            spike_sprites.update(event)
            kit_sprites.update(event)
            body_sprites.update(event)
        if pygame.sprite.spritecollideany(player, block_sprites):
            player.rect.y -= shift[1]
            camera.update(-shift[0])
            for sprite in block_sprites:
                camera.apply(sprite)
            for sprite in spike_sprites:
                camera.apply(sprite)
            for sprite in kit_sprites:
                camera.apply(sprite)
            block_sprites.update(event)
            spike_sprites.update(event)
            kit_sprites.update(event)
            body_sprites.update(event)
        if pygame.sprite.spritecollideany(player, spike_sprites):
            player.health -= 20
        if pygame.sprite.spritecollideany(player, kit_sprites):
            player.health += 80

    screen.fill(pygame.Color('lightskyblue'))

    # обновляем положение всех спрайтов

    block_sprites.draw(screen)
    spike_sprites.draw(screen)
    kit_sprites.draw(screen)
    body_sprites.draw(screen)
    print(player.health)
    pygame.display.flip()
