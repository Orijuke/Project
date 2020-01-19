import sys
from os import path
from random import randrange
import random
from level_generator import block_sprites, spike_sprites, kit_sprites, portal_sprites
from player_class import player, body_sprites, enemy_sprites, Player, new_player, new_enemies
import pygame
from minimap import draw_minimap, health_bar, score_bar
from technical_functions import camera_apply, sprites_draw, sprites_update
from level_generator import level_length, generate_level, place_blocks
from block_class import Block
from load_image_function import load_image, cell_size, size, width, height, load_sound
from camera import Camera, camera
from level_map import new_map

pygame.init()


def load_image_main(name):
    fullname = path.join('textures', name)
    image = pygame.image.load(fullname).convert_alpha()
    return image


screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 30
speed = 1
ticks = 0

jump_sound = load_sound('jump.ogg')

step = cell_size // 5
g = step / 2

step_dict = {
    pygame.K_d: (step, 0),
    pygame.K_a: (-step, 0),
    pygame.K_w: (0, -step),
    pygame.K_s: (0, step)
}

is_jump = False
go_down = False
jump_pos = 0

dy = 0


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
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


def collision_detector(shift):
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
        player.health += 20
        player.score -= 0.1
    if pygame.sprite.spritecollideany(player, enemy_sprites):
        player.health -= 10
        player.score += 0.6
    if pygame.sprite.spritecollideany(player, portal_sprites):
        end_screen(player.score, True)
    if player.score < 0:
        player.score = 0
    if player.health <= 0 or player.rect.y > 800:
        print(player.health)
        end_screen(player.score, False)


def enemies_make_steps():
    for enemy in enemy_sprites:
        enemy.make_step()


def main_game():
    global is_jump, dy
    while True:
        print(player.y, player.rect.y)
        handle_events()
        clock.tick(FPS)
        enemies_make_steps()
        pressed = pygame.key.get_pressed()
        for key, shift in step_dict.items():
            if pressed[key]:
                if key == pygame.K_w and not is_jump:
                    is_jump = True
                    jump_sound.play()
                    dy = cell_size * 0.75
                else:
                    player.rect.y += shift[1]
                camera.update(shift[0])
                player.x += shift[0] / cell_size
                camera_apply()
            collision_detector(shift)
        jump_event()
        screen.fill(pygame.Color('lightskyblue'))
        # обновляем положение всех спрайтов
        sprites_draw(screen)
        draw_minimap()
        health_bar()
        score_bar()
        pygame.display.flip()


player_score = 0


def start_screen():
    font = pygame.font.Font(None, 30)
    text_coord = 50
    intro_text = ['Приветствуем Вас в нашей игре.',
                  "Играя за доброго синего слизня",
                  "в ней Вам предстоит добежать",
                  "до портала, избегая",
                  "препятствия в виде лиловых кустов",
                  "и летающих противников,",
                  "которых можно бить.",
                  "Пополняйте здоровье при помощи",
                  "Голубых цветков",
                  "W - прыжок; A/D - назад/вперёд",
                  'Нажмите Enter для начала игры.',
                  "Желаем удачи!"]
    screen.fill((152, 217, 234))
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('mediumblue'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 800
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    fon_image = load_image_main('player.png')
    fon_image = pygame.transform.scale(fon_image, (800, 800))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
        text_cord = [0, 0]
        rect = fon_image.get_rect()
        rect.x = text_cord[0]
        rect.y = text_cord[1]
        screen.blit(fon_image, rect)
        clock.tick(FPS)
        pygame.display.flip()


def end_screen(score, win):
    global player_score
    if win and score > player_score:
        player_score = score
    font = pygame.font.Font(None, 30)
    text_coord = 50
    t = 'Вы победили, молодцы!' if win else 'Вы проиграли, но молодцы!'
    intro_text = ["Мы снова встретились!",
                  t,
                  "Счёт: " + str(int(score)),
                  "Рекорд при победе: " + str(int(player_score)),
                  'Для начала новой игры нажмите Enter.',
                  "Желаем удачи и новых рекордов!"]
    screen.fill((152, 217, 234))
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('mediumblue'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 800
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    fon_image = load_image_main('player.png')
    fon_image = pygame.transform.scale(fon_image, (800, 800))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    new_map()
                    new_player()
                    new_enemies()
                    player.health = 2000
                    player.score = 0
                    print(body_sprites)
                    main_game()
                    return
        text_cord = [0, 0]
        rect = fon_image.get_rect()
        rect.x = text_cord[0]
        rect.y = text_cord[1]
        screen.blit(fon_image, rect)
        clock.tick(FPS)
        pygame.display.flip()


def terminate():
    pygame.quit()
    sys.exit()


start_screen()
main_game()
terminate()
