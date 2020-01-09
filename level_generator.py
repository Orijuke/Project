from os import path
import pygame
from load_image_function import load_image, cell_size, size, width, height
import random
from block_class import Block, Spike, Kit, Portal

### air=-1 dirt=0 grass=1 spike=2 kit=3 portal=4 portal1=5

level_length = width * 4 // cell_size
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
spike_sprites = pygame.sprite.Group()
kit_sprites = pygame.sprite.Group()
portal_sprites = pygame.sprite.Group()
level_map = generate_level()

blocks = []
for y in range(level_height):
    for x in range(level_length):
        if level_map[y][x] != -1:
            block = Block(x, y, level_map[y][x])
            block_sprites.add(block)

spikes = []
for x in range(level_length):
    for y in range(level_height):
        if level_map[y + 1][x] == 1:
            need_to_be_placed = random.randrange(0, 5)
            if need_to_be_placed == 0:
                spike = Spike(x, y)
                spike_sprites.add(spike)
                level_map[y][x] = 2
            break

kits = []
for x in range(level_length):
    for y in range(level_height):
        if level_map[y + 1][x] == 1:
            if level_map[y][x] != 2:
                need_to_be_placed = random.randrange(0, 20)
                if need_to_be_placed == 0:
                    kit = Kit(x, y)
                    kit_sprites.add(kit)
                    level_map[y][x] = 3
            break

portals = []
for y in range(level_height):
    if level_map[y + 2][-width // cell_size // 2] == 1:
        print(True)
        portal = Portal(level_length - width // cell_size // 2, y, True)
        portal1 = Portal(level_length - width // cell_size // 2, y + 1, False)
        portal_sprites.add(portal)
        portal_sprites.add(portal1)
        level_map[y][-width // cell_size // 2] = 4
        level_map[y + 1][-width // cell_size // 2] = 5
        break
