from os import path
from random import randrange
import random
from level_generator import block_sprites
import pygame

from block_class import Block
from load_image_function import load_image, cell_size, size, width, height


screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 30



is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        block_sprites.update(event)
    clock.tick(FPS)
    screen.fill(pygame.Color('lightskyblue'))
    block_sprites.draw(screen)
    pygame.display.flip()