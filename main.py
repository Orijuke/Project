from os import path
from random import randrange
import random
from level_generator import block_sprites, spike_sprites, kit_sprites, portal_sprites, level_map
from player_class import player, body_sprites, enemy_sprites
import pygame
from minimap import draw_minimap, health_bar, score_bar
from technical_functions import camera_apply, sprites_draw, sprites_update

from block_class import Block
from load_image_function import load_image, cell_size, size, width, height, load_sound
from camera import Camera, camera

pygame.init()

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 100
speed = 1
ticks = 0

step = 4
g = step / 2

step_dict = {
    pygame.K_RIGHT: (step, 0),
    pygame.K_LEFT: (-step, 0),
    pygame.K_UP: (0, -step),
    pygame.K_DOWN: (0, step)
}

is_jump = False
go_down = False
jump_pos = 0

dy = 0
is_running = True


def handle_events():
    global is_running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        for enemy in enemy_sprites:

            enemy.get_event(event)


def jump_event():
    global is_jump, dy
    dy -= g
    player.rect.y -= dy
    player.y = player.rect.y / cell_size
    while pygame.sprite.spritecollideany(player, block_sprites):
        player.rect.y -= 1
        player.y = player.rect.y / cell_size
        is_jump = False
        dy = 0


def collision_detector():
    global is_running
    if pygame.sprite.spritecollideany(player, block_sprites):
        player.rect.y -= shift[1]
        camera.update(-shift[0])
        player.x -= shift[0] / cell_size
        player.y = player.rect.y / cell_size
        camera_apply()
    sprites_update()
    if pygame.sprite.spritecollideany(player, spike_sprites):
        player.health -= 10
        player.score += 0.2
    if pygame.sprite.spritecollideany(player, kit_sprites):
        player.health += 8
        player.score -= 0.1
    if pygame.sprite.spritecollideany(player, enemy_sprites):
        player.health -= 40
        player.score += 0.6
    if pygame.sprite.spritecollideany(player, portal_sprites) or player.health <= 0:
        is_running = False

def enemies_make_steps():
    for enemy in enemy_sprites:
        enemy.make_step()


while is_running:
    handle_events()
    clock.tick(FPS)
    enemies_make_steps()
    pressed = pygame.key.get_pressed()
    for key, shift in step_dict.items():
        if pressed[key]:
            if key == pygame.K_UP and not is_jump:
                is_jump = True
                dy = 15
            else:
                player.rect.y += shift[1]
            camera.update(shift[0])
            player.x += shift[0] / cell_size
            player.y = player.rect.y / cell_size
            camera_apply()
        collision_detector()
    jump_event()
    screen.fill(pygame.Color('lightskyblue'))
    # обновляем положение всех спрайтов
    sprites_draw(screen)
    draw_minimap()
    health_bar()
    score_bar()
    pygame.display.flip()
