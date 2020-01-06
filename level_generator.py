from os import path
import pygame
from load_image_function import load_image, cell_size, size, width, height
import random
from block_class import Block

level_length = width // cell_size
level_height = height // cell_size


def generate_level():
    y_last = level_height - 10
    generated_map = [[-1 for i in range(level_length)] for j in range(level_height)]
    for x in range(level_length):
        y = random.choice([y_last - 1, y_last, y_last + 1, y_last, y_last, y_last])
        while level_height < y + 1 or y + 1 < 5:
            y = random.choice([y_last - 1, y_last, y_last + 1, y_last, y_last, y_last])
        generated_map[y - 1][x] = 1
        for n_y in range(y, level_height):
            generated_map[n_y][x] = 0
        y_last = y
    return generated_map


block_sprites = pygame.sprite.Group()
level_map = generate_level()

blocks = []
for y in range(level_height):
    for x in range(level_length):
        if level_map[y][x] != -1:
            block = Block(x, y, level_map[y][x])
            block_sprites.add(block)
