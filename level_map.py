import pygame

from level_generator import generate_level, place_blocks, block_sprites, spike_sprites, kit_sprites, portal_sprites

level_map = []


def new_map():
    global level_map
    for el in block_sprites:
        el.kill()
    for el in spike_sprites:
        el.kill()
    for el in kit_sprites:
        el.kill()
    for el in portal_sprites:
        el.kill()
    level_map = generate_level()
    level_map = place_blocks(level_map)


new_map()
