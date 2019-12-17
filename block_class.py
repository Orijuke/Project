from os import path
from random import randrange
import random

import pygame


def load_image(name):
    fullname = path.join('textures', name)
    image = pygame.image.load(fullname).convert_alpha()
    return image


cell_size = 50
level_length = 72
level_height = 12
size = width, height = 3600, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 30

def generate_level():
    y_last = level_height - 3
    generated_map = [[-1 for i in range(level_length)] for j in range(level_height)]
    for x in range(level_length):
        y = random.choice([y_last - 1, y_last, y_last + 1])
        print(y)
        while height // cell_size < y + 1 or y + 1 < 5:
            print(y)
            y = random.choice([y_last - 1, y_last, y_last + 1])
        generated_map[y - 1][x] = 1
        for n_y in range(y, level_height):
            generated_map[n_y][x] = 0
        y_last = y
    return generated_map


class Block(pygame.sprite.Sprite):

    grass_image = load_image("grass.png")
    dirt_image = load_image("dirt.png")

    def __init__(self, x, y, grassed):
        super().__init__()
        if grassed:
            self.image = Block.grass_image
        else:
            self.image = Block.dirt_image
        self.rect = self.image.get_rect()
        self.rect.x = x * 50
        self.rect.y = y * 50

    def set_pos(self, x, y):
        self.rect.x = x * cell_size
        self.rect.y = y * cell_size


all_sprites = pygame.sprite.Group()
level_map = generate_level()

blocks = []
for y in range(level_height):
    for x in range(level_length):
        if level_map[y][x] != -1:
            block = Block(x, y, level_map[y][x])
            all_sprites.add(block)


is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        all_sprites.update(event)
    clock.tick(FPS)
    screen.fill(pygame.Color('white'))
    all_sprites.draw(screen)
    pygame.display.flip()


