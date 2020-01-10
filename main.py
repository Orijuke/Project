from os import path
from random import randrange
import random
from level_generator import block_sprites, spike_sprites, kit_sprites, portal_sprites, level_map
from player_class import player, body_sprites, enemy_sprites
import pygame

from block_class import Block
from load_image_function import load_image, cell_size, size, width, height
from camera import Camera

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 30
g = 10
camera = Camera()


step = 4

step_dict = {
                pygame.K_RIGHT: (step, 0),
                pygame.K_LEFT: (-step, 0),
                pygame.K_UP: (0, -step),
                pygame.K_DOWN: (0, step)
            }

is_jump = False
go_down = False
jump_pos = 0
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
            player.x += shift[0] / cell_size
            player.y += shift[1] / cell_size
            for sprite in block_sprites:
                camera.apply(sprite)
            for sprite in spike_sprites:
                camera.apply(sprite)
            for sprite in kit_sprites:
                camera.apply(sprite)
            for sprite in portal_sprites:
                camera.apply(sprite)
            for sprite in enemy_sprites:
                camera.apply(sprite)
        if pygame.sprite.spritecollideany(player, block_sprites):
            player.rect.y -= shift[1]
            camera.update(-shift[0])
            player.x -= shift[0] / cell_size
            player.y -= shift[1] / cell_size
            for sprite in block_sprites:
                camera.apply(sprite)
            for sprite in spike_sprites:
                camera.apply(sprite)
            for sprite in kit_sprites:
                camera.apply(sprite)
            for sprite in portal_sprites:
                camera.apply(sprite)
            for sprite in enemy_sprites:
                camera.apply(sprite)
        block_sprites.update(event)
        spike_sprites.update(event)
        kit_sprites.update(event)
        portal_sprites.update(event)
        body_sprites.update(event)
        enemy_sprites.update(event)


        if pygame.sprite.spritecollideany(player, spike_sprites):
            player.health -= 20
            player.score *= 1.002
        if pygame.sprite.spritecollideany(player, kit_sprites):
            player.health += 80
            player.score /= 1.002
        if pygame.sprite.spritecollideany(player, portal_sprites):
            is_running = False

    screen.fill(pygame.Color('lightskyblue'))

    # обновляем положение всех спрайтов

    block_sprites.draw(screen)
    spike_sprites.draw(screen)
    kit_sprites.draw(screen)
    portal_sprites.draw(screen)
    body_sprites.draw(screen)
    enemy_sprites.draw(screen)
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
    pygame.draw.rect(screen, pygame.Color('red'), (20 + player.x * 2, 20 + player.y * 2, 2, 2))
    pygame.draw.rect(screen, pygame.Color('black'), (20 + player.x * 2, 10, 2, 6))
    for enemy in enemy_sprites:
        pygame.draw.rect(screen, pygame.Color('brown'), (20 + enemy.x * 2, 20 + enemy.y * 2, 2, 2))
    pygame.display.flip()
