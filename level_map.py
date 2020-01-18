import pygame

from level_generator import generate_level, place_blocks

level_map = []


def new_map():
    global level_map
    level_map = generate_level()
    level_map = place_blocks(level_map)


new_map()
