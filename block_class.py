from os import path
from random import randrange

import pygame


def load_image(name):
    fullname = path.join('data', name)
    image = pygame.image.load(fullname).convert_alpha()
    return image

cell_size = 50
size = width, height = 600, 150
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 30

class Block(pygame.sprite.Sprite):

    grass_image = load_image("grass.png")
    dirt_image = load_image("dirt.png")

    def __init__(self, x, y, grassed=False):
        super().__init__()
        if type:
            self.image = Block.grass_image
        else:
            self.image = Block.dirt_image
        self.rect = self.image.det_rect()
        self.rect.x = x * 50
        self.rect.y = y * 50

    def set_pos(self, x, y):
        self.rect.x = x * cell_size
        self.rect.y = y * cell_size

all_sprites = pygame.sprite.Group()

blocks = []
for i in range(15):
    block = Block(randrange(0, width // cell_size), randrange(0, height // cell_size))
    while pygame.sprite.spritecollideany(block, all_sprites):
        block.set_pos(randrange(0, width // cell_size), randrange(0, height // cell_size))
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


