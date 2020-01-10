from os import path
from random import randrange
import random
from level_generator import block_sprites, spike_sprites, kit_sprites, portal_sprites, level_map
from player_class import player, body_sprites, enemy_sprites
import pygame
from minimap import draw_minimap
from technical_functions import camera_apply, sprites_draw, sprites_update

from block_class import Block
from load_image_function import load_image, cell_size, size, width, height
from camera import Camera, camera

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 100
g = 10

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
            camera_apply()
        if pygame.sprite.spritecollideany(player, block_sprites):
            player.rect.y -= shift[1]
            camera.update(-shift[0])
            player.x -= shift[0] / cell_size
            player.y -= shift[1] / cell_size
            camera_apply()
        sprites_update(event)

        for enemy in enemy_sprites:
            enemy.get_event(event)

        if pygame.sprite.spritecollideany(player, spike_sprites):
            player.health -= 20
            player.score *= 1.002
        if pygame.sprite.spritecollideany(player, kit_sprites):
            player.health += 80
            player.score /= 1.006
        if pygame.sprite.spritecollideany(player, enemy_sprites):
            player.health -= 40
            player.score *= 1.004
        if pygame.sprite.spritecollideany(player, portal_sprites):
            is_running = False

    screen.fill(pygame.Color('lightskyblue'))
    # обновляем положение всех спрайтов

    sprites_draw(screen)
    draw_minimap()
    pygame.display.flip()
